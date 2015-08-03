from django.shortcuts import render
from django.utils import timezone
from .models import Expense
from .models import Budget

# Create your views here.
def all_expenses(request):
	expenses = Expense.objects.filter(date__lte=timezone.now())
	return render(request, 'app_xspense/expenses.html', {'expenses': expenses})

def all_budgets(request):
	budgets = Budget.objects.filter(category__gte=0)
	return render(request, 'app_xspense/budgets.html', {'budgets': budgets})