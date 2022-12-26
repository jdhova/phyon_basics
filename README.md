
```
http://localhost:8888/tree

```

### Jupyter Notebook Instalaion
 ```
 https://stackoverflow.com/questions/62255762/jupyter-is-not-recognized-as-an-internal-or-external-command-operable-program  

 $ py -m notebook
Otherwise

$ python -m pip install jupyter --user
$ jupyter notebook

 ```

 ### LIST SETS TUPLES AND DICTIONARIES


### LIST
 ```
mylist = ['juud','cole']
mylist2 = [3,4,5]
mylist3 = [4,3,5]


mylist3 == mylist3 //False because they need to be on order

print(mylist2.append(20))  // [3,4,5,20]


mylist4 = [4,3,5,5,5,5]
print(len(mylist4)) // 6  counts all values

 ```
### SETS
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

#### for Loops needs a list to loop from  good for strings


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


 ```
### Functions

 ```
s = 30
def mult(n) :
  n * 20
  
mult(s)

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