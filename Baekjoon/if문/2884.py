from xml.dom import minicompat

hour, minute = map(int, input().split())

totalMinute = hour * 60 + minute
totalMinute -= 45

if totalMinute < 0:
    totalMinute = 24 * 60 + totalMinute

hour = totalMinute // 60
minute = totalMinute % 60

print(str(hour) + " " + str(minute))