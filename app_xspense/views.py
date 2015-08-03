from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import BudgetForm
from .forms import ExpenseForm
from django.shortcuts import redirect
from .models import Expense
from .models import Budget

# Create your views here.
def all_expenses(request):
	expenses = Expense.objects.filter(date__lte=timezone.now())
	return render(request, 'app_xspense/expenses.html', {'expenses': expenses})

def overview(request):
	budgets = Budget.objects.filter(category__gte=0)
	return render(request, 'app_xspense/overview.html', {'budgets': budgets})

def all_budgets(request):
	budgets = Budget.objects.filter(category__gte=0)
	return render(request, 'app_xspense/budgets.html', {'budgets': budgets})

def new_budget(request):
	form = BudgetForm()
	return render(request, 'app_xspense/new_budget.html', {'form': form})

def new_expense(request):
	form = ExpenseForm()
	return render(request, 'app_xspense/new_expense.html', {'form': form})