
#LIST

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

'''apan single inverted comma ya
double inverted comma bhi use kar skte hae list mae.'''


#accesing items in a list 
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles[0])

#title function is use to write any element neat an cleaN
#for example trek befor use title() and after using title()
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles[0].title())

#index position start at 0, Not 1.
'''for ex. we can use upper() & lower() to display in capital or small leters.
we can change index number also for paricular elements.'''
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles[2].upper())

bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles[1].lower())

bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles[1])
print(bicycles[3])

#python has a special syntax for accesing last elemnt in a list
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles[-1])
'''the index -1 python always return last element of list, for asking -2 return second
item from the end of the list, -3 return third 
item from the end, and so forth, fifth, sixth.........'''
bicycles = ["trek","Hero","jalwa","cannondale","redline","specialized"]
print(bicycles[-2])

#Using invidual values from a list
bicycles = ["Jalwa","cannondale","redline","specialized"]
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#TRY IT YOURSELF (Python book Pg No-36)
# Ex-3.1
names = ['rohan','shyam','mohan','geeta','babita']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

# Ex-3.2
names = ['rohan','shyam','mohan','geeta','babita']
message0 = f"How are you and what are you doing? {names[0].title()}"
message1 = f"How are you and what are you doing? {names[1].title()}"
message2 = f"How are you and what are you doing? {names[2].title()}"
message3 = f"How are you and what are you doing? {names[3].title()}"
message4 = f"How are you and what are you doing? {names[4].title()}"

print(message0)
print(message1)
print(message2)
print(message3)
print(message4)

#Ex-3.3
car = ['BMW','Mecredise','Lemborgini','Jaguar','RollsRoyce',' Toyota Supra']
statement0 = f"Kassh mae {car[0].title()} kharid pata."
statement1 = f"Mae {car[1].title()} car ko kal kharid lunga!!"
statement2 = f"{car[2].title()} chalai jane hoo sanu di chuta lene ho "
statement3 = f'Mene gadi kharidni hae {car[3].title()}.'
statement4 = f'{car[4].title()} mae mene guu kadiya guys hehehe..'
statement5 = f'naame toh suna hii hoga appun kae ilake mae appun koo {car[5].title()} khete hae!!@@'

print(statement0)
print(statement1)
print(statement2)
print(statement3)
print(statement4)
print(statement5)


#modifying elements in a list
motorcycles = ['Honda','yamaha','Suzuki']
print(motorcycles)
''' the  first code defines the original list,with 'honda' at the first elemnt.
The second code changes the value of the first item to 'ducati.
    The output shows that the first item has indeed changed , and the rest of the list   '''
motorcycles[0] = 'Ducati'
print(motorcycles)


#Adding elemts to a list 
# Appending elements to the end of a list
motorcycles = ['Honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')  #adding elements using append()
print(motorcycles)

# using empty list,lets add the elements to the list
motorcycles = []

motorcycles.append('Honda') #adding elements to the list one by one.Que- Kya mae ek sath elemts add kaer skta huu?
motorcycles.append('suzuki')
motorcycles.append('yamaha')

print(motorcycles)

#inserting elements into a list
motorcycles = ['honda','suzuki','yamaha']
motorcycles.insert(0, 'ducati')  #adding element at first place using insert()

print(motorcycles)

#removing elements from a list
#removing an item using the del statement
motorcycles = ['honda','suzuki','yamaha']
print(motorcycles)

del motorcycles[-0] #del ko kucH aise likhte hae guyss
print(motorcycles)

     #removing 2 element from list
#del motorcycles[-2] #isko kuch aise bhi likh skte hae 
del motorcycles[1] # orr aise bhi likh skte hae
# LEKIN!!yae dono code mae sae ek time pae koi ek hi chalega


#removing an elements using the pop() Method.
'''index (optional) - The value at index is popped out and removed. 
If the index is not given, then the last element is popped out and removed.

Return: Returns The last value or the given index value from the list.
Exception: Raises IndexError When the index is out of range.'''
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#- --- -- --- - ---- - -- ----- ---- - -- - ---- - - - - -

motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
print (f"The last motorcycle i owned was a {last_owned.title()}.") 
'''isko mae aise isliye likh rha huu kyuki,dekh Ex-3.3 mae jaise kra hae naa baar barr print or statement 
yae sab likhna vo idhar nhi hoo rha direct apan print krwa skte hae.'''

'''isko mae aise bhi likh skta huu
        motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
storage = f"The last motorcycle i owned was a {last_owned.title()}."   
print(storage)  ''' 
#LEKIN uppar wala shi hae abhi yae toh bas samajne kae liye likha hae


