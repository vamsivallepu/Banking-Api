# GraphQL Bank Branch API

This project provides a GraphQL API for querying banks and branches. It's built using the `graphene-django` library and integrates with Django models.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Development Server](#running-the-development-server)
  - [GraphQL Queries](#graphql-queries)

## Getting Started

- To experiment with the API, you can use the hosted version at [HERE](https://web-production-cb4e.up.railway.app/gql).

### Prerequisites

- Python (>=3.8)
- Django (>=3.2)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/Bank-Api.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Bank-Api
   ```
3. Install the dependencies:
   ```sh
    pip install -r requirements.txt
    ```
## Usage
1. Apply Migrations 
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
2. Start the Development Server
    ```sh
    python manage.py runserver
    ```
3. Access the GraphQL Playground: <br>
Open your browser and navigate to `http://127.0.0.1/gql/` to access the GraphQL Playground.

## GraphQL Queries
The API provides the following queries:

- `banks`: List all banks.
- `branches`: List all branches along with corresponding bank details.
- `branch_by_ifsc`: Retrieve a branch by its IFSC code.

Example Queries :
1. List all banks
    ```graphql
    query {
        banks {
            id
            name
        }
    }
    ```
2. List all branches along with corresponding bank details.
    ```graphql
    query {
        branches {
            ifsc
            bank {
                id
                name
            }
            branch
            address
            city
            district
            state
        }
    }
    ```
3. Retrieve a branch by its IFSC code.
    ```graphql
    query {
        branchByIfsc(ifsc: "ABHY0065001") {
            ifsc
            bank {
                id
                name
            }
            branch
            address
            city
            district
            state
        }
    }
    ```


