from django.urls import path
from .views import main, facts, photos, author, more

urlpatterns = [
    path('', main, name='main'),
    path('facts', facts, name='facts'),
    path('more', more, name='more'),
    path('photos', photos, name='photos'),
    path('author', author, name='author')
]