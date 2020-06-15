from django.contrib import admin
from django.urls import path

from rest_framework.authtoken import views as auth_views

from api.views import BookList, BookDetail

admin_routes = [path('admin/', admin.site.urls), ]

app_routes = [path('book/', BookList.as_view()), path('book/<int:id>', BookDetail.as_view())]

token_routes = [path('api-token-auth/', auth_views.obtain_auth_token)]

urlpatterns = admin_routes + app_routes + token_routes
