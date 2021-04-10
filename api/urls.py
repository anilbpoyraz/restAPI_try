from django.urls import path, include
from .views import  ArticleView, ArticleDetails, GenericAPIView,\
    ArticleViewSet, ArticleGenericViewSet, ArticleModalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleModalViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleView.as_view()),
    path('detail/<int:pk>/', ArticleDetails.as_view()),
    path('generic/article/<int:pk>/', GenericAPIView.as_view()),
    path('viewset/<int:pk>', include(router.urls))
    # path('detail/<int:pk>/', article_detail)
]
