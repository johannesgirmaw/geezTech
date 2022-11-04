from django.shortcuts import render
from rest_framework import generics, permissions
from applications.category.models import Category
from applications.category.serializers import CategorySerializer
from rest_framework import filters
# Create your views here.
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCategory(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Category.objects.all().filter(category_name = 'food')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name', 'description']

class GeneratePdf(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        data = {
             'today': 12, 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

