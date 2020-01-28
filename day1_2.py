# #STRINGS
# # s = 'John'

# # print(dir(s))   #shows the different methods/functions to work with strings
# # s = s.upper()   #To capitalize all the single letters  #you must always open and close parenthesis in python
# # print(s)

# # help(s.title)  #puts the first letter of the word in capital, titlecased
# # s = s.title()
# # print(s)

# # i = 10
# # print(dir(i))  #shows the different methods/functions to work with numbers

# # #l = [1,2,3,4,5]
# # help(l.append)

# # l.append(6)  #the function append adds a specified number to the end of the list
# # print(l)

# # #l.insert(0, 100)  #insert a particular object at a particular position)
# # print(l)

# l = [3,4,5,6,7,8]
# l.pop() # removes the bject at a specified index
# print(l)

# l.sort(reverse=True)  #arranges the objects in the list in reverse
# print(l)

# l.clear()  #deletes all the objects  but keeps the list
# print(l)

# #create a dictionary of countries and capital
# d = {'Nigeria' : 'Abuja', 'Italy': 'Rome', 'Kenya': 'Nairobi'}
# print(d)
# print(dir(d))

# help(d.keys)
# print(d.keys())  #prints the keys of the dictionary

# print(help(d.items)) #prints the items which is a big tuple that contains tuples of keys and corresponding values from the dictionary
# print(d.items())



#Loops
#mutable object means it is made of smaller objects
# #loops are defined as 'for something in list name'
# l = [1,2,3,4,5,6,7,8,9,10]
# for i in l:  #i can be any letter
#      print(i) #all objects in the list will be printed
#      print(i + 10)
# print(i)

# l1 = [10, 20, 30, 40]
# l2 = ['A', 'B', 'C', 'D']
# lt =[l1, l2]


#for loop
# # for i in lt:
# #     print(i)  #l1 is the first object in the list while l2 is the second object


# for i in lt:
#     for j in i:
#         print(j) #nested loop. started with the first elememt of lt then it goes into the second list and so on


# #while loop
# val = 0
# while val <= 20:  #while runs your instruction until your logic is correct
#     print(val)
#     val = val + 2 #this is necessary else it will run forever since it will continue to be less than 20

# d = {'names' : ['John', 'Maria', 'Anna'], 'age': [21, 25, 13]}
# for k in d.keys():  #looping into the keys in the dictionary
#     print(k)

# for s in d.values():
#     print (s)

# for c in d.items():
#     print(c)
# for s, c in d.items():
#     print(s,c)



# #if_statements
# l1 = [10, 20, 30, 40, 50, 60,]

# if len(l1) < 5:
#     print('I am a long list')
# elif len(l1) == 6:
#     print ('I am 6 items long')
# else:
#     print('I am inside the else')


d = {'names' : ['John', 'Maria', 'Anna'], 'age': [21, 25, 13]}
for k, v in d.items():
    if k == 'names':
        for i in v:
            print (i)
    else:
        print('i dont know')


# #Try and except statements: This is to exempt errors
# i = 10
# o = 0
# try:
#     result = i/ o
# except ZeroDivisionError:
#     print('I cannot divide by zero')

# l1 =[1,2,3]



#if you raise an exception, you are forcing python to stop the code from running at this point







