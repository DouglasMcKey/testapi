import decimal
import datetime

import django_countries
from dateutil.relativedelta import relativedelta

from api.ecb.views import get_exchange_rate
from api.models import ExchangeRateHistory
from transactions.models import Transaction, TransactionType


def save_transaction_data(data, year, currency_denominator):
    """
    This function saves transactions data that is received via an uploaded CSV
    file. The data is received as a list of dictionaries and must have the
    following format:
    [
        {
            'Date': '2021/4/28',
            'Purchase/Sale': 'purchase',
            'Country': 'Italy',
            'Currency': 'USD',
            'Net': '41.75',
            'VAT': '7.93'
        }
    ]
    :parameter data list of dictionaries.
    :parameter year year data is allowed for.
    :parameter currency_denominator the currency the values must be converted to.
    :returns: Nothing
    """
    for row in data:
        # Identify the data fields for each row.
        i_date = row["Date"].lower()
        i_transaction_type = row["Purchase/Sale"].strip().lower().capitalize()
        i_country = row["Country"]
        i_currency = row["Currency"]
        i_net = row["Net"]
        i_vat = row["VAT"]

        # Explicitly ignoring AED records as there is no AED data available through the API.
        # TODO: A decision needs to be made on how to handle transactions made with AED.
        if i_currency == "AED":
            continue

        formatted_date = i_date.replace("/", "-")
        # Convert the date string to a date object or continue.
        try:
            formatted_date = datetime.datetime.strptime(formatted_date, "%Y-%m-%d").date()
            if not formatted_date.year == year:
                continue
        except ValueError:
            continue

        # Manage some noted spelling mistakes.
        if i_transaction_type == "Sele":
            i_transaction_type = "Sale"
        if i_transaction_type == "Parchase":
            i_transaction_type = "Purchase"

        # Get the transaction type or continue.
        try:
            formatted_transaction = TransactionType.objects.get(
                name__iexact=i_transaction_type
            )
        except TransactionType.DoesNotExist:
            continue

        # Get the country or continue.
        formatted_country = None
        for country in django_countries.countries:
            if i_country == country.code or i_country == country.name:
                formatted_country = country.code
        if not formatted_country:
            continue

        # Manage the currency and monetary values.
        currency = f"{i_currency}".upper()
        net_amount = decimal.Decimal(i_net)
        vat_amount = decimal.Decimal(i_vat)

        if not currency == currency_denominator:
            # Get the exchange rate history object from the database.
            exchange_rate_object = None
            try:
                exchange_rate_object = ExchangeRateHistory.objects.get(
                    currency=currency,
                    observation_date=formatted_date
                )
            except ExchangeRateHistory.DoesNotExist:
                # If there is no data for a particular day, it is assumed that
                # the day in question is either a weekend or a public holiday.
                # Therefore, regardless of country or calendar type, we search the
                # latest records for one week prior to today and up until today.
                # The last available entry will either be:
                # -> the exact exchange rate for the endPeriod or
                # -> the most recent exchange rate prior to the endPeriod.
                # This assumption should enable us to get a fairly accurate
                # exchange rate if not 100% accurate for all records.

                # Get the exchange rate through the API.
                parameters = {
                    "startPeriod": f"{formatted_date - relativedelta(days=7)}",
                    "endPeriod": f"{formatted_date}",
                    "detail": "dataonly",
                    "format": "jsondata"
                }
                exchange_rate = get_exchange_rate(currency, filter_parameters=parameters)

                # Create the exchange rate history object.
                if exchange_rate:
                    exchange_rate_object = ExchangeRateHistory.objects.create(
                        currency=currency,
                        currency_denominator=currency_denominator,
                        exchange_rate=exchange_rate,
                        observation_date=formatted_date
                    )

            # Apply the exchange rate to the vat and net amounts, if applicable.
            if exchange_rate_object:
                currency = exchange_rate_object.currency_denominator
                net_amount = net_amount * decimal.Decimal(exchange_rate_object.exchange_rate)
                vat_amount = vat_amount * decimal.Decimal(exchange_rate_object.exchange_rate)

        # Create the transaction in the database.
        Transaction.objects.create(
            date=formatted_date,
            transaction_type=formatted_transaction,
            country=formatted_country,
            currency=currency,
            net=net_amount,
            vat=vat_amount
        )
