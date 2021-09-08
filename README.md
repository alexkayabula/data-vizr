[![Build Status](https://app.travis-ci.com/alexkayabula/data-vizr.svg?branch=main)](https://app.travis-ci.com/alexkayabula/data-vizr)
[![Coverage Status](https://coveralls.io/repos/github/alexkayabula/data-vizr/badge.svg?branch=main)](https://coveralls.io/github/alexkayabula/data-vizr?branch=main)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f230cde42d9c4c6d89b08d3adcafb7b7)](https://www.codacy.com/gh/alexkayabula/data-vizr/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alexkayabula/data-vizr&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/77c91f1ec5d6b2dff460/maintainability)](https://codeclimate.com/github/alexkayabula/data-vizr/maintainability)

# DataVizr
DataVizr is an API that allows clients to access products and make orders.
The application also includes an administartor ssection that allows admins to manage orders and access data analytics for proper decision making.

Deployed Application API: https://datavizr.herokuapp.com/signup


### Features
    
    EndPoint                | Functionality
    ---------------------   | ----------------------
    POST /auth/signup       | Create a user account
    POST /auth/login        | Login a user [Admin credentials:username: admin, password: admin]
    POST /products          | Add a product 
    GET  /products          | View all products
    PUT  /products/<int:id> | Update product [Admin access]
    POST /users/orders      | Make an order
    GET  /users/orders      | Current logged in user's orders
    GET  /orders            | Get all client orders, [Admin access]
    PUT  /orders/<int:id>   | Update an order [Admin access]
    GET  /price_per_product | Get price per product dataset [Admin access]
    GET  /orders_per_product| Get orders per product dataset [Admin access]
    GET  /orders_per_user   | Get orders per product dataset [Admin access]
 

### Test the application locally.

In the terminal:>
- Clone the repository: git clone https://github.com/alexkayabula/data-vizr.git
- Cd into the project folder: `cd data-vizr`
- Install virtual environment: `python3 -m venv .env`
- Source virtual environment: `source .env/bin/activate`
- Install requirements: `pip3 install -r requirements`
- Install databases: `psql`; `CREATE DATABASE [YOUR_DB_NAME];`; `CREATE DATABASE [YOUR_TEST_DB_NAME];`
- Run application: `python3 run.py`
- In the browser, access the app at: `http:localhost:5000`

### Unit Tests.

In the terminal:>
- Run tests: `nosetests --with-coverage --cover-html --cover-package=app -v`

### Technologies used

- Python
- Flask
- PostgreSQL
