from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.agora_token_generation import RtcTokenBuilder, Role_Publisher
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

# Create your views here.

@api_view(['GET'])
def generate_token(request, username, channel):
    try:
        User.objects.get(username=username)
    except ObjectDoesNotExist:
        return Response(status=403)
    token = RtcTokenBuilder().build_token_with_user_account(
        settings.AGORA_APP_ID,
        settings.AGORA_APP_CERTIFICATE,
        channel,
        username,
        Role_Publisher,
        1800,
    )
    return Response({'token': token}, 200)


@api_view(['GET'])
def brew_coffee(request):
    return Response(status=418)
