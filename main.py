"""
age_first = 10
print("my age is", age_first)
age_first = 18
print("my age as june 20 is ", age_first + age_first)

#integer dividsion  # ans: 5
integer_divisio = 10 // 2
print(integer_divisio)

#float dividsion  # ans: 5.0
float_divisio = 10 / 2
print(float_divisio)

#Quotient for 10/3 is 3.333
Quotient = 10 / 3
print(Quotient)

#Quotient for 10//3 is 3
Quotient = 10 // 3
print(Quotient)

#Remainder for 10%3 is 3
remainder_value = 10 % 3
print(remainder_value)



str_age_as = str(56)
print("my age is :" + str_age_as)

# STRING FORMATTING USING "f"
age = 56
#print(f"my new age is <'{age}'>'"+f"  and first age <'{age_first}'>")
# f String assigned to a variable
#my_name_is=f" I am SG and my age is  <'{age}'> "
my_name_is_1 = " I am SG and my age is :{} "
#print(my_name_is)

age_first = 39  # updating the value of age_first not applying
my_final_age_is = my_name_is_1.format(age_first)
print(my_final_age_is)
Name = "Ram"
Greetings_1 = f"Welcome first member {Name}"
print(Greetings_1)

greetings_2 = Greetings_1.format(Name=Name)
print("Welcome  Ram Twice ", Greetings_1 + '  ' + greetings_2)
Name = "Bob"
greetings_2 = Greetings_1.format(Name=Name)
print("Welcome both Ram and Bob not possible ",
      Greetings_1 + '  ' + greetings_2)

#step-1 Declare a var with assignment
#step-2 Cretae a string Template
#Step-3 Create a new variable to reuse the template
#Step-4 Print the var created

var_name = "New Year"
var_temp = "Welcome 2024 {}"
new_var_name_temp = var_temp.format(var_name)
print(new_var_name_temp)
print(var_temp.format(var_name))

#Multiplying the string with number prints that str times that number
Str_experience_months = str(1)
print(f"my experience in automation is {Str_experience_months*3} months")
int_exp_month = 3
print(f"my experience in automation is {int_exp_month*3} years")
#getting input through the console
Str_Name = input("Please Enter your name: ")
Int_Age = int(input("please enter your age in years: "))
convert_age_toMonths = Int_Age * 12
print(f"your name is {Str_Name}, your age is {convert_age_toMonths} months")
#Boolean Comparisions
str_name = input("please enter a name:")
print(str_name)
my_name = "Ram"
is_name_matches = (str_name) == (my_name)
print(f"the name both is same and matches: {is_name_matches}")
print(bool(0))  #False
print(bool('' or 0))  #False
print(bool(not 0))  # True
print(bool(not 35))  #False
#LISTS IN PYTHON:
#Declare single dimensional list
my_listS = ["one", "two", "three"]
print(my_listS)
#Get second item from list
print(my_listS[1])
#Get length of the list
print(len(my_listS))
my_listS.append("Six")
print(my_listS)
#Declare double dimensional list
my_list = [["one", '1'], ["two", "2"], ["three", "3"], ["Four", "4"]]
print(my_list)
#Get second item from list
print("my 2D list has sec item as ", my_list[1])
#Get length of the list
print(len(my_list))
#Append to list-Single DIM

#Remove to list-Single DIM
my_listS.remove("Six")
print(my_listS)
#Append to list-TWO DIM
my_list.append(["Five", "5"])
print("my 2D list has  ", my_list)
#REMOVE to list-TWO DIM
my_list.remove(["Five", "5"])
print(my_list)
#Tuples in PYTHON
#When u dont want to alter the list of items in a record use Tuples
#When you frequently change the list values yhen use LIST in Python
#Tuples Declaration
Tuples_short = ("one", "two", "three")
# Add to Tuples
Tuples_insert = Tuples_short + ("four", "Five", "Six")
print(f"Insert three new items to short tuples{Tuples_short} ", Tuples_insert)
#SET IN PYTHON HOLDS NO ORDER/NO DUPES
#Declaration of a set
set_python = {"1", "2", "3", "4", "5"}
set_new = {"6", "7", "5"}
#Add 5 to SET
set_python.add("5")
print("5 is duplicate to set python")
set_python.add("7")
print("7 is added to set python", set_python)
print("My set python wont agree duplicates[no 5] and no order", set_python)
set_python.remove("7")
print("un altered set  no order ", set_python)
#SET OPERATIONS
set_number_even = {"2", "4", "6", "8", "0"}
set_number_odd = {"0", "1", "3", "5", "7", "8"}
set_even_not_odd = set_number_even.difference(set_number_odd)
print("set number even is  ", set_even_not_odd)
set_odd_not_even = set_number_odd.difference(set_number_even)
print("set number odd is  ", set_odd_not_even)
set_not_in_both = set_number_odd.symmetric_difference(set_number_even)
print("set number not in both common   ", set_not_in_both)
set_in_both = set_number_odd.intersection(set_number_even)
print("set number both common   ", set_in_both)
set_in_all_numbers = set_number_odd.union(set_number_even)
print("set number in all   ", set_in_all_numbers)
#DICTIONARY IN PYTHON
#DICTIONARY IS NOT DUPE
#DICTIONARY IS IN ORDER
#Declaration of a Dictionary
my_dictionary={"rolf":22,"adam":34,"anne":28,"Bob":35}
my_dictionary["Zquil"]=26
my_dictionary["Tquil"]=45
my_dictionary["Acuil"]=4
print("My Dictionary has  : oredr no dupes  ",my_dictionary)



student={"class":"grad","age":12,"marks":90}
print(student.get('marks'))
print(student['marks'])
student.pop('marks')

#Dictionar: Declaration
simple_dictnry={"name":"Ram","age":13,"race":"indian"}
print(simple_dictnry["age"])

#Dictionary with Tuple
tuple_dictnry=(
      {"name":"Ram","age":13,"race":"indian"},
      {"name":"Rahim","age":11,"race":"pakistani"},
      {"name":"Rham","age":10,"race":"german"}
)
out_prnt_first_row=tuple_dictnry[0]["name"],tuple_dictnry[0]["age"],tuple_dictnry[0]["race"]
print("print tuple first row : ",out_prnt_first_row)


#Dictionary with List
#store First item in list is dictionary named output_tuple_0
output_tuple_0=tuple_dictnry[0]
print("first tuple list in dct",output_tuple_0["name"],output_tuple_0["age"],
      output_tuple_0["race"])

#store 2nd item in list is dictionary named output_tuple_1
output_tuple_1=tuple_dictnry[1]
print("second tuple list in dct",output_tuple_1["name"],output_tuple_1["age"],
      output_tuple_1["race"])

#store 3rd item in list is dictionary named output_tuple_2
output_tuple_2=tuple_dictnry[2]
print("third tuple list in dct", output_tuple_2["name"],
      output_tuple_2["age"],output_tuple_2["race"])

#Function dict() is used to turn data into dictionary object
# This below creates an empty dictionary
#my_dict1 = dict()

# You can also create a dictionary with key-value pairs
dictnry_key_value_pairs = [('a', 1), ('b', 2), ('c', 3)]
new_dict = dict(dictnry_key_value_pairs)
# This creates a dictionary {'a': 1, 'b': 2, 'c': 3}

#Declare a Tuple friends
tuple_friends=[("Ram",13),("Rahim",11),("Rham",10)]
print("Tuple of friends : ",tuple_friends)

#Create Dictionary object using tuple
tuple_to_dictionary=dict(tuple_friends)
print("Dict object from tuple using dict() funct ",tuple_to_dictionary)


#IF STATEMENTS
lst_colors = ["red", "green", "blue"]
lst_colors_light= ["yellow", "orange", "purple"]
str_input_color = input("Enter a color: ")
if str_input_color in lst_colors:
      print("Color is in the list")
elif str_input_color in lst_colors_light:
      print("Color is in thelist light")
else:
      print("Color is not in the list")

sampleList = [10, 20, 30, 40, 50,60,70,80,90,100]
sampleList.pop(4)
print("fourth popped out ",sampleList)
# 10, 20, 30, 40,60,70,80,90,100
sampleList.pop(2)
print("second popped out ",sampleList)
# 10, 20, 40,60,70,80,90,100

var_l ='None' * 10
print("value is ",var_l)
print("value is ",len(var_l))


sampleList = [10, 20, 30, 40, 50,60,70,80,90,100]
print("value for -2 ie (10-2) is 8th", sampleList[-2])
#value for 8th is  90
print("value for -4:-1 is ", sampleList[-4:-1])
# -4 is 10-4,ie 6th is 70, and-1 is 9th ie before 9th

sampleList = [10, 20, 30, 40,50]
del sampleList[1:3]
# 1st is 20 gone
# before 3rd is 30 gone
#remaining is 10,40,50
print(sampleList)

aList = [0,1,5, 10, 15, 25,35,40,45,50,55,60,65,70,75,80,85,90,95]
#Slice Every second element backwards
print(aList[::-2])
list1 = ['xyz', 'zara', 'zPYnative']
print (max(list1))
aList[1:4] = [20, 24, 28]
#: This line assigns a new list [20, 24, 28] to a slice of the 
#original list aList from index 1 to 4, #  not including the element at index 4.

#FOR LOOPS  SIMPLE
aList = [1, 2, 3, 4, 5, 6, 7]
for a in aList:
      print("print list in aList  ", a)
for b in range(1, 10):
      print("print list in  range of list  ", b)
#FOR LOOPS LIST ITEMS FROM KEYS WITH tuple_dict
print("FOR LOOPS LIST ITEMS FROM KEYS WITH tuple_dict")
tuple_dict = ({'Name': 'apple', 'Taste': 'Sour', 'Color': 'Red'}, 
           {'Name': 'banana', 'Taste': 'Sweet', 'Color': 'Yellow'},
           {'Name': 'orange', 'Taste': 'Sour', 'Color': 'Orange'},
           {'Name': 'grape', 'Taste': 'Tartar', 'Color': 'Purple'})
for fruits_types in tuple_dict:
      Name_1=fruits_types['Name']
      Tastes_1=fruits_types['Taste']
      Colors_1=fruits_types['Color']
      print(f"{Name_1} is going to be {Tastes_1} and color is showing {Colors_1} ends")

#FOR LOOPS LIST ITEMS FROM KEYS WITH 
print("second way to create dictnry using dict() ")
dict_func= dict(Name="apple", Taste="Sour", Color="Red")
print(f"{dict_func['Name']} is going to be {dict_func['Taste']} and color is showing {dict_func['Color']}")

#FOR LOOPS LIST ITEMS FROM KEYS WITH DICTNARY OBJECT
print("FOR LOOPS LIST ITEMS FROM KEYS WITH DICTNARY OBJECT")
dict_object = [{'Name': 'apple', 'Taste': 'Sour', 'Color': 'Red', 'Price': 100},
              {'Name': 'banana', 'Taste': 'Sweet', 'Color':'Yellow','Price':100},
              {'Name': 'orange', 'Taste': 'Sour', 'Color': 'Orange', 'Price': 100},
              {'Name': 'grape', 'Taste': 'Tartar', 'Color': 'Purple', 'Price':100},
              {'Name': 'Pom', 'Taste': 'Tartar', 'Color': 'Megenta', 'Price': 100},
              {'Name': 'Dragon', 'Taste': 'Sweet', 'Color': 'Megenta','Price': 100}
              ]

for fruit_types in dict_object:
      Name=fruit_types['Name']
      Taste=fruit_types['Taste']
      Color=fruit_types['Color']
      Price = fruit_types['Price']
      print(f" DICTNARY OBJECT OF {Name} is going to be {Taste} and color is showing {Color} with a Value of ${Price} ends")
    
#DESTRUTURING SYNTAX IN PYTHON USING TUPLES
print("DESTRUTURING SYNTAX IN PYTHON USING TUPLES")
#tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple_destructure_1=[('Name','Ram') , ('Age',13) , ('Race','Indian'),('Contry','Asia') , ('Eye','black') , ('Weight',90),('Name','Sam') , ('Age',12) , ('Race','dian'),('Contry','sia') , ('Eye','blu') , ('Weight',30)]

# Iterate through each tuple in the list
for i in range(0, len(tuple_destructure_1), 6):
    # Unpack each tuple, assuming each tuple has exactly six elements
    Name, Age, Race, Contry, Eye, Weight = tuple_destructure_1[i:i+6]
    print(f"Name is {Name[1]} and Age is {Age[1]} and Race is {Race[1]} and Contry is {Contry[1]} and Eye color is {Eye[1]} and body Weight is {Weight[1]} ends")
#DESTRUTURING SYNTAX IN PYTHON USING DICTINARY
print("DESTRUTURING SYNTAX IN PYTHON USING DICTINARY")
dict_person_age = {'Ram': 12, 'Andy': 13, 'Rank': 5, 'Rohan': 10, 'Ramu': 11}
# Iterate through each key-value pair in the dictionary
for key, value in dict_person_age.items():
      print(f"Key is {key} and value is {value} ends")
for person_name in dict_person_age:
      print(f"person Name is {person_name} and value is {dict_person_age[person_name]} ends")

for person_age in dict_person_age.values():
      print(f"Age value is  : {person_age}")

dict_person_age1 = {'Ramas': 12, 'Andya': 13, 'Ranks': 5, 'Rohans': 10, 'Ramus': 11}
for j in range(0, len(dict_person_age1), 2):
      keys = list(dict_person_age1.keys())
      values = list(dict_person_age1.values())
      print(f"Key is {keys[j]} and value is {values[j]} ends")      

#We CAN RETRIEVE VALUE AND KEY FROM DICTIONARY USING ITEMS, AND RETRIEVE # VALUES ALONE FROM FROM DICTIONARY USING VALUES() WITH DESTRUCTURING

#SET QUIZ
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.add("Blue")
sampleSet.add("Orange")
print(sampleSet)

sampleSet1 = {"Yellow", "Orange", "Black"}
sampleSet1.discard("Orange")
print(sampleSet1)

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set1.difference_update(set2)
print(set1)

set2.difference_update(set1)
print(set1)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}

print(set1.issubset(set2))
print(set2.issuperset(set1))

sampleSet2 = {"Yellow", "Orange", "Black"}
sampleSet2.update(["Blue", "Green", "Red"])
print(sampleSet2)

set11 = {"Yellow", "Orange", "Black"}
set12 = {"Orange", "Blue", "Pink"}

set13 = set12.difference(set11)
print(set13)

sampleSeta = {"Yellow", "Orange", "Black"}
sampleSeta.discard("Blue")
print(sampleSeta)

set12 = {10, 20, 30, 40}
set22 = {50, 20, "10", 60}

set32 = set12.union(set22)
print(set32)

sampleSetb = {"Yellow", "Orange", "Black"}
sampleSetc=sampleSetb.copy()
print("new set c is : {sampleSetc} ")
for a in sampleSetb:
      name=a[0:7]
      print("printing elements from set : ",name)

print("Two way to create Break and continue")
cars={"BMW","Audi","Faulty","Honda","Tesla"}
for status in cars:
    if status=="Faulty":
        print("Status is Faulty")
        break
for status1 in cars:
    if status1=="BMW":
        print("Status is BMW")
        continue 
for status2 in cars:
   if status2=="Tesla":
        print("Status is Tesla")
else:
      print("Status is not BMW")       


print("Find a number is aprime number")
for a in range(1,15):
      for b in range(2,a):
            if a%b==0:
                  print(f"this {a//b}")
                  print(f"{a} is not a prime number")
                  print(f"{a} equals {b} * {a//b}")
                  break
      else:
            print(f"this will be {a} is a prime number")

for a in range(1,12):
      for c in range(2,a):
            if a%c==0:
                  print(f"this {a//c}")
                  print(f"{a} is not a prime number")
                  print(f"{a} equals {c} * {a//c}")
                  break
      else:
            print(f"this will be {a} is a prime number")
            """
