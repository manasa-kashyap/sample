class doctor:
    def do_surgery(self,x,y):
        print('x=',x)
        print('y=',y)
d=doctor()
d.do_surgery(20,60)

class developer:
    def __init__(self,number,name,designation):
        print('number=',number)
        print('name=',name)
        print('designation=',designation)
d=developer(21,'vinay','developer')

class patient:
    def __init__(self,name,disease,age):
        print('this is patient object')
        print('name=',name)
        print('disease=',disease)
        print('age=',age)
    def admitroom(self,room):
        print('patient is admitted in room',room)
p=patient('manasa','cough',21)
p.admitroom(101)

class student:
    def __init__(self,number,name,subject):
        print('number=',number)
        print('name=',name)
        print('subject=',subject)
    def details(self,number,name,subject):
        print(number,name,subject)
s=student(21,'vinay','maths')
s.details(13,'suresh','science')


class test:
    def __init__(self):
        print('hii')
t1=test()
t2=test()

class test:
    def __init__(self,m):
        self.x=m
t1=test(10)
t2=test(20)
print(t1.x)

class doctor:
    def __init__(self,no,name,spec):
        print('no=',no)
        print('name=',name)
        print('spec=',spec)
    def __int__(self,no,name,spec):
        print('no=',no)

        print('name=',name)
        print('spec=',spec)
d=doctor('1','sachin','pediatric')
d=doctor(2,'veena','ent')

class test:
    def __init__(self,x):
        print(x)
t=test(10)

global_variable=40
class test:
    class_variable=30
    def __init__(self,local_variable):
        self.instance_variable=20
        print(local_variable)
        print(self.instance_variable)
        print(test.class_variable)
        print(global_variable)
test_one=test(10)

class details:
    def display(self,name,age,loc):
        print("my name is=",name)
        print('my age is=',age)
        print("my loc is=",loc)
d=details()
d.display('manasa',21,'gbd')

class doctor:
    def __init__(self,no,name,spec):
        self.no=no
        self.name=name
        self.spec=spec
    def display(self):
        print(self.no)
        print(self.name)
        print(self.spec)
d=doctor(1,"veena",'hr')
d.display()
d1=doctor(2,'umesh','hr')
d1.display()
d2=doctor(3,'david','hr')
d2.display()

class Demo:
    x=20
    def __init__(self,loc):
        print('loc=',loc)
    def m1(self,name):
         print('name=',name)
d=Demo('Bangalore')
print(d.x)
d.m1('Manasa')










