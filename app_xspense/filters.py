from django import template

register = template.Library()

@register.filter(name='categoryString')
def categoryString(value):
	return 'one'
	# return {
	# 	0: 'zer',
 #        1: 'one',
 #        2: 'two',
 #        3: 'th',
 #        4: 'fd',
 #        5: 'sf',
 #        6: 'six',
 #        7: 'sev',
 #        8: 'ocho',
 #        9: 'nue',
 #        10: 'die',
 #        11: 'once',
 #        12: 'doce',
 #        13: 'other'
 #    }.get(value, 13)