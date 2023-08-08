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
### Running the Application

2. Clone this repository to your local machine:

```bash
docker-compose up --build
```

## Endpoints and Usage

### API Endpoints

1. ```GET```api/available/
2. ```GET```out-of-stock/
3. ```POST```update-status/<int:pk>/
4. ```POST```create/

### Usage

1. put usage demo here