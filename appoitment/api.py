from .serializers import Appoitment_seria
from .models import Appoitment
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def Appoitment_api(request):
    all_Appoitment = Appoitment.objects.all()
    data = Appoitment_seria(all_Appoitment,many=True).data

    return Response({'data':data})