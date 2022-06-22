#prog_my_dist = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm','Sublime'], 'Java':{'JSE':'Netbeans','JEE':'Eclipse','Colors':{1:'red', 2:'blue', 3:{'Food':'Fast Food','Tea':'Number of Tea', 'Time':{9:'Nine', 10:'Ten','c':(11, 22, 33)}}}, 'number':[1, 2, 3, 4, {1:'jan', 2:'feb', 3:'march'}]}, 'a':{'1':'one', '2':'two'},'b':[1, 2, 3, 4, 5], 'c':(1, 2, 3)}
# print(prog_my_dist)

#example for update dictionaries
# prog_my_dist['city'] = "Rajkot"
# prog_my_dist.update({"city":"Rajkot"})
# print(prog_my_dist)

# update_dic = prog_my_dist.get('Java').get('Colors')
# d1 = update_dic
# d1 = {3:"green",4:"yellow"}
# d1.update(d1)
# print(d1)


# update_number = prog_my_dist.get('Java').get('number')[4]
# number = update_number
# numbers = {4: "april",5: "may",6: "jun",7: "july"}
# number.update(numbers)
# print(number)
#example for update dictionaries

#example for update dictionary value with list using append & insert
# update_new = prog_my_dist.get('b')
# update_new.append(65)
# update_new.insert(1,20)
# update_new.insert(7,50)
# print(update_new)
#example for update dictionary value with list using append & insert

# print(prog_my_dist.get('Java').get('Colors').get(3))
# print(prog_my_dist.get('Java').get('number')[4][1])
# print(prog_my_dist.get('Python')[1])
# print(prog_my_dist.get('b')[0])

#example of items function
marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }
print(marks.items())
#example of items function

#example of keys function
print(marks.keys())
#example of keys function

#example of pop function
print(marks.pop('Physics'))
#example of pop function


#example of popitem function return last in first out
print(marks.popitem())
#example of popitem function

#example of setdefault function
print(marks.setdefault('Biology',50))
#example of setdefault function


#example of value function
print(marks.values())
#example of value function
