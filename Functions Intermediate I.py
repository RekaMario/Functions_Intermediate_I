#1 Update Values in Dictionaries and Lists
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
#first
x[1][0]= 15
print(x)
#second
students[0]['last_name']= 'Bryant'
print(students)
#third
sports_directory['soccer'][0]= 'Uzuni'
print(sports_directory)
#fourth
z[0]['y']= 30 
print(z)

#2 Iterate Through a List of Dictionaries

def iterateDictionary(students):
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]
    for i in range(len(students)):
        print('first name -', students[i]['first_name'] , 'last name -' , students[i]['last_name'])

iterateDictionary(students)


#3 Get Values From a List of Dictionaries

def iterateDictionary2(students):
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]
    for i in range(len(students)):
        print(students[i]['first_name'])
        print(students[i]['last_name'])
iterateDictionary2(students)


#4 Iterate Through a Dictionary with List Values

def printInfo():
    dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
   }
    print(len(dojo['locations']), "Locations")
    for location in dojo['locations']:
        print(location)
    print(len(dojo['instructors']), "Instructors")
    for location in dojo['instructors']:
        print(location)

printInfo()