"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the current app
import logging
logger = logging.getLogger(__name__)


#from.import googcal;
import requests;
import os;
print("from urls");
print("api test");
print(requests.get("https://www.googleapis.com/calendar/v3"));
print(requests.get("https://www.googleapis.com/calendar/v3/users/me/calendarList"));
print("os.getcwd() - ",os.getcwd());
#googcal.main();




def my_view(request):
    informate=logger.info(request.META);
    print(informate);
    # ... rest of your view logic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.entry),
    path('ts/', include("TS1Proj.urls")),
    path('upload/', views.upload), 
    path('--bogo/', views.input), 
    path('clear_served_files/', views.clear_served_files), 
]
