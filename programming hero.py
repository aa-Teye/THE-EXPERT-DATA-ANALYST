#Taking inputs and coverting them 
'''
age_test = input('Enter your age: ')
age = int(age_test)
print( "your age is age:", age)

#Simple Additon

num1 = input('Enter first number:')
num2 = input ('Enter second number:')
sum = int(num1)  + int(num2)
print("The sum of first number and second number is:", sum)

#Simple Division
money = input('Enter the amount of money for all families:')
families = input('Enter the number of families:')
each_family = int(money) / int(families)

print("Each family will get:", int(each_family), "amount of money.")
'''


# Problem: The Grade Calculator
'''Objective: Write a program that takes a student's score as input and outputs their corresponding grade.

Grading Scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
Input: An integer representing the student's score.

Output: A string representing the student's grade (e.g., "A", "B", "C", "D", "F").

Constraints:

The input score will be between 0 and 100, inclusive.
Example Test Cases:

Input Score	Expected Output
95	A
82	B
70	C
65	D
45	F
100	A
0	F

'''


'''
Score = int(input('Enter your score:eg, 89,76.....'))
if Score >= 90:
    print('you had an A ')
elif Score >= 80:
    print('you had a B')
elif Score >= 70:
    print(' you had a C')
elif Score >= 60:
    print('you had a D')
elif Score <60:
    print('you had an F')
else:
    print('Invalid score, please enter a score between 0 and 100.')



#PLAYING WITH LISTS
NamesOfAnimals = ['cat' 'dog', 'lion', 'tiger', 'elephant']
NamesOfAnimals.append('monkey')  # Adding a new animal to the list
print(NamesOfAnimals)
NamesOfAnimals.append(50)
NamesOfAnimals.append(50.5)
print(NamesOfAnimals)
TotalOfAnimals = len(NamesOfAnimals)  # Getting the total number of animals in the list
print("Total number of animals in the list:", TotalOfAnimals)


#Objective:
#You'll simulate managing items in a simple shopping cart. This will involve adding items, removing items, checking if an item is in the cart, and displaying the contents.
media_Items = ['camera , camcorder, Laptop, hdmi_cables,Vga_cables, video_capture_card']
media_Items.append('microphone')
media_Items.append('sound_card')
media_Items.remove('hdmi_cables')
media_Items.remove('network_cables')
if i in media_Items:
    print('Item is in the media_Items list')
else:
    print('Item is not in the media_Items list')
print(len(media_Items))#

print('media Items;', media_Items)



#ADVANCE LIST
#USING SORTING
nums = [21, 63, 1, 36, 11]
nums.sort()
print(len(nums))
print(max(nums))
print(min(nums))
print(nums)

#SORTING A STRING
female_actor = ["Sandra Bullock", "Jennifer Lawrence", "Angeline Jolie", "Paris Hilton"]
female_actor.sort()
print(female_actor)

#HOW TO CHANGE ORDER , PUTTING THE LAST ELEMENT TO FIRST AND THE FRIST TO LAST

actors = ["Brad Pitt", "Johnny Depp","Will Smith", "Matt Damon"]
actors.sort()# THE SORT KEYWORD ARRANGE IT IN ASCENING ORDER WHETHER NUMERIC OR ALPHATICAL EG.[] ALEX, ALICE] AND [1, 2, 3]
actors.reverse()
print(actors)

#USING RANGE : SELECTING A GROUP VALUE OUT OF AVLIST
#IN RANGE (4, 20) THE STARTING NUMBER IS 4 AND STOPPING VALUE IS 20
nums = [21, 63, 1, 36, 11]
nums.sort()
nums2 = nums[0:3]
print(nums2)

#WORKING ON LOOPS IN A LIST 
#EXAMPLE 1
nums = [21, 63, 1, 36, 11]
nums.sort()
for num in nums:
    print(num)

#EXAMPLE 2 [ I ADDED A AND IF CONDITION TO LOOP]
nums = [21, 63, 1, 36, 11]
nums.sort()
for num in nums:
    if num < 20:
        print(num)
    else:
        print("number in valid ")

#EXAMPLE 3 
nums = [21, 63, 1, 36, 11]
nums.sort()
for num in nums:
    message = "number valid and is " + str(num)
    print(message)
    if num < 20:
        print(num)
    else:
        print("number bigger than 20")

#EXAMPLE 4 USING BREAK:

nums = [21, 63, 1, 36, 11]
nums.sort()
for num in nums:
    if num >= 50:
        break
    print(num)

#EXAMPLE 5 USING CONTINUE[ continue is used when you want to skip a particular value when the condition is met]
nums = [21, 63, 1, 36, 11]
nums.sort()
for num in nums:
    if num == 11:
        continue
    print(num)
'''
#PLAYING WITH FUNCTIONS
def brushTeeth():
    print("Take the toothbrush")
    print("Add toothpaste")
    print("Get some bottle of water")
    print("Go to the batheroom")
    print("Final Brush your teeth")

brushTeeth()

def summation(num1 ,num2):
    num1 = int(input(" Enter fisrt number:"))
    num2 = int(input("Enter seond number:"))
    sum = num1 + num2 
    print("The sum is ", sum)

summation(25, 45)