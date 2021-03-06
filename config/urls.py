"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

admin.site.site_header = "Library Management System Admin"
admin.site.site_title = "Library Management System Admin Portal"
admin.site.index_title = "Welcome to Library Management System admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('member/', include('member.urls', namespace='member')),
    path('issue/', include('issue.urls', namespace='issue')),
    path('', include('book.urls', namespace='book')),
]

from django.conf import settings
if settings.DEBUG == True:

    from . import url_config

    urlpatterns += url_config.urlpatterns
