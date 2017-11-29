from django.conf.urls import url

from . import views

urlpatterns = [
			url(r'^quotes$', views.quotes, name = 'quote_list'),
			url(r'^(?P<quote_id>[0-9]+)$', views.get_quote_by_id, name = 'quote_by_id'),
			url(r'^post_quotes$', views.post_quotes, name = 'post_quotes'),
]