# Django App with Mocking objects to test
This project was done to learn about Django's object mocking to run tests. I have used various libraries to do this, they are listed below

- used `django 2.15`
- used `mixer.blend` for mocking `objects`
- used `pytest.mark.django_db` to mock `database`
- used `RequestFactory` to mock `request`
- used `AnonymousUser` to mock a non logged in user
- used `python coverage` to test what files need testing, and how much is tested
- used `python fixtures` to create factory for re-using the objects

Referenced tutorials : 
- https://www.youtube.com/watch?v=B-qYGeLpUtE (full series)
