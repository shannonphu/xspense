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
        5: 'BABY & KIDS',
        6: 'TOYS & GAMES',
        7: 'FOOD',
        8: 'HEALTH',
        9: 'BEAUTY',
        10: 'FITNESS',
        11: 'AUTO',
        12: 'GIFTS',
        13: 'OTHER',
        14: 'EDUCATION'
    }.get(value, 13)

@register.filter(name='sumExpenses')
def sumExpenses(expenses):
	total = 0;
	for expense in expenses:
		total = total + expense.price
	return total

@register.filter(name='icon')
def icon(category):
    icon = {
        0: 'headphones',
        1: 'paperclip',
        2: 'facetime-video',
        3: 'home',
        4: 'sunglasses',
        5: 'ice-lolly-tasted',
        6: 'bishop',
        7: 'cutlery',
        8: 'plus-sign',
        9: 'eye-open',
        10: 'scale',
        11: 'dashboard',
        12: 'gift',
        13: 'option-horizontal',
        14: 'education'
    }.get(category, 13)
    return '<span class="glyphicon glyphicon-' + icon + ' small-12 medium-1 columns" aria-hidden="true"></span>'

@register.filter(name="progress")
def progress(budget):
    totalExpense = sumExpenses(budget.expense_set.all())
    percentage = int((totalExpense / budget.amount) * 100)
    if percentage >= 100:
        return '<div class="progress-bar progress-bar-warning progress-bar-striped" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width:100%; min-width: 2em">100%</div>'
    else:
        percentage = str(percentage)
        return '<div class="progress-bar progress-bar-warning progress-bar-striped" role="progressbar" aria-valuenow="' + percentage + '" aria-valuemin="0" aria-valuemax="100" style="width: ' + percentage + '%; min-width: 2em">' + percentage + '%</div>'





