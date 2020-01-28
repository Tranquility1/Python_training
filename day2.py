# #Range
# r = range(0, 100, 2)
# print(r)

# l = list(r) #convert range to list
# print(l)

# a = range(1, 51)
# b = range(1, 21)

# d = {'a': [a], 'b': [b]}
# print(d)

# if d.keys == 'a':
#     print(d.values > 25)
# elif d.values > 25:
#     print('no values')


ra = list (range(1,50))
rb = list(range(1,20))
d = {'a' : ra, 'b' : rb}
#print(d)

# for k, v in d.items(): #k is key, v is value
#     if k == 'a':
#         for i in v:
#             if i > 25:
#                 print(i)
#             else:
#                 print('no values')

#     if k == 'b':
#         for i in v:
#             if i < 10:
#                 print(i)

# #To create an empty list and fill it up with values from a dictionary
# print(d['a'])
# l = []  #define an empty list
# for i in d['a']:
#     if i > 25:
#         l.append(i)  #then fill it up
# print(l)


#Now we are moving to functions
# def my_function():  #You can describe your function imbetween three single quotes to help you remember what it does and maybe the parameters
#     '''
#     This function prints something
#     This function does not need parameters
#     '''
#     print('hi python')
# my_function()  #calling the function
# #print(help(my_function))

# def my_function2(s):
#     print(s)
# my_function2('Sakinat')

# def my_function3(name='Sakinat', age=22):  #a function is like a template, you can change the content later when calling the fuction
#     print(name, age)
# #my_function3('Sakinat, 22')
# my_function3(age=29) 

#def multiply(x,y):
   # result = x * y
    #print(result)

#multiply (10, 35)
#l = [10,2,3,50]
#multiply(l[0], l[2])

# def multiply2(*args):  #arg is considered a list
#     v = 1
#     for i in args:  # this looping allows you to multiply as many numbers in a list as you want
#         v = v * i
#     #print(v)
#     return v
# my_number = multiply2(1,30,90,4,3)
# print(my_number)

#classwork: area of rectangle
# def rect_area(height, width):
#     result = height * width
#     print(result)
# my_area = rect_area(8,5)
# print(my_area)

# def shape_area(shape, width, height):
#     if shape == 'rectangle':
#         calculation = width * height
#         return calculation
#     if shape == 'triangle':
#         calculation = width * height / 2
#         return calculation
#     else:
#         print('I do not know the shape')

# area = shape_area('rectangle', 100, 5)
# print(area)


# def temp_conv(celsius):
#     fahrenheit = (celsius*9/5)+32
#     print(fahrenheit)
# my_temp = temp_conv(0)
# print(my_temp)



#to convert a list of numbersin celcius to fahrenheit
def fahrenheit2(*args):
    lf =[]
    for c in args:

        calculation = (c * 9/5) + 32
        lf.append(calculation)
    return lf
ic = [10, 0, 100,50]
my_f = fahrenheit2(10, 0, 100, 33)
print(my_f)
my_f2 = fahrenheit2(*ic)
print(my_f2)
















