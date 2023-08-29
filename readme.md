# GraphQL Bank Branch API

This project provides a GraphQL API for querying banks and branches. It's built using the `graphene-django` library and integrates with Django models.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Methodology](#methodology)
  - [Example Queries](#example-queries)

## Getting Started

- To experiment with the API, you can use the hosted version at [HERE](https://web-production-cb4e.up.railway.app/gql).

### Prerequisites

- Python (>=3.8)
- Django (>=4.2)

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

## Methodology
### 1.  Defining GraphQL Types
I began by creating GraphQL types for the Bank and Branch models. To achieve this, we utilized the `graphene_django.types.DjangoObjectType class`. This allowed us to establish a clear mapping between our existing Django models and the GraphQL schema. By setting up these types, we laid the foundation for interacting with the data through GraphQL queries.

### 2. Designing GraphQL Queries
The next step involved constructing the GraphQL queries that would enable users to retrieve information about banks and branches. We defined three main queries:

- banks: This query retrieves a list of all banks present.
- branches: This query fetches a list of all branches available along with the corresponding bank details.
- branch_by_ifsc: This query lets users retrieve a specific branch by providing its unique IFSC code.

### 3. Resolving the Queries
To fulfill these queries with data, I implemented resolver functions for each query. These resolver functions acted as the bridge between the GraphQL queries and the Django models. Inside these functions, I utilized Django's Object-Relational Mapping (ORM) capabilities to fetch data from the underlying database.
For instance, the resolver for the banks query used `Bank.objects.all()` to fetch all banks, and the resolver for `branch_by_ifsc` query utilized `Branch.objects.get(ifsc=ifsc)` to retrieve a branch based on its IFSC code.

## Example Queries :
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


