import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','~','^','&','*','(',')','+']
print("PASSWORD GENERATOR!!")
hi_letters=int(input("Tell me how many Letter you want to enter?\n"))
hi_numbers=int(input("Tell me how many numbers you want to enter?\n"))
hi_symbols=int(input("Tell me how many symbols you want to enter?\n"))
password=""
pass_list=[]
for i in range(1,hi_letters+1):
    char=random.choice(letters)
    pass_list +=char
for i in range(1,hi_numbers+1):
    char=random.choice(numbers)
    pass_list +=char
for i in range(1,hi_symbols+1):   
    char=random.choice(symbols)
    pass_list +=char
print('------------------------------')
print(pass_list)

for char in pass_list:
    password = password+char
print(password)