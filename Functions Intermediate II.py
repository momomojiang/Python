x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# How would you change the value 10 in x to 15?  
# Once you're done x should then be [ [5,2,3], [15,8,9] ]. 
x[1][1]=15
print(x) 
# How would you change the last_name of the first student 
# from 'Jordan' to "Bryant"?
student[0]['last_name']="Bryant"
print(students )
# {'first_name': 'Michael', 'last_name': 'Bryant'}
# {'first_name': 'John', 'last_name': 'Rosales'}

# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0]="Andres"

print(sports_directory)
# basketball  =  ['Kobe', 'Jordan', 'James', 'Curry']
# soccer  =  ['Andres', 'Ronaldo', 'Rooney']

# For z, how would you change the value 20 to 30?
z = [ {'x': 10, 'y': 20} ]

z[0]['y']=30
print(z)

# 2. Create a function that given a list of dictionaries, it loops through each 
# dictionary in the list and prints each key and the associated value.  
# For example, given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def function1():
    for person in students:
        for k, v in person.items():
            print(f"{k}-{v}",end=" ")
        print()

solution 2:
def changecolon():
    for s in students:
        print(str('first_name'),' - ',s['first_name'],',',str('last_name'),' - ',s['last_name'])

changecolon()

# 3. Create a function that given a list of dictionaries and a key name, 
# it outputs the value stored in that key for each dictionary. 
#  For example, iterateDictionary2('first_name', students) should output
def iterateDictionary2():
    for person in students:
        print(person['first_name'], end="\n")
    print()
iterateDictionary2() 

# 4.  Say that
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print(f"{(len(dojo['locations']))}"' '"LOCATIONS")
def printDojoInfo1(dojo):

    for i in dojo:
        x=dojo['locations']
    for y in x:
      print(y)
printDojoInfo1(dojo)



print(f"{(len(dojo['instructors']))}"' '"INSTRUCTORS")
def printDojoInfo2(dojo):

    for z in dojo:
        z=dojo['instructors']
    for m in z:
      print(m)
printDojoInfo2(dojo)


def changeValue()













