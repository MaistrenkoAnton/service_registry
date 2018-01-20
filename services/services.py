from services.models import Service


def get_service(pk):
    try:
        return Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return
