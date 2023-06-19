import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/api/categories/"

    def test_category_get(self, category_factory, api_client):
        category_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4


class TestBrandEndpoints:
    endpoint = "/api/brands/"

    def test_brand_get(self, brand_factory, api_client):
        brand_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4


class TestProductEndpoints:
    endpoint = "/api/products/"

    def test_product_get(self, product_factory, api_client):
        product_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4
