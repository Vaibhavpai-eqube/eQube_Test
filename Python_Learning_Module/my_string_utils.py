sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)
sentence1 = 'The quick brown fox jumps over the lazy dog'
print(sentence1)
#both sentences are the same, but they are defined using different types of quotes.
sentence2 = """The quick brown fox jumps over the lazy dog"""
print(sentence2)
# triple quotes can be used for multi-line strings
sentence3 = '''The quick brown fox jumps over the lazy dog'''
print(sentence3)

# string as array
# strings are arrays of bytes representing unicode characters
# you can access the characters in a string using indexing
string = "Hello, World!"
print(string[0])  # H
print(string[7])  # W
# you can also use negative indexing
print(string[-1])  # !, negative indexing starts from right hand side
print(string[-2])  # d


# looping in strings
fruit = "APPLE"
for letter in fruit:
    print("letter = " + letter)

# string length
name = "eQube"
print("Length of name:", len(name))

#Check String
#To check if a certain phrase or character is present in a string, 
# we can use the keyword in.
office = "eQube has their office in Indiranagar"
print("Bengaluru" in office)  # false
print("Indiranagar" in office)  # true
print("Bengaluru" not in office)  # true

# slicing strings
print(office[0:5])  # eQube
print(office[6:11])  # has
print(office[12:])  # their office in Indiranagar, slicing to the end of the string
print(office[:6])  # eQube, slicing from the beginning of the string
print(office[-10:])  # Indiranagar, slicing from the end of the string
print(office[-10:-1])  # Indiranaga, slicing from the end of the string

# modify string

# to uppercase
name = "eQube"
print(name.upper())  # EQUBE

# to lowercase
print(name.lower())  # eqube

# removing whitespaces
name_with_spaces = "   eQube   "
print(name_with_spaces.strip())  # eQube, removes leading and trailing whitespaces

# replace string
print(name.replace("eQube", "eQube Systems"))  # eQube Systems

# split string
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.split())  # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(sentence[2])
split_sentence = sentence.split();
print(split_sentence[2])  # brown, accessing the third word in the sentence

# String Format
"""
In python we cannot append string directly with numbers. we have to use Fstring formatting or casting to convert the number to a string.
age = 36
txt = "My name is John, I am " + str(age)
print(txt)
"""
age = 23;
txt =  f"Age is: {age}"
print(txt)  # Age is: 23

# adding decimals in number
price = 49
text = f"Price of Poha per plate is: {price:.3f}"
print(text)  # Price of Poha per plate is: 49.000