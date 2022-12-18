


from django.contrib import admin
from django.urls import path

from .view import find_Wallpapers, set_new_background

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", find_Wallpapers),
    path("set/", set_new_background),
]
