def open_account() :
  print("create account.")

def deposit(balance, money):
  print("The deposit has been completed. The balance is {0}.".format(balance + money))
  return balance + money

def withdraw(balance, money) :
  if balance >= money :
    print(money, "has been withdrawn. The balance is {0}.".format(balance - money))
    return balance
  else :
    print("The amount you want to withdraw is higher than the amount you have, so you cannot withdraw.")


balance = 0
balance = deposit(balance,1000)
print(balance)
balance = withdraw(balance,1200)

def profile(name, age, main_lang="Python") :
  print("Name : {0}\t Age : {1}\t Main_Lang : {2}".format(name, age, main_lang))
"""def인수에 기본값을 넣을 때는 뒤에서부터 채울것 
When you put the default value in the def argument, fill it from the back."""
profile("Kim Geun Ho", "22", "Python")
profile("KGH","22")

def profile_1(name,age,l1,l2,l3,l4,l5):
  print("Name :{0}\t Age:{1} \t".format(name,age), end=" ")
  print(l1,l2,l3,l4,l5)
profile_1("KGH", 22, "C", "C++","C#","Python","Java")

gun = 10

def cp(soldiers):
  gun = 20
  gun = gun - soldiers
  print("The gun amount left in the function : {0}".format(gun))

print("All the Gun :{0}".format(gun))
cp(2)
print("The remaining gun : {0}".format(gun))

def cp_r(gun,soldiers):
  gun = gun - soldiers
  print("The gun amount left in the function : {0}".format(gun))
  return gun

print("All the Gun :{0}".format(gun))
gun = cp_r(gun,2)
print("The remaining gun : {0}".format(gun))