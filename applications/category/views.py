from rest_framework import generics
from commons.authentication.permissions import CustomPermission
from applications.category.models import Category
from applications.category.serializers import CategorySerializer
from rest_framework import filters
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse
from commons.utils.paginations import CustomCursorPagination
from http import HTTPStatus
# Create your views here.

from commons.utils.file_utils import render_to_pdf


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCategory(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.order_by('?')
    serializer_class = CategorySerializer

    pagination_class = CustomCursorPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['category_name', 'description']
    ordering_fields = ['category_name', 'description']
    def post(self, request, *args, **kwargs):
        x = Category.objects.filter(category_name = 'food').last()
        request.data.__setitem__( 'category_name', 'x.description')
        create =self.create(request, *args, **kwargs)
        return create


class GeneratePdf(generics.ListAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()
    def get(self,request):
        data = {"category": Category.objects.all()}
        pdf = render_to_pdf('invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

