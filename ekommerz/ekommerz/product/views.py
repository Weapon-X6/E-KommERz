from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """A simple ViewSet for viewing all categories."""

    queryset = Category.objects.all().isactive()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """A simple ViewSet for viewing all brands."""

    queryset = Brand.objects.all().isactive()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.GenericViewSet):
    """A simple ViewSet for viewing all Products."""

    queryset = Product.objects.all().isactive()
    serializer_class = ProductSerializer
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = (
            self.get_queryset().filter(slug=slug).select_related("category", "brand")
        )
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request):
        serializer = ProductSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)",
    )
    def list_product_by_category_slug(self, request, slug):
        """An endpoint to return products by category."""
        queryset = self.get_queryset().filter(category__slug=slug)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
