from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Budget(models.Model):
	ELECTRONICS = 0
	OFFICE = 1
	ENTERTAINMENT = 2
	HOME_FURNITURE = 3
	CLOTHES = 4
	BABY_KIDS = 5
	TOYS_GAMES_CRAFTS = 6
	FOOD = 7
	HEALTH = 8
	BEAUTY = 9
	SPORTS_FITNESS = 10
	AUTO = 11
	GIFTS = 12
	OTHER = 13
	category_choices = [
		(ELECTRONICS, 'electronics'),
		(OFFICE, 'office'),
		(ENTERTAINMENT, 'entertainment'),
		(HOME_FURNITURE, 'home/furniture'),
		(CLOTHES, 'clothes'),
		(BABY_KIDS, 'baby/kids'),
		(TOYS_GAMES_CRAFTS, 'toys/games/crafts'),
		(FOOD, 'food'),
		(HEALTH, 'health'),
		(BEAUTY, 'beauty'),
		(SPORTS_FITNESS, 'sports/fitness'),
		(AUTO, 'auto'),
		(GIFTS, 'gifts'),
		(OTHER, 'other')
		]
	category = models.IntegerField(choices=category_choices, default=13)
	user = models.ForeignKey('auth.User', null=True)
	purpose = models.TextField()
	amount = models.DecimalField(max_digits=9, decimal_places=2)
	date_created = models.DateTimeField(
		default=timezone.now)

	def publish(self):
		self.date_created = timezone.now()
		self.save()

	def __str__(self):
		return "%s budget of amount $%f" % (self.category_choices[self.category][1], self.amount)



class Expense(models.Model):
	user = models.ForeignKey('auth.User', null=True)
	budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True)
	item = models.TextField()
	price = models.DecimalField(max_digits=9, decimal_places=2)
	date = models.DateTimeField(
		default=timezone.now)
	location = models.TextField()

	def publish(self):
		self.date = timezone.now()
		self.save()

	def __str__(self):
		return "%s bought at %s" % (self.item, self.location)



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
