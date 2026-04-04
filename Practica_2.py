def anagrama (a , b):
    a2 = a.lower()
    b2 = b.lower()
    if a2 == b2:
        return False
    elif sorted(a2) == sorted(b2):
        return True
    else:
        return False

print(anagrama("RoMA" , "AmoR"))