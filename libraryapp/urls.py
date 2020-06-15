from django.contrib import admin
from django.urls import path

from api.views import authetication, book

admin_routes = [path('admin/', admin.site.urls), ]

app_routes = [
    path('book/', book.BookList.as_view()),
    path('book/<int:id>', book.BookDetail.as_view())
]

token_routes = [
    path('api-token-auth/', authetication.CustomAuthToken.as_view())
]

urlpatterns = admin_routes + app_routes + token_routes
