def greet():
  print("hello")

greet()

def greet(name):
  print("hello",name)

greet("hemanth")

def add(num1,num2):
  return num1+num2
sum = add(134,342)
print(sum)

# positional arguments -> you can pass multiple positional arguments by using *args 
# keyword arguments -> you can pass multiple keyword arguments by using **kwargs

def mult(num1,num2,*args,**kwargs):
  return num1*num2

result = mult(45,6,837,3648,name="Srihari",value="zero")
print(result)