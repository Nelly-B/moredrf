from django.urls import path, include
from .views import postsView, post_details, PostsAPIView, postDetailAPIView,GenericApiView, PostViewSet

from rest_framework import routers
router = routers.SimpleRouter
router.register('posts', PostsAPIView, basename='posts')

urlpatterns = [
    path('postsGenericAPIView/', GenericApiView.as_view(), name='postsAPIView'),

    path('postsGenericAPIViewUpdate/<int:id>/', GenericApiView.as_view(), name='postsAPIView'),


    path('postsAPIView/', PostsAPIView.as_view(), name='postsAPIView'),
    path('detailsAPIView/<int:pk>', postDetailAPIView.as_view(), name='detailsAPIView'),
    

    path('posts/', postsView, name='posts'),
    path('details/<int:pk>', post_details, name='details'), 
    # path('', include('router.urls'))

]

urlpatterns += router.urls