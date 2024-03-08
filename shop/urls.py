# from django.urls import path, include
# from shop.views import ProductListView, ProductRetrieveAPIView, ProductDestroyAPIView
#
# urlpatterns = [
#     path('products/', ProductListView.as_view(), name='list'),
#     path('products/<int:pk>', ProductRetrieveAPIView.as_view(), name='retrieve'),
#     path('products/<int:pk>/destroy', ProductDestroyAPIView.as_view(), name='destroy'),
# ]

from rest_framework.routers import DefaultRouter

from shop.views import ProductListView

router = DefaultRouter()

router.register('products', ProductListView, basename='products')

urlpatterns = router.urls
