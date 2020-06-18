from django.views.decorators.cache import cache_page
from django.contrib import admin
from django.urls import path

from libraryapp import settings
from api.views import authetication, book

cache_time = settings.CACHE_TIME

admin_routes = [
    path('admin/', admin.site.urls),
]

app_routes = [
    path('book/', cache_page(cache_time)(book.BookList.as_view())),
    path('book/<int:id>', book.BookDetail.as_view())
]

token_routes = [
    path('api-token-auth/', authetication.CustomAuthToken.as_view())
]

urlpatterns = admin_routes + app_routes + token_routes
