"""

project_1.py: první projekt do Engeto Online Python Akademie

author: Erik Stojaspal

email: erast@seznam.cz

discord: erastxxi
"""
# NABÍDKA TEXTŮ

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# UŽIVATELÉ

users = {"bob": "123", 
            "ann": "pass123", 
            "mike": "password123",
            "liz": "pas123"}

# ČÁRA OKRAJE =================================

line = "=" * 55

# UVÍTÁNÍ

print(f"{line}\nTEXT ANALYZER - APP\n{line}")

# ZADÁNÍ JMÉNA A HESLA
user = input("Enter a login name: ")
password = input("Enter your password: ")

# KONTROLA JMÉNA A HESLA

if users.get(user) == password:
    print(f"{line}\nWelcome to the app, {user} !!!") 
    print(f"We have 3 texts to be analyzed.\n{line}")    
else:
    print(f"{line}\nUnregistered user, terminating the program..\n{line}")                  
    quit()
    
# NABÍDKA TEXTU

for index,text in enumerate(TEXTS, 1):
    print(f"TEXT - {index}\n{text}")    
    
# VÝBĚR ČÍSLA TEXTU  

number_text = input(f"{line}\nEnter a number btw. 1 and 3 to select: ")
if number_text in ("1", "2", "3"):
    print(line)  
else:    
    print(f"{line}\nYou entered the wrong number, exit the program..\n{line}")
    quit()
    
# TVORBA OŘEZANÝCH SLOV

index_text = int(number_text) - 1
words = []
for index in TEXTS[index_text].split():
    word = index.strip(".,?!-")
    words.append(word)
    
# ANALÝZA SLOV

number_words = len(words)
titlecase_words = 0  
uppercase_words = 0 
lowercase_words = 0
numeric_strings = 0
sum_numbers = 0

for word in words:
    if word.istitle():
        titlecase_words += 1
    elif word.isupper():
        uppercase_words += 1 
    elif word.islower():
        lowercase_words += 1   
    elif word.isnumeric():
        numeric_strings += 1
        sum_numbers += int(word)    
       
print(
f"""There are {number_words} words in the selected text.
There are {titlecase_words} titlecase words.
There are {uppercase_words} uppercase words.
There are {lowercase_words} lowercase words.
There are {numeric_strings} numeric strings.
The sum of all the numbers {sum_numbers}
{line}"""
)

# PŘEVOD NA LEN

words_len = []     
for index in words:
    words_len.append(len(index))
        
# VYTVOŘENÍ SLOVNÍKU S LEN

occurence_word = {}

for word_number in words_len:
    if word_number not in occurence_word:
        occurence_word[word_number] = 1
    else:
        occurence_word[word_number] = occurence_word[word_number] + 1 
      
# VÝPIS LEN

print("LEN|" + "OCCURENCES".center(max(occurence_word.values())+2) + f"|NR\n{line}")
for i in range(1,(max(words_len)+1)):
    print(
         str(i).rjust(3) + "|" + 
         (occurence_word.get(i, 0) * ("*")).ljust(max(occurence_word.values())+2) + 
         "|" + str(occurence_word.get(i, 0))
         ) 
print(f"{line}\nEND TEXT ANALYZER - APP\n{line}")       



