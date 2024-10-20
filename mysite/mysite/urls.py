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
"""
from django.contrib import admin
from django.urls import path, include
from polls.urls import *
from . import views
#import views


def sig():
    print("Signal 1 that there is output");
    
sig();
views.signal2();
urlpatterns = [
    #path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
    #path('polls/', views.my_view, name='my-view'),
    path('polls/', views.my_view),
    path('polls/', views.index),
]
"""

from django.contrib import admin
from django.urls import path, include
from polls.urls import *  # Import all URL patterns from polls.urls

from . import views  # Import views from the current app
def sig():
    print("Signal 1 that there is output");
    
sig();
views.signal2();

import logging

logger = logging.getLogger(__name__)

def my_view(request):
    informate=logger.info(request.META);
    print( informate);
    # ... rest of your view logic


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('polls/', views.my_view),
    path("polls/", include("polls.urls")),
    path('', views.entry),
    path('ts/', include("TS1Proj.urls")),
    #path('polls/', views.index),  # Uncomment if you prefer the default view
]
