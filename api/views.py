from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.agora_token_generation import RtcTokenBuilder, Role_Publisher
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from jobs.models import Job

# Create your views here.

@api_view(['GET'])
def generate_token(request, username, channel):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return Response(status=403)
    token = RtcTokenBuilder().build_token_with_uid(
        settings.AGORA_APP_ID,
        settings.AGORA_APP_CERTIFICATE,
        channel,
        user.pk,
        Role_Publisher,
        3600,
    )
    return Response({'token': token, 'app_id': settings.AGORA_APP_ID, 'uid': user.pk}, 200)

@api_view(['GET'])
def place_in_queue(request, username, channel):
    job = Job.objects.get(channel__pk=channel)
    for index, user in enumerate(job.joinedUsers.all()):
        if user.username == username:
            return Response({'place': index}, 200)
    return Response(status=404)

@api_view(['GET'])
def leave_queue(request, username, channel):
    job = Job.objects.get(channel__pk=channel)
    job.joinedUsers.remove(job.joinedUsers.get(pk=username))
    return Response(status=200)


@api_view(['GET'])
def brew_coffee(request):
    return Response(status=418)
