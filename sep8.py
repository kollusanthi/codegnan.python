'''

Student Marks Manager
---------------------
#make sure to create marks list
marks=[]
for mark in range(3):
    mark=int(input('Enter the marks: '))
    marks.append(mark)
#print(marks)
#Insert 90 marks into the list
marks.insert(0,90)
#print(marks)
#add multiple marks
marks.extend([75,85])

if 75 in marks:  #check for 75 marks in given marks list
    marks.remove(75)  #remove 75 from the list
#to remove the final mark using pop
removed_mark=marks.pop()
print(f'Removed mark is {removed_mark}')
#final list of marks
print(f'Final student marks list is {marks}')
print(f'Count of student marks list is {len(marks)}')



Number List Analyser
--------------------
numbers=[20,10,30,20,40,20]
#sort the list in ascending order
numbers.sort()
#print(numbers)
numbers.reverse() #reverse to descending order
#print(numbers)
#ask user for a number to search in the list
num=int(input('Enter a number to search: '))
if num in numbers:
    print('Number found')
    print('Count: ', numbers.count(num))#count of the search element in list
    print('First index: ',numbers.index(num))#index of the search element in the list
else:
    print('Number not found')
print('smallest value: ',min(numbers))
print('Largest value: ',max(numbers))
print('Total: ', sum(numbers))


Even and Odd numbers separator
-------------------------------
numbers=[10,15,20,30,35]
even=[] #create empty list to store even values
odd=[] #create empty list to store odd values
for num in numbers:
    if num%2==0: #check the element in the list is even or not
        even.append(num) #if the element is even then we store it in the even list using append() method
    else:
        odd.append(num) #if the element is odd then we store it in the odd list using append() method
print('Even numbers: ', even)
print('Odd numbers: ',odd)
print('First 3 numbers in the list: ',numbers[:3])
print('Last 3 numbers in the list: ',numbers[-3:])
backup=numbers.copy() # copy the numbers list 
#print(backup)
numbers.clear() #delete all the elements in the original list using clear() method
print(f'Original list: {numbers}')
print(f'backup list: {backup}')


BMI problem
-----------
#Task --> store the results of name, weight, height --> BMI into a collection

#Repetition --> while
#same above task we need to handle the errors (Exception handling) and also
#make sure strictly to enter only numeric values

def bmi():
    users=[]
    no_of_users=int(input('Enter no of users: '))
    for i in range(no_of_users):
        while True:
            name=input('Enter the user name: ')
            weight=int(input('Enter the weight in kgs: '))
            height=float(input('Enter the height in meters: '))
            #in this case we prefer Exception Handling
            try:
                if weight>0 and height>0:
                    break
            except Exception as e:
                print(f'The Error is {e}')
        BMI=(weight)/((height)**2)
        if BMI<18.5:
            print(f'{name} is into Under Weight category and BMI is {BMI}')
        elif BMI>=18.5 and BMI<=24.9:
            print(f'{name} is into Normal weight category and BMI is {BMI}')
        elif BMI>24.9 and BMI<=29.9:
            print(f'{name} is into Over weight category and BMI is {BMI}')
        elif BMI>=30:
            print(f'{name} is into obesity category and BMI is {BMI}')
        
    else:
        print('Make sure to enter only positive values')
        bmi()
    users.extend([name, weight, height])
    print(users)
        
bmi()        



'''

#control block (if, elif, else, for, while, break, continue)
#BMI usecase --> BMI (Body Mass Index)

#weight --> kgs
#height --> meters
#feet --> 12 inches
#inch --> 2.54cm

#BMI = (weight)/((height)**2)
def bmi():
    users=[]
    no_of_users=int(input('Enter no of users: '))
    for i in range(no_of_users):
        while True:
            #in this case we prefer Exception Handling
            try:
                name=input('Enter the user name: ')
                weight=int(input('Enter the weight in kgs: '))
                height=float(input('Enter the height in meters: '))
                if weight>0 and height>0:
                    break
            except Exception as e:
                print(f'The Error is {e}')
        BMI=(weight)/((height)**2)
        if BMI<18.5:
            print(f'{name} is into Under Weight category and BMI is {BMI}')
        elif BMI>=18.5 and BMI<=24.9:
            print(f'{name} is into Normal weight category and BMI is {BMI}')
        elif BMI>24.9 and BMI<=29.9:
            print(f'{name} is into Over weight category and BMI is {BMI}')
        elif BMI>=30:
            print(f'{name} is into obesity category and BMI is {BMI}')
    users.extend([name, weight, height])
    print(users)
        
bmi()        
















