def sayhello(greeting, name):
    return f"{greeting} {name}"

def saygoodbye(greeting, name):
    return f"{greeting} {name}"

if __name__ == "__main__":
    print("Say hello from say hello")
    print(f"Now in {__name__}")
    print(sayhello("Gutten Tag", "Jack"))