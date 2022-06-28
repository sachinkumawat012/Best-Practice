from django.contrib import admin
from django.urls import path
from redis_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('show/<int:id>', show),
    # path('home/', get_recipe),
]
