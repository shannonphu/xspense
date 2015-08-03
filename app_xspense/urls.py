from django.conf.urls import url
from . import views

urlpatterns = [
	# root webpage route '/'
	url(r'^expenses$', views.all_expenses, name='all_expenses'),
	url(r'^budgets$', views.all_budgets, name='budgets')
	#url(r'^new/budget$', views.new_budget, name='new_budget')
]