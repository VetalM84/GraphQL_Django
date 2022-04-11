"""Main Abstract scheme file for the GraphQL API."""

import graphene

from graphql_app import schema

from graphql_app import mutations


class Query(schema.Query, graphene.ObjectType):
    """This class will inherit from multiple Queries
    as we begin to add more apps to our project."""

    pass


class Mutation(mutations.Mutation, graphene.ObjectType):
    """This Abstarct class will inherit from multiple Mutations."""

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
