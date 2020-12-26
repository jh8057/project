class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sayhello(self,to_name): 
        print("hello,"+to_name+" i am " + self.name)
    def sayage(self):
        print("i am "+self.age)

class person(animal):
    def saylanguage(self,language):
        print("i m "+self.name+" i can speak "+language)



zzaemal = animal("zze","25")

zzaemal.sayhello("UZ")

zzaemal.sayage()


BB = person("BB","27")
BB.saylanguage("ko")