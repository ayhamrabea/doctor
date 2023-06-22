from .serializers import contact_seria
from .models import modelcontact
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def contact_api(request):
    all_contact = modelcontact.objects.all()
    data = contact_seria(all_contact,many=True).data

    return Response({'data':data})