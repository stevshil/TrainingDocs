def sayhello(greeting, name):
    return f"{greeting} {name}"

def addnums(listnums):
    sumnums = sum(listnums)
    return sumnums

print(f"Now in {__name__}")    
print("This is the start of our script")
print(sayhello("Bonjourno","Steve"))
result=addnums([2,5,7,10,4])
print(result)