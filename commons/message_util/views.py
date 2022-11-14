from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics
from .serializers import EmailMessageSerializer
from .models import EmailMessage

# Create your views here.
class SendEmail(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['subject', 'message_body']

    def post(self, request):
        data = request.data
        recievers =data.recievers
        emails = []
        for reciever in recievers:
            email.append(reciever.email)
        send_mail(data.subject,  data.message_body,  settings.EMAIL_HOST_USER,[emails],fail_silently=False,)

