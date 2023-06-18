import pytest

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
