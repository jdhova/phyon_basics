
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


#### LIST
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
 #### TUPLES
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

print(person['age'])

 ```