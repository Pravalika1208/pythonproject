password=input("enter your password:")
special=['!','@','#','$','%','^','&','*','_']
space=" "
def check_password(password):
    if len(password)<10 or len(password)>15:
        return "Weak:password should contain min 10 char and max 15 char"
    elif not any(char.isupper() for char in password):
        return "Moderate:use at least one uppercase letter"
    elif not any(char.islower() for char in password):
        return "Moderate:use atleast one lowercase letter"
    elif not any(char.isdigit() for char in password):
        return "Moderate:use atleast one digit"
    elif not any(char in special for char in password):
        return "Moderate:use atleast one special char"
    elif ' ' in password:
        return "Moderate:white spcaes are not allowed"
    elif password.endswith('.') or password.endswith('@'):
        return "Moderate:password should not end with dot or @"
    else:
        return "Strong:good password"
result=check_password(password)
print(result)
enter your password:Pravalika@123
Strong:good password

[5]
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
fact(5)
120
[9]
a=[44,56,89,90]
b=[67,59,78]
a.append(b)
a[4]
a[4][0]
67
[10]
a={}
type(a)
dict
[11]
def calculate(cart):
    total=sum(cart.values())
    if len(cart)>5:
        total*=0.9
    return total
cart={'lap':50000,'headphones':2000,'mouse':3500,'key':1500,'monitor':8000,'usb':1000}
print(f"cart items:{cart}")
print(f"total price:{calculate(cart)}")
cart items:{'lap': 50000, 'headphones': 2000, 'mouse': 3500, 'key': 1500, 'monitor': 8000, 'usb': 1000}
total price:59400.0

[12]
def calculate(cart):
    total=sum(cart.values())
    if total in range(20000,50000):
        total*=0.9
        return total
    elif total>50000:
        total*=0.85
        return total
cart={'lap':50000,'headphones':2000,'mouse':3500,'key':1500,'monitor':8000,'usb':1000}
print(f"cart items:{cart}")
print(f"total price:{calculate(cart)}")   
        
cart items:{'lap': 50000, 'headphones': 2000, 'mouse': 3500, 'key': 1500, 'monitor': 8000, 'usb': 1000}
total price:56100.0

[15]
def add(menu,item):
    menu.append(item)
    return menu
def remove(menu,item):
    if item in menu:
        menu.remove(item)
        return menu
    else:
        print(f"Item '{item}' is not present in the menu")
        return menu
def check_avail(menu,item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")
menu=['rice','pasta','soups']
print("current menu:",menu)
add_item=input("add_item=")
remove_item=input("remove_item=")
check_item=input("check_item=")
menu=add(menu,add_item)
menu=remove(menu,remove_item)
check_avail(menu,check_item)
print("Updated menu:",menu)
check_avail

current menu: ['rice', 'pasta', 'soups']
add_item=biryani
remove_item=rice
check_item=pasta
pasta is available
Updated menu: ['pasta', 'soups', 'biryani']

<function __main__.check_avail(menu, item)>
