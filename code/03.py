#!/usr/bin/python

# https://www.runoob.com/python/python-basic-syntax.html

input("Press Enter to exit...")


if False:
    print("Hello, World!")
else:
    print("Hello, Universe!")
    print("Hello, Galaxy!")
    
print('-' * 20)

item_1 = 'item_1'
item_2 = "item_2"
item_3 = '''item_3
3'''
item_4 = """item_4
4"""

item_fin = item_1 + \
    item_2 + \
    item_3 + \
    item_4

print(item_fin)
print('-' * 20)
print(item_1, item_2, item_3, item_4)
print('-' * 20)
print(item_1, item_2, item_3, item_4, sep=", ")
print('-' * 20)
print(item_1, item_2, item_3, item_4, sep=", ", end=".\n")
print('-' * 20)

'''
多行注释
'''

"""
另一种多行注释
"""
