from .views import home
from django.urls import path

app_name="blog"
urlpatterns=[
    path( '', home),
]
