test = open('test.txt')
print(test.read())
print(test.read()) # shows nothing since cursor at the end of file
print(test.read()) # shows nothing since cursor at the end of the file
test.seek(0) # to return the cursor to the start of the file
print(test.read()) # Now we are able to print again.
test.seek(0) # to return the cursor to the start of the file
print(test.read())
test.seek(0)
print(test.readline())
print(test.readline())
print(test.readline())
test.seek(0)
print(test.readlines())
test.close()

with open('test.txt') as my_file: # no need to close
    print('using with:')
    print(my_file.read())