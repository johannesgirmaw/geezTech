from rest_framework import generics
from commons.utils.permissions import CustomPermission
from applications.category.models import Category
from applications.category.serializers import CategorySerializer
from rest_framework import filters
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse
from commons.utils.paginations import CustomCursorPagination
from http import HTTPStatus
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from commons.utils.file_utils import render_to_pdf


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCategory(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    pagination_class = CustomCursorPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['category_name', 'description']
    ordering_fields = ['category_name', 'description']

    # def post(self, request, *args, **kwargs):
    #     x = Category.objects.filter(category_name='food').last()
    #     request.data.__setitem__('category_name', 'x.description')
    #     create = self.create(request, *args, **kwargs)
    #     return create


class GeneratePdf(generics.ListAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()

    def get(self, request):
        data = {"category": Category.objects.all()}
        pdf = render_to_pdf('invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

# def category(request, pk=None,*args,**kwargs):
#     method = request.method

#     if method == 'GET':
#         if pk is not None:
#             query_set = get_object_or_404(Category,pk=pk)
#             data = CategorySerializer(query_set, many = False).data
#             Response(data)
#         else:
#             query_set  = Category.objects.all()
#             data = CategorySerializer(query_set, many =True).data
#             Response(data)
#     if method == "POST":
#         serializer = CategorySerializer(request.data)
#         if serializer.is_valid(raise_exception = True):
#             category_name = serializer.validated_data.get('category_name')
#             description = serializer.validate_data.get('description')
#             if description is None:
#                 description = category_name
#             serializer.save()
#         return Response(serializer.validated_data)


#     if method == 'PUT':
#         if pk is not None:
#             serializer = CategorySerializer(data =  request.data)
#             serializer.is_valid(raise_exception = True)
#             serializer.save()
#             data = serializer.validated_data

#             return Response(data)
