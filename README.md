
```
http://localhost:8888/tree

```

### Jupyter Notebook Instalaion
 ```
 https://stackoverflow.com/questions/62255762/jupyter-is-not-recognized-as-an-internal-or-external-command-operable-program  

 https://replit.com/@JudeOkagu1/CodeInBlack#index.js

 https://onecompiler.com/python2/3ysyk2cfv



 $ py -m notebook
Otherwise

$ python -m pip install jupyter --user
$ jupyter notebook

 ```

 ### LIST SETS TUPLES AND DICTIONARIES


### LIST list are also inbult functions check below
 ```
mylist = ['juud','cole']
mylist2 = [3,4,5]
mylist3 = [4,3,5]


mylist3 == mylist3 //False because they need to be on order

print(mylist2.append(20))  // [3,4,5,20]


mylist4 = [4,3,5,5,5,5]
print(len(mylist4)) // 6  counts all values

 ```
### SETS   sets are also inbuit functions like list() check below
  ```
mysets = {'juud','cole'}
sets = {2,3,4}
sets2 = {4,3,2}

print(mysets,sets2)  //  {'cole','juud'} {2,3,4} Automatically arranges in order lowest to highest

sets2 = {4,3,2,2,2,2,2,2,2,2,2,2}

print(sets2 == sets)  //true

print(len(set3))  //3 delets repeted values

 ```
 ### TUPLES
 ```
my_turple = (1,2,3)
my_turple2 = (3,2,1)
my_turple == my_turple2  //false These are similar to lists just you canr append() better for optimization and memory alocation and its faster


turple umpacking works also works with a collection of arrays and lists and booleons
x=(1,2,3,4,5)

a,b,c,d,e = x

print(a)
print(b)
print(c)
print(d)
print(e)



 ```
### Dictionaries
 ```

person = {
  'fname':'jude',
 'lname':'ik',
  'age': 20
}
person = {
  'fname':'jude',
 'lname':'ik',
  'age': 25
}

print(person['age']) // 25

 ```
### Operators
 ```
true and true is true
true and false is true
true or false is true
false or false is false 
not true is false 
not false is true

1 in [1,2,3]  // true

 ```
### If Else Statment syntax
#### true and false give error should be True or False 
#### if a = true also gives error

 ```

a = True
b = True
c = False

if a:
      print('Is It Snowing')
      if b: 
        print('yes')
        if c:
          print('Summer on the way')
else:
    print('its hot')


 ```

### Loops

#### for Loops needs a list to loop from  good for strings range saves in variable


 ```
a = [1,2,3,4,5,6]

for n in a:
  print(n)

#### while loops is based on a condision does not need a list to loop from  example countdown
a = 0
while a < 7 :
    print (a)
    a+=2
    // a = a + 2


mylist = list(range(20))

print(mylist[:: 2])

 ```
### Functions

 ```
s = 30
def mult(n) :
  n * 20
  
mult(s)


def perfomOp(num1,num2,num3,operation='sum',message='here we'):
  # print(message)
  if operation == 'sum':
   print(message,operation,num1* num2 * num3)
  if operation =='multiply':
     # return num1 * num2 * num3
     print(message,operation,num1* num2 * num3)
    
perfomOp(3,4,5,'sum')

 ```
 ### Classes

 ```

class Persons:
    def __init__(person, name):
        person.name = name
        person.legs = 4
    
    def details(person):
        print(person.name + ' is a man!')
    
    def details2(person):
      print(person.name + ' is a woman!')
        
        
  
my_friend = Persons('Jude')
my_wife = Persons('Ego Oyibo')

my_friend.details()
my_wife.details2()


 ```
 ### Formating, slicing, Multi-Line and concat Str, 

 ```

print(f' my age is {20}')

list = [2,3,5,1,6,7]

names = 'my name is jude'

print(list[2:])

print(names[2:])


quote = '''
this is my new line
i start on one 
and end below
'''

print(quote)

 ```
 ### copy append,pop and remove
