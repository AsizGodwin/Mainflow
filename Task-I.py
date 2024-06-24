list=[1,2,4,5]
list.append(6)
print('List after updating:',list)
list.insert(2,3)
print('List after updating:',list)
list.pop(4)
print('List after updating:',list)
list.clear()
print('List after updating:',list)

print("\n")

dict={'A':"Audi",'B':"Benz",'C':"Corvette"}
dict.update(D="Dodge")
print('Dictionary after updating:',dict)
dict.pop('A')
print('Dictionary after updating:',dict)
dict.get('C')
print('Dictionary after updating:',dict)
dict.clear()
print('Dictionary after updating:',dict)

print("\n")

set={'list','array','dictionary','tuple'}
set.add('values')
print('Set after updating:',set)
set.discard('array')
print('Set after updating:',set)
set.remove('tuple')
print('Set after updating:',set)
set.clear()
print('Set after updating:',set)
