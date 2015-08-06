from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .forms import BudgetForm, ExpenseForm, UserForm, UserProfileForm
from .models import Expense, Budget

# show all budgets/expenses
@login_required
def all_expenses(request):
	expenses = Expense.objects.filter(user=request.user).order_by('-date')
	return render(request, 'app_xspense/expenses.html', {'expenses': expenses})

def overview(request):
	budgets = Budget.objects.filter(user=request.user.id)
	return render(request, 'app_xspense/overview.html', {'budgets': budgets})

@login_required
def all_budgets(request):
	budgets = Budget.objects.filter(user=request.user).order_by('category').order_by('-date_created')
	return render(request, 'app_xspense/budgets.html', {'budgets': budgets})

# Load forms

@login_required
def new_budget(request):
	if request.method == "POST":
		form = BudgetForm(request.POST)
		if form.is_valid():
			budget = form.save(commit=False)
			budget.user = request.user
			budget.publish()
			messages.success(request, 'Budget successfully recorded.')
			return redirect('app_xspense.views.overview')
	else:
		form = BudgetForm()
	return render(request, 'app_xspense/new_budget.html', {'form': form})

@login_required
def new_expense(request):
	if request.method == "POST":
		form = ExpenseForm(request.user, data=request.POST)
		if form.is_valid():
			expense = form.save(commit=False)
			expense.user = request.user
			expense.publish()
			messages.success(request, 'Expense successfully recorded.')
			return redirect('app_xspense.views.overview')
	else:
		form = ExpenseForm(request.user)
	return render(request, 'app_xspense/new_expense.html', {'form': form})



## USER AUTHENIFICATION SYSTEM ##
def register(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			# Now we save the UserProfile model instance.
			profile.save()

			# Update our variable to tell the template registration was successful.
			registered = True
			messages.success(request, 'Successfully registered. Login to continue.')
			return HttpResponseRedirect('login')

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print (user_form.errors, profile_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render(request,
			'app_xspense/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				messages.success(request, 'Successfully logged in.')
				return HttpResponseRedirect('/')
			else:
				# An inactive account was used - no logging in!
				messages.error(request, 'Your account is disabled.')
				return HttpResponseRedirect('login')
		else:
			# Bad login details were provided. So we can't log the user in.
			# print "Invalid login details: {0}, {1}".format(username, password)
			messages.error(request, 'Invalid login details supplied.')
			return HttpResponseRedirect('login')

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render(request, 'app_xspense/overview.html', {})


# logout
@login_required
def user_logout(request):
	logout(request)
	messages.success(request, 'Successfully logged out.')
	return HttpResponseRedirect('/')




