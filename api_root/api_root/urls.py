from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get_all', include('to_do_list_api.urls'), name='to_do_list_api')
]
