from typing import List, Union

language_list: List[Union[str, List[int], List[str]]] = ["PHP","PYTHON","JAVA","C++",[10,20,50,100],['a','b','c']]
#this is example of insret function and add value in existing list
# print(f'Current List {language_list}')
# num = (input("Please enter a number Or Element to add to list:\n"))
# index = int(input(f'Please enter the index between 0 and {len(language_list) - 1} to add the number:\n'))
# language_list.insert(index,num)
# print(f'Update Numbers List {language_list}')
#this is example of insret function and add value in existing list

# this is example of find elemennt in existing list
# print(language_list[int(input(f'Please enter the index between 0 and {len(language_list) - 1} and Find Element from List:\n'))])
# print(language_list[int(input(f'Please enter the index between 0 and {len(language_list)} and Find Element from List:\n')):int(input(f'To index between 0 and {len(language_list)} and Find Element from List:\n'))])
# this is example of find elemennt in existing list

#this example is for check item is available in item
# chech_num = input(f'Plese entry value to check this value is True Or not:\n')
# # print(chech_num in language_list)
# if chech_num in language_list:
#     print("Value is Available in Item")
# else:
#     print("Value is Not Availble in Item")
#this example is for check item is available in item

#example for value change in list
# language_list[int(input(f'Please Entre index between 0 and {len(language_list)-1} and change Element From List:\n'))] = input(f'Please Enter Value and change value in List:\n')
# print(language_list)
#example for value change in list

#example for append value in list
car_list = ["bmw","audi",[1,2,3],['a','c']]
# num = (input("Pleae enter value to add in lits:\n"))
# car_list.append(num)
# print(f'New Updated List {car_list}')
#example for append value in list

#example for remove item in list
# num = (input("Please enter value to remove from list:\n"))
# car_list.remove(num)
# print(f'new update list {car_list}')
#example for remove item in list


#example for pop function
# num = int(input(f'please Enter the index between 0 to {len(car_list)-1} to remove element from list:\n'))
# car_list.pop(num)
# print(car_list)
#example for pop function

# this is an Example of Copy Function In List
# car_list = car_list.copy()
# print(car_list)
# this is an Example of Copy Function In List

#example of extend function
# new_list = []
# new_list.extend(['car','bike'])
# print(new_list)
# new_list.extend([1,2])
# print(new_list)
# new_list.extend(['True','False'])
# print(new_list)
#example of extend function

#concatination example
# add = [1,3,5]
# update = [2,4,6]
# new_add = update+add
# print(new_add)
#concatination example

#sorting function
def myFunc(e):
    return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'TATA', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)
#sorting function
