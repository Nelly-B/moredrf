from django.urls import path
from .views import postsView

urlpatterns = [
    path('posts/', postsView, name='posts')
]