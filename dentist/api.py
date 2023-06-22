from .serializers import dentist_seria
from .models import doctor
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def dentist_api(request):
    all_dentist = doctor.objects.all()
    data = dentist_seria(all_dentist,many=True).data

    return Response({'data':data})