#this is my comment

#integers
i = 3
print (i)

#using a function
ii = int(1.2)
print(ii)

#floating
f = 1.4
print (f)

result = i - f
print(result)

#strings
s = 'my string'
ss = "my other string"
print(s, ss) #yes, I can comment after the code

i = int(10)
print(i)
k = 'backlash \\'
print (k)

g = 'Bob\'s cat'
print(g)

g = "Tee's bag"
print(g)
f = '''my string ' " '''
print(f)


name = 'Sakinat'
complete_name = 'My name is %s' % name
print(complete_name)


complete_name = 'My name is {}'.format(name)
print(complete_name)

complete_name = f'My name is {name}'


name = 'Sakinat'
surname ='Ahmad'
age = 27 
Complete_info = f'''My complete name is {name} {surname} and I'm {age}years old'''
print(Complete_info)

#Boolean
mybool = True
mybool2 = False
print(mybool, mybool2)

i = 1
print(str(i))  #the number 1 has been converted to a string
#A string cannot be convertd to a number

s = i
conv = int(s)  #useful when files are imported into python and it doesn't recognize them. Convert the numbers to integer

s = 't'
print(bool(s))

a = 'a'
print(bool(a))

i = 10
ii = 3
print(i/ii)
print(i%ii) #prints the remainder of 10 divided by 3



#BASIC OBJECTS
#lists
l = [1, 2, 3, 4, 5]
print(type(l))
print(l)

ii = [1, 'A', 1.3, True]  #all data types can be put in a list in python
print(ii)

print(i == ii) #double equal sign is used because single means attributing a value
print(i != ii) #!= is asking if the objects are different

l1 = [1,2,2,2,2,3,1,1,1,2,2,2,3,3,3,3,3,3]
print(l1)

s1 = set(l1)
print(s1)

#print(type(s1))  #to check the data type of s1

print(l1[0])  #printing the first number in the l1 list

print(l1[-1])  #printing the last number of a list

print(l1[0:3]) #printing the first 3 numbers in the list

print(len(l1)) #printing the length of the list, i.e the number of numbers in that list

l = [1,2,3,4,5,6,7,8,9,10]
print(l[:-2])

l1 = [1,2,3]
l2 = [4,5,6]
lt = l1 + l2 #concatenates
print(lt)

ltt = l1 * 4  #replicates the list in the specified number of time

print(ltt)

lm = [l1, l2]
print(lm)

print(lm[0]) #It will show the first list

del lm[0]
print(lm)

t = (1,2,3)
print(t)
print(type(t))

#t[0] = 1000  #tuple object does not support object assignment



#Dictionaries
d = {'name':'Sakinat'}
print(d)

d = {'name':'Sakinat', 'age': 'Sakinat'}
print(d)

d = {'names':['Joe', 'Matteo', 'John']}
print(d['names'][0])



