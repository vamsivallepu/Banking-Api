import graphene
from graphene_django.types import DjangoObjectType
from .models import Bank, Branch
from graphql import GraphQLError

# GraphQL types for Bank and Branch models
class BankType(DjangoObjectType):
    class Meta:
        model = Bank


class BranchType(DjangoObjectType):
    class Meta:
        model = Branch

# GraphQL queries for banks and branches
class Query(graphene.ObjectType):
    # Query to list all banks
    banks = graphene.List(BankType, description="List all banks")

    # Query to list all branches
    branches = graphene.List(BranchType, description="List all branches")

    # Query to retrieve a branch by its IFSC code
    branch_by_ifsc = graphene.Field(
        BranchType,
        description="Retrieve a branch by its IFSC code",
        ifsc=graphene.String(required=True),
    )

    def resolve_banks(self, info):
        # Resolver logic to fetch all banks
        return Bank.objects.all()

    def resolve_branches(self, info):
        # Resolver logic to fetch all branches
        return Branch.objects.all()

    def resolve_branch_by_ifsc(self, info, ifsc):
        try:
            # Attempt to retrieve a branch by its IFSC code
            return Branch.objects.get(ifsc=ifsc)
        except Branch.DoesNotExist:
            # Handle the case when branch is not found
            raise GraphQLError("Sorry, branch with IFSC code {} does not exist!".format(ifsc))
            # return None


# Create a GraphQL schema with the defined queries
schema = graphene.Schema(query=Query)
