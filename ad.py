# String Concatenation
str1 = "Greetings"
str2 = "Everyone"
result = str1 + "!" + str2
print(result)

# String Repetition:
str1 = "Code"
result = str1 * 4
print(result)

# String Length
str1 = "Hello, World!"
length = len(str1)
print(length)

# String Indexing and Slicing
str1 = "Substring Example"
substring = str1[5:10]
print(substring)

# String Methods
# strip

str1 = "   Amazing   "
result = str1.strip()
print(result)

# Replace 

str1 = "Stay focused"
result = str1.replace("focused", "determined")
print(result)

# Split

str1 = "apple,grape,watermelon"
result = str1.split(",")
print(result)

# find

str1 = "Welcome to Python"
index = str1.find("Python")
print(index)

# String joining

words = ["Good", "morning", "to", "you"]
result = " ".join(words)
print(result)
