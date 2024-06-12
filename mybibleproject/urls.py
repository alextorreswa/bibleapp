"""
URL configuration for mybibleproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from bibleapp import views
from django.urls import path, include
from django.views.generic.base import TemplateView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")), 
    path('accounts/', include('django.contrib.auth.urls')),    
    path("", TemplateView.as_view(template_name="main.html"), name="main"), 
    # path('', views.main, name='main'),
    path('books/', views.books, name='books'),
    path('books/details/<int:id>', views.book, name='book'),
    path('read/<str:idbible>/<int:b>/<int:c>', views.read)
]
