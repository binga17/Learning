#slicing in python doesnot include the last position mentioned 

b = "Hello, World!"
print(b[2:5]) # position 5 is not included in the output

#slicing from the start

b = "Hello, World!"
print(b[:5]) #position 5 i not included in the output

#slice to the end

b = "Hello, World!"
print(b[2:])

#negative indexing
#negative slicing starts from -1. 
#-1 represents the last character of the sentence

b = "Hello, World!"
print(b[-5:-2]) #position -2 is not included in the output

