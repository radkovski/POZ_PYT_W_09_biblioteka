"""biblioteczka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biblioteczka_app.views import Blank, AddAuthor, AuthorDisplay, AuthorId, AddBook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Blank.as_view()),
    path('add/', AddAuthor.as_view(), name ='add'),
    path('author_list/', AuthorDisplay.as_view(), name='authors'),
    path('author/<int:id>/', AuthorId.as_view(), name='author'),
    path('add_book/', AddBook.as_view(), name='add_book')
]
