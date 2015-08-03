from django.conf.urls import url
from . import views

urlpatterns = [
	# root webpage route '/'
	url(r'^$', views.overview, name='overview'),
	# view list of expenses or budgets separately
	url(r'^expenses$', views.all_expenses, name='all_expenses'),
	url(r'^budgets$', views.all_budgets, name='all_budgets'),
	# create new budget/expense
	url(r'^new/budget$', views.new_budget, name='new_budget'),
	url(r'^new/expense$', views.new_expense, name='new_expense'),
	url(r'^register$', views.register, name="register"),
	url(r'^login$', views.user_login, name="login"),
	url(r'^logout$', views.user_logout, name='logout'),
]