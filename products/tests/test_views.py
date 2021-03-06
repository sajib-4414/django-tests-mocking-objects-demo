from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from django.contrib.auth.models import User, AnonymousUser
from products.models import Product
from products.views import product_detail
import pytest


@pytest.mark.django_db
class TestViews():
    def test_product_detail_authenticated(self):
        #creating a mock product
        mixer.blend(Product)
        #taking the path and by supplying kwargs creating a full path
        path = reverse('detail',kwargs={'pk':1})
        #mocking an HTTP request
        request = RequestFactory().get(path)
        #creatng a mock user and assigns it to the request
        request.user = mixer.blend(User)

        #mocking, passing an HTTP request with parameters in the view method
        response = product_detail(request,pk=1)
        #checking if it gives status 200 or not, we are passing an user, so it is authenticated call. So it will return 200
        assert response.status_code == 200

    def test_product_detail_unauthenticated(self):
        #creating a mock product
        mixer.blend(Product)
        #taking the path and by supplying kwargs creating a full path
        path = reverse('detail',kwargs={'pk':1})
        #mocking an HTTP request
        request = RequestFactory().get(path)
        #creatng a non logged in user scenario
        request.user = AnonymousUser()

        #mocking, passing an HTTP request with parameters in the view method
        response = product_detail(request,pk=1)
        #checking if the response contains this hit to login
        assert "accounts/login" in response.url


#---------------------------NOW doing the same test using testcase
from django.test import TestCase
@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUp(cls):
        super(TestViews,cls).setUpClass()
        #creating a mock product
        mixer.blend(Product)
        cls.factory = RequestFactory()



    def test_product_detail_authenticated(self):
        #taking the path and by supplying kwargs creating a full path
        path = reverse('detail',kwargs={'pk':1})
        #mocking an HTTP request
        request = self.factory.get(path)
        #creatng a mock user and assigns it to the request
        request.user = mixer.blend(User)

        #mocking, passing an HTTP request with parameters in the view method
        response = product_detail(request,pk=1)
        #checking if it gives status 200 or not, we are passing an user, so it is authenticated call. So it will return 200
        assert response.status_code == 200

    def test_product_detail_unauthenticated(self):
        #taking the path and by supplying kwargs creating a full path
        path = reverse('detail',kwargs={'pk':1})
        #mocking an HTTP request
        request = self.factory.get(path)
        #creatng a non logged in user scenario
        request.user = AnonymousUser()

        #mocking, passing an HTTP request with parameters in the view method
        response = product_detail(request,pk=1)
        #checking if the response contains this hit to login
        assert "accounts/login" in response.url

#--------------------------Now doing the same test using Fixtures

@pytest.fixture(scope='module')
def factory():
    print("Factory instantiated")
    return RequestFactory()

@pytest.fixture
def product(db):
    return mixer.blend(Product)

def test_product_detail_authenticated(factory, product):
    #taking the path and by supplying kwargs creating a full path
    path = reverse('detail',kwargs={'pk':1})
    #mocking an HTTP request
    request = factory.get(path)
    #creatng a mock user and assigns it to the request
    request.user = mixer.blend(User)

    #mocking, passing an HTTP request with parameters in the view method
    response = product_detail(request,pk=1)
    #checking if it gives status 200 or not, we are passing an user, so it is authenticated call. So it will return 200
    assert response.status_code == 200

def test_product_detail_unauthenticated(factory,product):
    #taking the path and by supplying kwargs creating a full path
    path = reverse('detail',kwargs={'pk':1})
    #mocking an HTTP request
    request = factory.get(path)
    #creatng a non logged in user scenario
    request.user = AnonymousUser()

    #mocking, passing an HTTP request with parameters in the view method
    response = product_detail(request,pk=1)
    #checking if the response contains this hit to login
    assert "accounts/login" in response.url