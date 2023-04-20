from django.urls import path
from .views import (
    ListCreateServiceAPIView, CreateConnectionAPIView,
    FetchPublicKeyAPIView, ListAllServiceAPIView,
    ConnectionDetailAPIView
)
app_name = 'services'
urlpatterns = [
    path('fetch-public-key/', FetchPublicKeyAPIView.as_view(), name='fetch-public-key'),

    path('service/all/', ListAllServiceAPIView.as_view(), name='list-all-service'),

    path('connection/new/', CreateConnectionAPIView.as_view(), name='create-connection'),
]
