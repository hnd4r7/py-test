"""
Note:  You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
    tuple can be used as keys
"""

tel = {'jack': 4098, 'sape': 4139}
print('guido' in tel)
print(list(tel))
print(sorted(tel))

lista = [('sape', 4139), ('guido', 4127), ('jack', 4098)]
lista.append(('fksdjf',333))

"""
convert list of tuples to dict 
"""
print(dict(lista))

print({x: x**2 for x in (2, 4, 6)})

d = dict(sape=4139, guido=4127, jack=4098)
print(d)