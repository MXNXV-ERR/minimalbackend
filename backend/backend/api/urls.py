from django.urls import path
from . import views

urlpatterns = [
    path('getPickelpredictions/',views.getPredPickelReview),
    path('getTensorpredictions/',views.getPredTensorReview),
    path('getImagePred/',views.getImagePred),
]