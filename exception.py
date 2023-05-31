

## Try with one except and else block

print('start')
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
try:
    print('Try is started')
    res=a/b
    print('Try is ended')
except ZeroDivisionError:
    print('I have handled the error')
else:
    print(res)
print('end')






## Single Try with Multiple Except Block

print('start')
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
try:
    print('Try is started')
    res=a/b
    print(x)
    print('Try is ended')
except ZeroDivisionError as e:
    print(e)
except NameError as n:
    print(n)
else:
    print(res)
print('end')







## Default Exception Block

print('start')
a=int(input("Enter a number: "))
b=input("Enter a number: ")
try:
    print('Try is started')
    res=a/b
    print(x)
    print('Try is ended')
except ZeroDivisionError as e:
    print(e)
except NameError as n:
    print(n)
except:
    print('Unknown error is handled')
else:
    print(res)
print('end')






## Generic Exception Class

print('start')
a=eval(input("Enter a value: "))
b=eval(input("Enter a value: "))
try:
    print("Try is started")
    res=a/b
    print(res)
    print(x)
    print('Try is ended')
except Exception as e:
    print(e)





## Finally Block

print('start')
try:
    print('Try is started')
    fo=open('finally.txt','w')
    data=eval(input("Enter Data: "))
    fo.write(data)
    print('Try is ended')
except Exception as e:
    print(e)
finally:
    print('I am inside finally')
    fo.close()
print('end')
print(fo.closed)





##-----------------------------------------------------------






#* Example:-1
## No handler

def current():
    print("Current function Started")
    print(a)
    print("Current function Ended")

def caller():
    print("caller function Started")
    current()
    print("caller function Ended")

print("Main start")
caller()
print("Main Ends")





## Handler in current function

def current():
    print("Current function Started")
    try:
        print(a)
    except Exception as e:
        print(e)
    print("Current function Ended")

def caller():
    print("caller function Started")
    current()
    print("caller function Ended")

print("Main start")
caller()
print("Main Ends")





## Handler in caller function

def current():
    print("Current function Started")
    print(a)
    print("Current function Ended")

def caller():
    print("caller function Started")
    try:
        current()
    except Exception as e:
        print(e)
    print("caller function Ended")

print("Main start")
caller()
print("Main Ends")






## Handler in main space// place where we have called the function

def current():
    print("Current function Started")
    print(a)
    print("Current function Ended")

def caller():
    print("caller function Started")
    current()
    print("caller function Ended")

print("Main start")
try:
    caller()
except Exception as e:
    print(e)
print("Main Ends")





#* Example:-2
## No Handler

def f1():
    print('f1 is started')
    a=10/0
    print('f1 is ended')

def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')

print('main starts')
f2()
print('main ends')





## Handler in current function

def f1():
    print('f1 is started')
    try:
        a=10/0
    except Exception as e:
        print(e)
    print('f1 is ended')

def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')

print('main starts')
f2()
print('main ends')




## Handler in caller function

def f1():
    print('f1 is started')
    a=10/0
    print('f1 is ended')

def f2():
    print('f2 is started')
    try:
        f1()
    except Exception as e:
        print(e)
    print('f2 is ended')

print('main starts')
f2()
print('main ends')




## Handler in main space// place where we have called the function

def f1():
    print('f1 is started')
    a=10/0
    print('f1 is ended')

def f2():
    print('f2 is started')
    f1()
    print('f2 is ended')

print('main starts')
try:
    f2()
except Exception as e:
    print(e)
print('main ends')






##-----------------------------------------------------------------------------------------------



## Raise
## Built-in raise error

print('start')
try:
    print('first limeof try')
    l=[11,22,334,67]
    ip=int(input("Enter The ip: "))
    if ip>len(l):
        raise IndexError("Index outof range")
    print('Last line of try')
except Exception as e:
    print(e)
else:
    print(l[ip])
print('end')






## User-defined raise error

class DemoError(BaseException):
    def __init__(self,msg):
        self.msg = msg

print('start')
try:
    print('first line of try')
    raise DemoError('This is our first USD Error')
    print('last line of try')
except DemoError as e:
    print(e)