"""                                                            
Enter 'a' to add a movie, 'l' to see the movies, 'f' to find the movies and 'q' to quit the movies
--Add Movies                                                   
--show movies                                                  
--find a movie                                                 
-stop running the movie                                             
Tasks:                                                                                                        
[]: Decide where to store the movie                            
[]: what is the format of the movie                            
[]: show user the main interface and get their input           
[]: Allow users to add movie                                   
[]: show all their movies                                      
[]: Find a  movie                                              
[]: Stop running the program when they enter 'q'               
"""          
movies = []                 
"""                         
     movie = {              
     'name':         (str), 
     'director':     (str), 
     'year':         (int)  
     }                      
"""
def menu():            
    user_input = input ( "Enter 'a', 'l' , 'f' and 'q'  :  " ) 
    while user_input != 'q':
        if user_input == 'a':                                                   
              add_movie ()                                  
        elif user_input == 'l':
            show_movie ()           
        elif user_input == 'f':
              find_movie ()                                      
        else:                                                  
            print ( "unknown command" )                        
        user_input = input ( "Enter 'a', 'l' , 'f' and 'q'  :  " )         

def add_movie():                                                           
    name = input ( "Enter a movie name  :  " )                             
    director = input ( "Enter a directr name  :  " )                       
    year = int ( input ( "Enter a movie name  :  " ) )                     

    movies.append ({                                           
        'name':name,                                           
        'director':director,                                   
        'year':year                                            
    })                                                         
menu ()                                                                    
print(movies)