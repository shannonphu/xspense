from django import template

register = template.Library()

@register.filter(name='categoryString')
def categoryString(value):
	return {
		0: 'ELECTRONICS',
        1: 'OFFICE',
        2: 'ENTERTAINMENT',
        3: 'HOME FURNITURE',
        4: 'CLOTHES',
        5: 'BABY/KIDS',
        6: 'TOYS/GAMES/CRAFTS',
        7: 'FOOD',
        8: 'HEALTH',
        9: 'BEAUTY',
        10: 'SPORTS/FITNESS',
        11: 'AUTO',
        12: 'GIFTS',
        13: 'OTHER'
    }.get(value, 13)

@register.filter(name='sumExpenses')
def sumExpenses(expenses):
	total = 0;
	for expense in expenses:
		total = total + expense.price
	return total