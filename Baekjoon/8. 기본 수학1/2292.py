N = int(input())
room = 1
count = 1

while N > room :
    room += count * 6
    count += 1

print(count)