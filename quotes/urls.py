from django.conf.urls import url

from . import views

urlpatterns = [
			url(r'^quotes$', views.quotes, name = 'quote_list'),
]