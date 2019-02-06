from mixer.backend.django import mixer
import pytest

from products.models import Product


@pytest.mark.django_db
class TestModels:

    def test_product_is_in_stock(self):
        product = mixer.blend('products.Product', quantity=1)
        assert product.is_in_stock == True

    def test_product_is_not_in_stock(self):
        product = mixer.blend('products.Product', quantity=0)
        assert product.is_in_stock == False

#--------------NOW with fixtures
@pytest.fixture
def product(request,db):
    return mixer.blend(Product,quantity=request.param)


@pytest.mark.parametrize('product',[1], indirect=True)
def test_product_is_in_stock(product):
    assert product.is_in_stock == True

@pytest.mark.parametrize('product',[0], indirect=True)
def test_product_is_not_in_stock(product):
    assert product.is_in_stock == False