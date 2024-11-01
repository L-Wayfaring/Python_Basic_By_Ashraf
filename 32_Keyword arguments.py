# keyword arguments = an argument preceded by an identifier
#                     helps with readablity
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. keyword 4. arbiatary

def hello(greeting , title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello",title="Mr.",first="Spongebob",last="Squarepants")

print("1","2","3", sep="-") # here sep is a keyword for print function.
