from rest_framework import generics
from commons.authentication.permissions import CustomPermission
from applications.category.models import Category
from applications.category.serializers import CategorySerializer
from rest_framework import filters
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

from commons.utils.file_utils import render_to_pdf


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCategory(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name', 'description']

class GeneratePdf(generics.ListAPIView):
    permission_classes = [CustomPermission]
    def get(self, request, *args, **kwargs):
        data = {"category": Category.objects.all()}
        pdf = render_to_pdf('invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
class SendEmail(generics.ListAPIView):
    # permission_classes = [CustomPermission]
    def get(self,request):
        message = "well come baby"
        email = request.user.email
        print(email)
        send_mail('well come',  message,  settings.EMAIL_HOST_USER,[email],fail_silently=False,)
    
        return HttpResponse('message send success fully')



