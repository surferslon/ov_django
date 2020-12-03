from product.models import Product
from product.serializers import ProductListSerializer, ProductDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