```
 
my_list = [1,2,3,4,5]
my_list.append(30)
my_list.remove(3)
while len(my_list):
  print(my_list.pop())
print(my_list)


a = [1,2,3,4]
b = a.copy()
a=[1,2,3]
print(b,a)

```
### Range and Slice

```

my_list = [1,2,3,4,5,6,7,8,9]

print(my_list[3:6]) // 4,5,6

print(my_list[3::2])  // 4,6,8


mylist = list(range(20))

print(mylist[:: 2])


```
### Challange

```
### challange create a function which accepts numbers and
#### prints I ENJOY if number is divisible by 3 
#### prints I  CODING if number is divisible by 5 
#### prints I ENJOY CODING PYTHON if number is divisible by 15 

### creates another function that loops tru withh range and slicing and prints same values

```
### convarting a list to a Turple (removing Duplicates)  sets and list data structures

```
my_list = [1,2,3,4,5,1,2,3,4,5]

new_set = set(my_list)

new_list = list(set(my_list))

print(my_list)

print(new_set,' is a turple')

print(new_list,' is a list which works with split :: and  index []')

print(new_list[0:3])


print(new_set) 



new_set.add('e')
new_list.append('e')

new_set.remove(5)
new_list.remove(5)

print(1 in new_set)
print(1 in new_list)

print(len(new_list))

print(len(new_set))

print('poped from list:',new_list.pop(3))

new_set.discard(1)

print('new set',new_set)
print('new list',new_list)


Turples are non immutable cos they are more effitient and allocates exact space in memory

```
### Dictionaries

#### Challange

```
Write a Dictionary check if Dictonary has Nationality
bades on result Add Natiinality and then  pop nationalities out after added to dictonary

check if Name is in names and if so populate new name to list

```
#### Solution

```
person = {
  'name' : ['Jude', 'James','Ann'],
  'age' : [25,33,21],
'occupation' : ['Dev','Nurse','Teacher']
}


person['name'].append('Dave')     # dding 'Dave' 

if 'Nationality' not in person :
      person['Nationality'] = []

person['Nationality'].append('Canadian')
person['Nationality'].append('Nigerian')
person['Nationality'].append('Kenya')                 #Adding Nationality

if 'name' in person:
  person['name'].append('Ego Oyibo')                #Checking for name befre adding

if 'Ego Fresh' not in person['name'] :
    person['name'].append('Ego Fresh')
  
while len(person['Nationality']):
  print('poped item',person['Nationality'].pop(0))       #Checking for len before poping



print('Nationality is empty',person['Nationality'])
print(person)

from collections import defaultdict  can also be used 
```

### If ELSE 

#### Fizz Buzz Statment 
```
for n in range(1,50):
  if n % 15==0 :
    print('fizz')
  elif n % 5 ==0:
    print('buzz')
  elif n % 3 ==0:
    print('fizzbuzz')
  else:
    print(n)


  [ 'fizzBuzz' if n % 15 == 0 else 'Fizz' if n % 5 == 0 else 'buzz' if n % 3 == 0 else n for n in range(2,100)]

```
### FOR LOOPS

```

d = {'apple': 1, 'banana': 2, 'orange': 3}

for key,value in d.items():
  print('the key is',key, 'the value is',value)


for key in d:
  print(key, d[key])


  for key in d.keys():
  print(key)

# Output:
# apple
# banana
# orange

for value in d.values():
  print(value)

# Output:
# 1
# 2
# 3

```

### BINARY

```

import numpy as np

 

b2 = [128, 64, 32, 16, 8, 4, 2, 1]
on = [  0,  1,  1,  1, 1, 1, 1, 0]

 

# how many bits in a byte?
len(b2)

 

b2 = np.array(b2)
on = np.array(on)

 


print(on)
print(b2 * on)
print()
print(sum(b2 * on))

```


### Notes
```
check for values in memory between sets and lists  
always use .copy()
natural language

make turples from turples
SSIS DTS means Data Transformation Services
```



