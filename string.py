a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#strings are arrays

a = "Hello World!"
print(a[1])

#looping through string

for x in "BIGYAN":
    print(x)

#string length (counts space as well)

a = "Bigyan Chandra Bashyal"
print(len(a))

#we can use keyword in to check if certain phrase or character is present

txt = "The best things in life are free!"
print("free" in txt)

#with if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#to check if not, then use not in command

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")