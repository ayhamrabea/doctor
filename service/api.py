from .serializers import service_seria
from .models import service
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def service_api(request):
    all_contact = service.objects.all()
    data = service_seria(all_contact,many=True).data

    return Response({'data':data})