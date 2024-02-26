# urls.py

# from django.contrib import admin          # Not required
from django.urls import path
from django_runtime.views import check_website, result_view, api_check_website

# Routes for our APP
urlpatterns = [
    # path('admin/', admin.site.urls),           # Not required
    path('', check_website, name='check_website'),
    path('result/', result_view, name='result_view'),
    path('api/', api_check_website, name='api_check_website'),
]
