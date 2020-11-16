from django.urls import path, include
from rest_framework.routers import DefaultRouter
from purchase import views

router = DefaultRouter()
router.register('card', views.CardView)
router.register('purchase', views.PurchaseView)

urlpatterns = [
    path('', include(router.urls)),
]
