# testapi

---

This is the master code repository for `testapi`.
This projects is based on the Django Rest Framework

---

### Setup Guide

---
Please read carefully through the entire process below before starting. 

---

1) ###### Database
    Ensure that you have a MySQL database and user setup. Use the following credentials:
    - database name`testapi` (this is empty)
    - datebase user: `testapi`
    - database user password: `testapi`
---
2) ###### Clone the repository
---
3) ###### CLI Commands
   From the command line, run the following commands, in order, within the project root directory:
   - `> pipenv update`
   - `> pipenv run python manage.py migrate`
   - `> pipenv run python manage.py loaddata initial_data.json`
---
3) ###### Admin Access
   - Visit `http://localhost:8000/administration/`
   - Username: `admin@testapi.com`
   - Password: `testapi`
---

### My approach for the Process Step for the APi

Initially I was planning to use the Django cache table to store exchange rates 
and then refer to the cache table first before performing another API call.
However, after some consideration I felt the cache table should rather be 
utilized for more dynamic data. The exchange rates received through the API will 
never change.

This left me with two choices.
1) Call the API for every record `OR`
2) store the exchange rates as I receive them, and then refer to my stored exchange
rates before using the API again.

I opted for option 2.

With this approach the initial data will take a tad longer to run in order to 
populate the stored exchange rates, however, as more and more records are 
processed, the need for the API will diminish and eventually the API will be 
used in very few circumstances.

---

### Building a scalable solution for large data sets.
I have never had the opportunity to work with data of scale. However, my approach 
would be in line with the following:

###### Understand the data.
If we understand the data, it's size, source and format, then we will be able to
make better decisions when building out the solution.

###### Choosing a library over raw code.
In some cases, choosing a library that comes with powerful features can be a 
strong choice over raw code. So we don't always have to reinvent the wheel.

However, once we discover their powers can we potentially build more bespoke, 
more optimized and lighter code solutions with raw code.

###### Technology and tools.
With the vast array of digital services from cloud providers, the solution will 
likely include the use of their tools, combined with code or libraries where we 
can build a solution that can scale.

For this particular application, I would look for ways to partition the data 
for the ingestion queue. I would use an elastic server/container service (if available) 
that can scale based on the queue size.
