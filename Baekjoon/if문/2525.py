hour, minute = map(int, input().split())
cookTime = int(input())

totalMinute = hour * 60 + minute
totalMinute += cookTime

if totalMinute >= 24 * 60 :
    totalMinute = totalMinute - 24 * 60

hour = totalMinute // 60
minute = totalMinute % 60

print(str(hour) + " " + str(minute))