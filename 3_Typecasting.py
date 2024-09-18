# Typecasting = The process of converting a variable from one data type to another
#           str(), int(), float(),bool()

name="L. Wayfaring"
age =25
gpa =3.2
is_student = True # T must be capital.
complex_num = 2+3j
print(type(name)) # string
print(type(age)) # int
print(type(gpa)) # float
print(type(is_student)) # boolean
print(type(complex_num)) # complex

gpa = int(gpa)
print(gpa) # 3
age= float(age)
print(age) #25.0
age=str(age)
print(age) #25 (this is string)
name=bool(name)
print(name) # True

name2=''
name2=bool(name2)
print(name2)
