#FOR LOOP PROBLEMS
#basic understanding
#1. print numbers from 1 to 10 in one line
for x in range(1, 11):
    print(x, end=' ')  # 1 2 3 4 5 6 7 8 9 10

#2. print even numbers from 5 to 30 in one line
for x in range(5, 31):
    if x % 2 == 0:     # 6 8 10 12 14 16 18 20 22 24 26 28 30
        print(x, end=' ')

#3. print odd numbers from 5 to 30 in one line
for x in range(5, 31):
    if x % 2 != 0:     
        print(x, end=' ')  # 5 7 9 11 13 15 17 19 21 23 25 27 29

#4. print numbers divisible by 5 from 1 to 30 in one line
for x in range(1, 31):
    if x % 5 == 0:
        print(x, end=' ') # 5 10 15 20 25 30

#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for x in range(1, 101):
    if x % 5 == 0 and x % 7 == 0:
        print(x, end=' ')   # 35 70

#6. sum of numbers from 10 to 25
sum = 0
for x in range(10, 26):
    sum += x
print(sum)  #280

#7. sum of numbers in any list
l = [10, 20, 30, 40, 50]
sum = 0
for x in l:
    sum += x
print(sum)  #150

#8. multiplication table of a number 
n = int(input("Enter a number: "))
for x in range(1, 11):
    print(n, '*', x, '=', n * x)

#interview problems
#9. factorial 
n = int(input())

fact = 1
for i in range(1, n + 1):
    fact *= i

print(fact)

#10. fibonacci 
n = int(input())

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#11. reverse a string
s = input()

print(s[::-1])

#12. count vowels in a string
s = input()

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print(count)

#13. count z's and y's in a string
s = input()

z = 0
y = 0

for ch in s:
    if ch == 'z':
        z += 1
    elif ch == 'y':
        y += 1

print("z:", z)
print("y:", y)

#14. check whether a number is prime number or not 
n = int(input())

if n < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")



#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
x = 1
while x <= 10:
    print(x, end=' ')
    x += 1  # 1 2 3 4 5 6 7 8 9 10

#print even numbers from 1 to 10
x = 1
while x <= 10:
    if x % 2 == 0:
        print(x, end=' ')
    x += 1  # 2 4 6 8 10

#print numbers divisible by both 5 and 7 from 1 to 500
x = 1
while x <= 500:
    if x % 5 == 0 and x % 7 == 0:
        print(x, end=' ')
    x += 1   # 35 70 105 140 175 210 245 280 315 350 385 420 455 490

#interview problems
#count digits
n = int(input())

count = 0

while n > 0:
    count += 1
    n //= 10

print(count)

#reverse a number
n = int(input())

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)

#palindrome number 
n = int(input())

original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#palindrome string (without slicing, built in function)
s = input()

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#armstrong number
n = int(input())

original = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** digits
    n //= 10

if original == sum:
    print("Armstrong")
else:
    print("Not Armstrong")