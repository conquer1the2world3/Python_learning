from typing import Any

# 父类
class Person:
    "这是一个Person类"
    count = 0
    __private_var = "私有变量"
    _protected_var = "受保护的变量"
    public_var = "公共变量"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1
        self.__private_method()
        print("调用父类构造方法")

    def __private_method(self):
        print("在类内部调用私有方法")

    def getattr(self):
        print("获取父类属性")
        print(self.__private_var)
        print(self._protected_var)
        print(self.public_var)
    
    def setattr(self,name,age):
        self.name = name
        self.age = age
        print("设置父类属性")

    def __del__(self):
        Person.count -= 1 

    def __str__(self):
        return "姓名：%s,年龄：%d"%(self.name,self.age)

    def __prt__(self):
        print("调用父类方法")
        print(self.__class__)

# 子类
class IT(Person):
    def __init__(self,name,age,language):
        Person.__init__(self,name,age)
        self.language = language
        print("调用子类构造方法")
        print("子类访问父类受保护的变量",self._protected_var)

    def say(self):
        print("调用子类方法：",self)

    def __str__(self):
        return "姓名：%s,年龄：%d,语言：%s"%(self.name,self.age,self.language)

    def __del__(self):
        print("调用子类析构方法：")

p1 = Person("张三",20)
print(p1.__str__())
p1.__prt__()
p1.sex = "男"
print("性别：",p1.sex)
del p1.sex
print("对象名._类名__私有属性名访问私有属性",p1._Person__private_var)


##getter 和 setter
getattr(p1,"name")
setattr(p1,"name","李四")
print(p1.name)
delattr(p1,"name")

p2 = Person("李四",21)
print("当前员工个数：",Person.count)
p2.__del__()
print("当前员工个数：",Person.count)

Person.count = 10
print("当前员工个数：",Person.count)

print("Person.__doc__:",Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)
print(Person.__dict__)
        
zfsjlll = IT("张三",20,"Python")
zfsjlll.getattr()
zfsjlll.setattr("李四",21)
zfsjlll.say()

# 私有变量和方法不能在类外部访问和继承
# print(zfsjlll.__private_var)
# zfsjlll.__private_method()

# 多继承
class Xiaoyao(IT,Person):
    def __init__(self,name,age,language,sex):
        IT.__init__(self,name,age,language)
        Person.__init__(self,name,age)
        self.sex = sex

    def __str__(self):
        return "姓名：%s,年龄：%d,语言：%s,性别：%s"%(self.name,self.age,self.language,self.sex)

print(issubclass(IT,Person))
print(issubclass(Person,IT))
print(issubclass(Xiaoyao,IT))
print(issubclass(Xiaoyao,Person))

print(isinstance(zfsjlll,Person))
print(isinstance(zfsjlll,IT))
print(isinstance(zfsjlll,Xiaoyao))