## Nested Try and Except block

print('start')
try:
    print('First line of outer try')
    l=[11,22,33,44]
    ip=int(input("Enter The ip: "))
    print(l[ip])
    try:
        print("Inner try is started")
        x=int(input("Enter x: "))
        y=int(input("Enter y: "))
        res=x/y
        print("Inner try is ended")
    except Exception as e:
        print(e)
    else:
        print(res)
    print('last line of try')
except Exception as e:
    print(e)
print('end')



##-----------------------------------------------------------------------------------------

#*PROGRAMS
## Validation of credential login
## 1st type---->try block in current method

class Bank:
    bank_name='SBI'
    bank_branch='Marathali'
    bank_roi=7

    def __init__(self,name,age,acc,bal,pin):
        self.name=name
        self.age=age
        self.account=acc
        self.balance=bal
        self.pin=pin

    def withdraw(self):    
        amount=int(input("Enter The Amount: "))
        try:
            if self.balance>=amount:
                self.balance-=amount
                print("Withdraw Successful")
            else:
                raise Insufficient_balance_Error('Insufficient Balance')
        except Insufficient_balance_Error as e:
            print(e)
                        
tus=Bank('Tushar',25,36209,10000,9090)


class Credentional_Error(BaseException):
    def __init__(self,msg):
        self.msg=msg
    
class Insufficient_balance_Error(BaseException):
    def __init__(self,msg):
        self.msg=msg

try:
    a=input("Enter Username: ")
    if tus.name==a:
        pin=int(input("Enter The Pin: "))
        if tus.pin==pin:
            tus.withdraw()
        else:
            raise Credentional_Error('Incorrect Pin')
    else:
        raise Credentional_Error('Incorrect Username')
except Credentional_Error as e:
    print(e)






## 2nd type----> try block in caller method

class Bank:
    bank_name='SBI'
    bank_branch='Marathali'
    bank_roi=7

    def __init__(self,name,age,acc,bal,pin):
        self.name=name
        self.age=age
        self.account=acc
        self.balance=bal
        self.pin=pin

    def withdraw(self):    
        amount=int(input("Enter The Amount: "))
        if self.balance>=amount:
            self.balance-=amount
            print("Withdraw Successful")
        else:
            raise Insufficient_balance_Error('Insufficient Balance')

tus=Bank('Tushar',25,36209,10000,9090)
print(tus.name)

class Credentional_Error(BaseException):
    def __init__(self,msg):
        self.msg=msg
    
class Insufficient_balance_Error(BaseException):
    def __init__(self,msg):
        self.msg=msg

# ## r=Credentional_Error('not valid)
try:
    a=input("Enter Username: ")
    if tus.name==a:
        pin=int(input("Enter The Pin: "))
        if tus.pin==pin:
            try:
                tus.withdraw()
            except Insufficient_balance_Error as e:
                print(e)
        else:
            raise Credentional_Error('Incorrect Pin')
    else:
        raise Credentional_Error('Incorrect Username')
except Credentional_Error as e:
    print(e)
















## type type---->
class Bank:
    bank_name='SBI'
    bank_branch='Marathali'
    bank_roi=7

    def __init__(self,name,age,acc,bal,pin):
        self.name=name
        self.age=age
        self.account=acc
        self.balance=bal
        self.pin=pin

    def withdraw(self):    
        amount=int(input("Enter The Amount: "))
        if self.balance>=amount:
            self.balance-=amount
            print("Withdraw Successful")
        else:
            raise Insufficient_balance_Error('Insufficient Balance')

tus=Bank('Tushar',25,36209,10000,9090)


class Credential_Error(BaseException):
    def __init__(self,msg):
        self.msg=msg
    
class Insufficient_balance_Error(BaseException):
    def __init__(self,msg):
        self.msg=msg


a=input("Enter Username: ")
b=int(input("Enter Password: "))
try:
    if tus.name!=a or tus.pin!=b:
        raise Credential_Error('Mismatch of details')
    else:
        try:
            tus.withdraw()
        except Insufficient_balance_Error as e:
            print(e)
except Credential_Error as e:
    print(e)


















