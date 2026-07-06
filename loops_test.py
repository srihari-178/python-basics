# 1)print numbers from 1 to 10 using a for loop
# numbers = 10
# for num in range(1,numbers+1):
#     print(num)

# 2) print numbers from 10 to 1 using a whie loop

# numbers_1 = 10;
# while numbers_1 >=1:
#     print(numbers_1)
#     numbers_1-=1

# 3) print all even numbers between 1 and 20

# for even_num in range(2,21,2):
#     print(even_num)

# 4) print all the odd numbers between 1 and 20

# for odd_num in range(1,20,2):
#     print(odd_num)

# 5) find the sum of numbers from 1 to 10

# num = 1
# sum_1 = 0
# while num <= 10:
#     sum_1+= num
#     num+=1

# print(sum_1)

# print(sum(range(1,11)))

# 6) print each name from this list using a for loop 

# names = ["Srihari","Ravi","sekhar","kiran"]
# for elem in names:
#     print(elem)

# 7) print both the index and value of each item in the list:
# fruits = ["apple","banana","mango","orange"]
# for indx,fruit in enumerate(fruits):
#     print(indx , fruit)

# 8) print numbers from 1 to 20 but skip number 10
# for num in range(1,21):
#     if num==10:
#         continue
#     print(num)

# 9) print numbers from 1 to 20 but stop the loop completely when the number become 15

# for num in range(1,21):
#     if num==15:
#         break
#     print(num)

# 10) count how many vowels are present in this string:

word = "kubernetes"
vowels_count = 0
for ch in word:
    if ch in 'AEIOUaeiou':
        vowels_count+=1

print("The number of vowels present is:",vowels_count) 

# 11) print every character from this string using a for loop

text = "DevOps"
for ch in text:
    print(ch)

# 12) find the largest number in this list using a loop

# numbers = [12,45,7,89,34,56,101,3547,32]
# largest_num = numbers[0]
# for i in numbers:
#     if i > largest_num:
#         largest_num = i
      
# print(largest_num)

# 13) Find the smallest number in the list using a loop:

numbers = [12,45,7,89,34,56,-5]
smallest_num = numbers[0]
for i in numbers:
    if i <smallest_num:
        smallest_num = i
print(smallest_num)

sample = ["server1","server2","server3","server4"]
for i in range(len(sample)):
    print(sample[i])

sample1 = ["pod1","pod2","pod3","pod4"]
for i in sample1:
    print(i)
    





