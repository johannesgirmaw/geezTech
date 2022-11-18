from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from http import HTTPStatus

from rest_framework import generics
from .serializers import EmailMessageSerializer
from .models import EmailMessage
from commons.authentication.permissions import CustomPermission
from commons.authentication.models import CustomUser

# Create your views here.
class SendEmail(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer
    search_fields = ['subject', 'message_body']

    def post(self, request):
        data = request.POST
        recievers = dict(data)['recievers']
        emails = []
        print(data, recievers)
        for reciever in recievers:
            user = CustomUser.objects.get(id = reciever)
            emails.append(user.email)
        send_mail(data['subject'],  data['message_body'],  settings.EMAIL_HOST_USER, emails)
        return JsonResponse({'data':"message send"},status = HTTPStatus.ACCEPTED)

