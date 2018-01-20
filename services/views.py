from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView

from services.models import Service
from services.serializers import ServiceSerializer


class ServiceCreateView(CreateAPIView):
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        response = super(ServiceCreateView, self).create(request, args, kwargs)
        response.message = 'created'
        return response


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('type', 'version')


class ServiceDeleteView(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def destroy(self, request, *args, **kwargs):
        response = super(ServiceDeleteView, self).destroy(request, args, kwargs)
        response.message = 'removed'
        return response


class ServiceUpdateView(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def partial_update(self, request, *args, **kwargs):
        response = super(ServiceUpdateView, self).partial_update(request, args, kwargs)
        response.message = 'changed'
        return response
