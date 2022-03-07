# 1, Basic - print all integers from 0 to 150
from tracemalloc import stop


for i in range(1, 151):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(1, 1001):
    if(i % 5==0):
        print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

x= "Coding"
y = "Coding Dojo"
for i in range(1, 100):
    if(1%5):
        print(x)
    if(1%10):
        print(y)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum. 







# 5. Countdown by fours - Print positive numbers starting at 2018, counting down by fours.







# 6. Flexible Counter - Set three variables: lowNum, highNum, Mult. Starting at lowNum and going through highNum, print only the integers that are a multiply of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3,6,9 (on successive lines)