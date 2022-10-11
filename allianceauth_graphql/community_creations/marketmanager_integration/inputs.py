import graphene

class OrderInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    value = graphene.Int(required=True)

