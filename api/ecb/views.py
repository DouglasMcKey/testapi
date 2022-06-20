import decimal
import requests

from django.core.validators import EMPTY_VALUES

from api.ecb.constants import DATA_ENDPOINT, DATA_FLOWREF, DATA_RESOURCE


def get_exchange_rate(base_currency: str, currency_denominator: str = "EUR", frequency: str = "D", exchange: str = "SP00", variation: str = "A", filter_parameters: dict = None) -> decimal or None:
    """
    This function fetches the exchange rate for the given currency from the
    ECB SDMX 2.1 RESTful web service. https://sdw-wsrest.ecb.europa.eu/help/
    :param base_currency str
    :param currency_denominator str convert currency to this denominator.
    :param frequency str
    :param exchange str
    :param variation str
    :param filter_parameters str or None
    :returns: Decimal or None
    """
    response = None

    # Build URL Key.
    URL_KEY = f"{frequency}.{base_currency}.{currency_denominator}.{exchange}.{variation}"

    # Build the URL. i.e. wsEntryPoint/resource/flowRef/key?parameters
    url = f"{DATA_ENDPOINT}/{DATA_RESOURCE}/{DATA_FLOWREF}/{URL_KEY}"

    try:
        # Call the API. Include the parameters, if applicable.
        if filter_parameters:
            request = requests.get(url, params=filter_parameters)
        else:
            request = requests.get(url)

        if request.status_code == 200:
            response = request.json()

            # Process the response to extract the exchange rate.
            if response["dataSets"] not in EMPTY_VALUES:
                dataset = response["dataSets"][0]
                if dataset not in EMPTY_VALUES:
                    observations = dataset.get("series").get("0:0:0:0:0").get("observations")
                    if observations not in EMPTY_VALUES:
                        last_observation = observations.get(f"{len(observations) - 1}")
                        response = decimal.Decimal(last_observation[0])

        # If the request was successful, no exceptions will be raised.
        request.raise_for_status()

    except requests.exceptions.HTTPError as http_error:
        print(f"Error: {http_error}")
    except Exception as ex:
        print(f"Error: {ex}")

    return response
