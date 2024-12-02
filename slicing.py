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

b = "Hello, World!"
print(b[-5:-2])