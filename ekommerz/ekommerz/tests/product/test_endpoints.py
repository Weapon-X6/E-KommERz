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

    def test_return_all_products(self, product_factory, api_client):
        product_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4

    def test_return_single_product_by_slug(self, product_factory, api_client):
        obj = product_factory(slug='it"s about you')

        response = api_client().get(f"{self.endpoint}{obj.slug}/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_return_products_by_category_name(
        self, category_factory, product_factory, api_client
    ):
        cat = category_factory(slug="cat-chat")
        product_factory(category=cat)

        response = api_client().get(f"{self.endpoint}category/{cat.slug}/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
