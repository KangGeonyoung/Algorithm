def drawStar(n) :
    if n == 1 :
        return ['*']
    
    stars = drawStar(n//3)
    L = []

    for star in stars :
        L.append(star * 3)
    
    for star in stars :
        L.append(star + ' ' * (n//3) + star)

    for star in stars :
        L.append(star * 3)

    return L

N = int(input())
print('\n'.join(drawStar(N)))
    