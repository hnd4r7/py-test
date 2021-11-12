"""
Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
"""
empty = set()

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

a = set('abracadabra')
print(a)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)