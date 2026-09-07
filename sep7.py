'''
Triple Quotes --> multiline comments --> doc string

variables -->oprators --> datatypes(Numeric, collections(str, list, tuple,sets,dicts) --> control block(logic) (if, elif, else, for ,
while, break,continue, pass) --> procedure oriented programming(functions) --> oop(class, objects)


steps
1.input
2.output
3.logic

slicing-->[start:end] --> used to get group of
indexing--> usedto get only one 
loops--> access each mail id one by one (for, while)
in --> membership variable

'''
name='codegnan'
batch=5
email_id='saketh@codegnan.com'
print(email_id[7:15])
email_ids=['santhikollu95@gmail.com','saketh@codegnan.com','sandhya12@gmail.com','info@codegnan.com','support@codegnan.com']
print(len(email_ids))
print(email_ids[-2:])
#store 3 more mail ids into above at a time
extra_emails=['abc@gmail.com','sasdffd@gmail.com']
email_ids.extend(extra_emails)
print(email_ids)

#Access each mail id one by one --> for this we use loops
for mail in email_ids:
    print(f'Mail id of person is {mail}')
    
#store the email ids with relevent user names
users={}#by default {} is indicating dictionary
'''
#set is used for unique values
#get the email ids into above users dictionary
users=dict.fromkeys(email_ids)
print(users)
users['santhikollu95@mail.com']=123
print(users)

#All python built-in datatypes are  built-in functions
#(int,float,str,list,tuple,set,dict,bool)

'''

for i in range(len(email_ids)):
        #print(i,email_ids[i])
        users[i+1]=email_ids[i]
print(users)

#enumerate --> it provides by default a counter object(you can store in desired collection)
data=dict(enumerate(email_ids,1))
print(data)

#Python --> everything in python is a object
#functions-->it is termed as first class objects because it uses recursive functions and a function can pass, return, get, use another function.
#set is an unordered collection as no indexing




















