def blank(n) :
    if n == 1 :
        print(" ", end='')
        return 0
    
    return blank(n/3)

def line() :
    print()
    return 0

def star(n) :
    if n == 1 :
        print("*", end='')
        return 0

    return star(n/3) + star(n/3) + star(n/3) + line() + star(n/3) + blank(n/3) + star(n/3) + line() + star(n/3) + star(n/3) + star(n/3)


print(star(9))