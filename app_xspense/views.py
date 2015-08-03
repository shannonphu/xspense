from django.shortcuts import render

# Create your views here.
def all_expenses(request):
	return render(request, 'app_xspense/expenses.html', {})