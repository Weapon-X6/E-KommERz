import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        obj = category_factory(name="conejo")
        assert obj.__str__() == "conejo"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        obj = brand_factory(name="gatillo")
        assert obj.__str__() == "gatillo"


class TestProductModel:
    def test_str_method(self, product_factory):
        obj = product_factory(name="rush")
        assert obj.__str__() == "rush"


class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        obj = product_line_factory(sku="MTF2207131123")
        assert obj.__str__() == "test_produkt / MTF2207131123"

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        produkt = product_factory()
        product_line_factory(product=produkt, order=1)

        with pytest.raises(ValidationError):
            product_line_factory(product=produkt, order=1).clean()
