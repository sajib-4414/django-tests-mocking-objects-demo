# Django App with Tox automated test
This project was done to learn about Tox configuration in a Django project. Using the Tox, we can specify code formatiing, testing behavior, code coverage functionalities. Whole 
list of featues is beyond this scope. This project was done as a boilerplate to use this automated testing in my other projects.

- used `django 2.15`
- used `mixer.blend` for mocking `objects`
- used `pytest.mark.django_db` to mock `database`
- used `RequestFactory` to mock `request`
- used `AnonymousUser` to mock a non logged in user
- used `python coverage` to test what files need testing, and how much is tested
- used `python fixtures` to create factory for re-using the objects

Tutorials which are taken help from : 
- https://www.youtube.com/watch?v=B-qYGeLpUtE (full series)
