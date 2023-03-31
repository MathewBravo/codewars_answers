import re

def alphanumeric(password) -> bool:
    # if len(password.split()) > 1:
    #     return False
    if password.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    print(alphanumeric( "hello world_" ))
    print(alphanumeric("PassW0rd"))
    print(alphanumeric("  "))
