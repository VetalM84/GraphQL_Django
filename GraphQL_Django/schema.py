import graphene

from graphql_app import schema

# from graph_app_two import mutations


class Query(schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


# class Mutation(mutations.Mutation, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)
