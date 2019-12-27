class checkregister:
    def __init__(self,name,lastname,username,password,mail,mobile,code):
        self.name=name
        self.lastname=lastname
        self.username=username
        self.passwoerd=password
        self.mail=mail
        self.mobile=mobile
        self.code=code
    def checkname(self):
        count1=0
        c = [i for ele in self.name for i in ele] #cleave characters of string and save in a list
        if 0<len(c)<22: #check length of name
            for i in c:
                if ord('a')<=ord(i)<=ord('z'): #count number of characters a-z
                    count1+=1
                if ord('A')<=ord(i)<=ord('Z'): #count number of characters A-z
                    count1+=1
                if ord(i)==32: #count number of space
                    count1+=1
            if count1==len(c): #check all of characters of name be true
                return 1
    def checklastname(self):
        count1=0
        c = [i for ele in self.lastname for i in ele]
        if 0<len(c)<31:
            for i in c:
                if ord('a')<=ord(i)<=ord('z'):
                    count1+=1
                if ord('A')<=ord(i)<=ord('Z'):
                    count1+=1
                if ord(i)==32:
                    count1+=1
            if count1==len(c):
                return 1
    def checkusername(self):
        count1=0
        if self.username!="username": #check username not be "username"
            if self.username!="admin": #check username not be "admin"
                c = [i for ele in self.username for i in ele]
                if 6<len(c)<51:
                    for i in c:
                        if ord('a')<=ord(i)<=ord('z'):
                            count1+=1
                        if ord('A')<=ord(i)<=ord('Z'):
                            count1+=1
                        if ord(i)==ord("@"):
                            count1+=1
                        if ord(i)==ord("_"):
                            count1+=1
                        if ord("0")<=ord(i)<=ord("9"):
                            count1+=1
                    if count1==len(c):
                        return 1
    def checkpassword(self):
        count1=0
        count2=0
        count3=0
        c = [i for ele in self.passwoerd for i in ele]
        if 8<len(c)<51:
            for i in c:
                if ord('a')<=ord(i)<=ord('z'):
                    count1+=1
                if ord('A')<=ord(i)<=ord('Z'):
                    count1+=1
                if ord(i)==ord("@"):
                    count3+=1
                if ord(i)==ord("_"):
                    count3+=1
                if ord(i)==ord("&"):
                    count3+=1
                if ord(i)==ord("#"):
                    count3+=1
                if ord(i)==ord("%"):
                    count3+=1
                if ord(i)==ord("$"):
                    count3+=1
                if ord("0")<=ord(i)<=ord("9"):
                    count2+=1
            if count1+count2+count3==len(c):
                if count1!=0: #check characters be in password
                    if count2!=0: #check numbers be in password
                        if count3!=0: #check symbols be in password
                            return 1
    def checkmail(self):
        count1=0
        count2=0
        count3=0
        c = [i for ele in self.mail for i in ele]
        for i in c:
            if ord(i)==ord("@"):
                count2+=1
            if ord(i)==ord("."):
                count3+=1
            if ord("0")<=ord(i)<=ord("9"):
                count1+=1
            if ord("a")<=ord(i)<=ord("z"):
                count1+=1
            if ord("A")<=ord(i)<=ord("Z"):
                count1+=1
            for i in range(len(c)):
                if c[i]=="@": #found place of @
                    a=i
                elif c[i]==".": #found place of .
                    b=i
        if count1+count2+count3==len(c):
            if count2!=0: #check @ must be in string
                if count3!=0: #check . must be in string
                    if a!=0: #check be character before @
                        if b!=i: #check be character after .
                            if b>a+1: #check be chahracter after @ and before . and @ be before .
                                return 1
    def checkmobile(self):
        count1=0
        c = [i for ele in self.mobile for i in ele]
        if len(c)==11: #check length of number
            for i in c:
                if ord('0')<=ord(i)<=ord('9'):
                    count1+=1
            if count1==len(c):
                if c[0]=="0": #check be 0 first of number
                    return 1
    def checkcode(self):
        count1 = 0
        count = 10
        sum = 0
        c = [i for ele in self.code for i in ele]
        if len(c) == 10:
            for i in c:
                if ord("0") <= ord(i) <= ord("9"):
                    count1 += 1
            for i in range(9): #calculate sum of place*number
                a = count * int(c[i])
                sum += a
                count -= 1
            b = sum % 11
            if count1 == 10:
                if b < 2:
                    if b == int(c[9]):
                        return 1
                if b >= 2:
                    if 11 - b == int(c[9]):
                        return 1
    def check(self):
        if self.checkname() == 1:
            if self.checklastname() == 1:
                if self.checkusername() == 1:
                    if self.checkpassword() == 1:
                        if self.checkmail() == 1:
                            if self.checkmobile() == 1:
                                if self.checkcode() == 1:
                                    return 1
name=input("Enter name:")
lastname=input("Enter lastname:")
username=input("username:")
password=input("enter password:")
email=input("Enter email:")
mobile=input("Enter mobile:")
code=input("Enter code:")
p1=checkregister(name,lastname,username,password,email,mobile,code)
if p1.check()==1:
    print("register ok")
else:
    print("register error")
