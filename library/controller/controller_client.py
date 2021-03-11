from ..models import Client


def getClient(filter):
    client = Client.objects.get(**filter)
    return client