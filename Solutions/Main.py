from 20290122(2).py import *

obj1 = ListClass([1,2,3,4,5,6], 'list1')
obj1.printName()
print('Elements:', obj1)
print('Length:', obj1.getLength())

print('Odd elements:', end=" ")
obj1.printOdds()

print('Even elements:', end=" ")
obj1.printEvens()

obj1.changeItem(2,7) # Item 2 will be changed with 7
print(obj1)

obj1.addItem(8)
obj1.addItems([1,2,3,9,10])  # 1 and 3 will be omitted (since they already exists), and the rest will be inserted
print(obj1)

obj1.removeItem(4)
print(obj1)

obj1.removeItems([1,2,3,4,11]) # Since 4 and 11 do not exist in the list, they will be omitted. The rest will be removed
print(obj1)

obj2 = ListClass([5,10,7,8,2], 'list2')
obj2.printName()
print('Elements:', obj2)
if obj1 < obj2:
	print('The sum of list1 items is less than sum of list2 items.')
else:
	print('The sum of list1 items is greater than or equal to sum of list2 items.')

