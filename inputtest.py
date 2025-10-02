#program to evaluate the time an event will end given the start time and duration
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = dura + mins
hour = hour + mins // 60
mins %= 60
hour %= 24
print(hour, ":", mins, sep="")
