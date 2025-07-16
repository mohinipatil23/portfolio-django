from django.contrib import admin
from django.urls import path

from portfolioapp1 import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # portfolioapp1 views
    path('', views.home, name='home'),          
    path('resume/', views.resume, name='resume'),  
]
