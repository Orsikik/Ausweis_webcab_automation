from time import gmtime, strftime, time

time_now = strftime("%Y-%m-%d %H:%M", gmtime(time() + 10800))
time_plus_5_minutes = strftime("%Y-%m-%d %H:%M", gmtime(time() + 11100))
current_hour = strftime("%H", gmtime(time() + 10800))
current_minute = strftime("%M", gmtime(time() + 10800))
current_r_minute = list(current_minute[0])

if int(list(current_minute)[1]) < 5:
    current_r_minute.append(0)
elif int(list(current_minute)[1]) >= 5:
    current_r_minute.append(5)

current_round_minute = int("".join(map(str, current_r_minute)))

print(current_minute)
print(current_r_minute)
print(current_round_minute)



# print(current_minute)
