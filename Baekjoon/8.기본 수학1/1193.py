input = int(input())
X = 0
Y = 0

def calculator(input) :
    x = 1
    y = 1
    direct = True
    count = 1

    while count < input :

        # direct = True = right 일 때
        if direct :
            x += -1
            y += 1
            
            if x == 0 :
                x = 1
                direct = not direct
                count += 1
                continue

            if y == 0 :
                y = 1
                direct = not direct
                count += 1
                continue

            count += 1

        # direct = False = left 일 때
        else :
            x += 1
            y += -1

            if x == 0 :
                x = 1
                direct = not direct
                count += 1
                continue

            if y == 0 :
                y = 1
                direct = not direct
                count += 1
                continue

            count += 1

    return x, y

X, Y = calculator(input)
print(f"{X}/{Y}")