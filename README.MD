# GO2 PYTHON EXAM

This is a technical exam for python engineer for Go2 which involves creating a Django application that can provide responses through different API endpoints. Written using
Django, DRF, and other libraries.

## Table of Contents

1. [Requirements](#requirements)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Running the Application](#running-the-application)
3. [Endpoints and Usage](#usage)
   - [API Endpoints](#api-endpoints)
   - [Usage](#usage)
   
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

Send a ```GET``` request to localhost:8000/api/products/available/

<img width="960" alt="Get available products" src="https://github.com/drewbuensuceso/go2_python/assets/42257616/5571e456-ad9f-4b2b-924d-c42036e06751">

#### 2. OUT OF STOCK PRODUCTS

Send a ```GET``` request to localhost:8000/api/products/out-of-stock/

<img width="960" alt="out of stock list" src="https://github.com/drewbuensuceso/go2_python/assets/42257616/129ba365-c8bb-4d39-af72-00bfc43f2eb5">


#### 3. CREATE

Send a ```POST``` request to http://localhost:8000/api/products/create/ containing a in the request body a JSON in the following format:

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
A successful product creation will return a 201 Created response 
<img width="960" alt="product created" src="https://github.com/drewbuensuceso/go2_python/assets/42257616/80684391-0df1-40f6-9263-c33b61e0c056">

#### 4. UPDATE STATUS

Send a ```PUT``` request to http://localhost:8000/api/products/update-status/primary_key_of_product/ containing a in the request body a JSON in the following format:

```json
{   
    "status": true
}
```

<img width="959" alt="successful update product" src="https://github.com/drewbuensuceso/go2_python/assets/42257616/e2566fff-b0a9-4375-9879-7c833946ecf2">

#### 5. ORDER PROCESSING ENDPOINT

Send a ```POST``` request to http://localhost:8000/api/products/order/ containing a in the request body a JSON in the following format:

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
#### SUCCESSFUL ORDER
<img width="960" alt="successful order" src="https://github.com/drewbuensuceso/go2_python/assets/42257616/fb651478-3ae6-44ae-8750-8064fa603cd3">

#### ORDER WITH AN OUT-OF-STOCK ITEM
<img width="960" alt="order with out of stock" src="https://github.com/drewbuensuceso/go2_python/assets/42257616/50b7b259-94b0-4c3e-9ef2-fb3307b80c57">
