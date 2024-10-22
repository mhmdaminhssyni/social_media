from django.urls import path
# from .views import PostListView, PostDetailView
from .views import PostView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'', PostView, basename= 'posts')

urlpatterns = [
    # path('', PostListView.as_view()),
    # path('<int:pk>/', PostDetailView.as_view())
    # path('', PostListView.as_view({"get": 'list', "post": 'create'})),
    # path("<int:pk>/", PostView.as_view({"get": 'retrieve', 'put': 'update', 'delete': 'destroy'}))
    path('', include(router.urls))
]



