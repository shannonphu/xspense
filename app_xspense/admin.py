from django.contrib import admin
from .models import Budget
from .models import Expense
from .models import UserProfile

admin.site.register(Budget)
admin.site.register(Expense)
admin.site.register(UserProfile)