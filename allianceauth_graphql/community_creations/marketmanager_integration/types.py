from graphene_django import DjangoObjectType
from allianceauth.services.hooks import get_extension_logger
from marketmanager.models import Order


logger = get_extension_logger(__name__)

class OrderType(DjangoObjectType):

    class Meta:
        model = Order
