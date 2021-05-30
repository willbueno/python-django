"""taxistasonsm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import taxistas
from investimentos import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="home.html")),
	url(r'^taxistas/',include('taxistas.urls')),
	url(r'^investimentos/',include('investimentos.urls')),
	url(r'^corridas/',include('corridas.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^login/$', taxistas.views.login, name='login'),
	url(r'^$',views.lucro, name='lucro'),
	url(r'^lucro/',views.lucro, name='lucro'),
]