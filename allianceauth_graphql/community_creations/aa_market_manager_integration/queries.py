import graphene
from graphql_jwt.decorators import login_required, permission_required

from marketmanager.models import Order
from .types import OrderType


class Query:
    order = graphene.Field(OrderType, id=graphene.Int(required=True))

    @login_required
    @permission_required('marketmanager.basic_market_browser')
    def resolve_order(self, info, id):
        return Order.objects.get(pk=id)
