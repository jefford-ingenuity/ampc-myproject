from django.urls import path

from books.views import search, contact, add_author, search_author, login_view, logout_view


app_name = "books"

urlpatterns = [
    path('search/', search, name="search"),
    path('contact/', contact, name="contact"),
    path('add-author/', add_author, name="add_author"),
    path('search-author/', search_author, name="search_author"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]

