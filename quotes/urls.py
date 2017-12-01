from django.conf.urls import url

from . import views

urlpatterns = [
			url(r'^quotes$', views.quotes, name = 'quote_list'),
			url(r'^quotes/(?P<quote_id>[0-9]+)$', views.quote_by_id, name = 'quote_by_id'),
]