
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('',include('home.urls')),

    #makeappoitment
    path('makeappoitment/',include('appoitment.urls')),

    #service
    path('service/',include('service.urls')),
    
    #dentists
    path('dentists/',include('dentist.urls')),

    #contact
    path('contact/',include('contact.urls')),

    #rest_fraemwork
    path('api-auth/', include('rest_framework.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
