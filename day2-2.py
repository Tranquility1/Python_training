#classes: similar to fuctions
# class Test:
#     pass 
# x = Test() # x and y are instances
# y = Test()

# print(x)
# print(y)

# class Test:
#     name = 'I am the class'
#     Variable =  10

# x = Test()
# y = Test()


# class Test:
#     name = 'I am the class'
#     variable = 10
#     def printName(self):
        #print('I am a method of the class')



# class Test2:
#     def __init__(self, name):
#         self.name = name
#         print('I am the init function')

# y = Test2('y')


# class Dog:
#     scientific_name = 'Canis'  #The class attribute will be the same for each dog

#     def __init__(self, name):
#         self.name = name

# duke = Dog ('duke')
# bob = Dog('bob')

# print(duke.scientific_name)
# print(duke.name)

# print(bob.scientific_name)
# print(bob.name)


# class Hero:
#     def __init__(self, name):
#         self.name = name
#         self.energy = 100
    
#     def eating(self, food):
#         if food == 'pasta': 
#             self.energy = self.energy + 10
#         elif food == 'pizza':
#             self.energy = self.energy - 20

# mario = Hero('Mario')
# print(mario.name)
# print(mario.energy)
# mario.eating('pasta')
# print(mario.energy)
# mario.eating('pizza')
# print(mario.energy)
#adissu = Hero('Adissu')

#print(mario.name)
#print(mario.energy)


# class BaseClass:   #uclear section

#     def printname(self):
#         print('I come from the base class')

# class subClass(BaseClass):
#     pass

# a = SubClass()
# a.printName()



class Employee:    #PRACTICE@home
    def __init__(self, name, paycheck):
        self.name = name
        self.paycheck = paycheck
    def raise_paycheck(self, number):
        self.paycheck = self.paycheck + (self.paycheck * number)

mario = Employee('Mario', 1000)
print(mario.name)
print(mario.paycheck)

mario.raise_paycheck(0.1)
print(mario.paycheck)








