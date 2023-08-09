# GO2 PYTHON EXAM

This is a technical exam for python engineer for Go2 which involves creating a Django application that can provide responses through different API endpoints. Written using
Django, DRF, and other libraries.

## Table of Contents

1. [Requirements](#requirements)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Running the Application](#running-the-application)
3. [Endpoints and Usage](#usage)
   - [Accessing the Application](#accessing-the-application)
   - [Adding/Updating Products](#adding-updating-products)
   - [Other Custom Behaviors](#other-custom-behaviors)

## Requirements

Before running the project, make sure you have the following installed on your system:

- Docker
- Docker Compose
- Postman (optional) for testing the API endpoints

## Getting Started

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/drewbuensuceso/go2_python.git
cd order_processing_project
```

2. For database creation and setup, run:

```bash
docker-compose run web python manage.py migrate
```

### Running the Application
1. To run the application for the first time and build the docker images, run:
```bash
docker-compose up --build 
```
If not first time run you can remove the option ```--build```:

```bash
docker-compose up 
```

## Endpoints and Usage

### API Endpoints

1. ```GET```api/products/available/
2. ```GET```api/products/out-of-stock/
3. ```POST```api/products/update-status/<int:pk>/
4. ```PUT```api/products/create/
5. ```POST``` api/products/order/

### Usage

After running the server successfully 


#### 1. AVAILABLE PRODUCTS

Send a GET request to localhost:8000/api/products/available/

#### 2. OUT OF STOCK PRODUCTS

Send a GET request to localhost:8000/api/products/out-of-stock/


#### 3. CREATE

Send a POST request to http://localhost:8000/api/products/create/ containing a in the request body a JSON in the following format:

```json
{   
    "name":"Sample Available Product 3",
    "sku": "132114",
    "price": 11.00,
    "description": "This is a sample product",
    "quantity": 0,
    "status": false
}
```

#### 4. UPDATE

Send a PUT request to http://localhost:8000/api/products/update-status/<primary key of product>/ containing a in the request body a JSON in the following format:

```json
{   
    "status": true
}
```

#### 5. ORDER PROCESSING ENDPOINT

Send a POST request to http://localhost:8000/api/products/order/ containing a in the request body a JSON in the following format:

```json
{
    "order_number": "12345",
    "items": [
        {
            "sku": "000002",
            "quantity": 2
        },
        {
            "sku": "000003",
            "quantity": 1
        }
    ],
    "customer": {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "address": "123 Main St, Anytown USA"
    }
}
```
