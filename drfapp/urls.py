from django.urls import path
from .views import postsView, post_details

urlpatterns = [
    path('posts/', postsView, name='posts'),
    path('details/<int:pk>', post_details, name='details')
]