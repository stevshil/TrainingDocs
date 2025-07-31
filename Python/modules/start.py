import sys
# sys.path.append(".")
print(sys.path)
# import sayhello
from stevemods.sayhello import sayhello as sh
import stevemods.mymath as mymath

print(f"Now in {__name__}")    
print("This is the start of our script")
print(sh("Bonjourno","Steve"))
result=mymath.addnums([2,5,7,10,4])
print(result)