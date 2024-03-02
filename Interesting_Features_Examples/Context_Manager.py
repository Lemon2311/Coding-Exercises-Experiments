# Using a context manager to open and close a file
with open('example.txt', 'w') as f:
    f.write('Hello, world!')
#f.close() is not used anymore as the file is automatically closed after the with block
# The file is automatically closed after the with block
