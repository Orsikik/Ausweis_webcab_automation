from time import gmtime, strftime, time

time_now = strftime("%Y-%m-%d %H:%M", gmtime(time() + 10800))
time_plus_2_minutes = strftime("%Y-%m-%d %H:%M", gmtime(time() + 10920))
time_plus_4_minutes = strftime("%Y-%m-%d %H:%M", gmtime(time() + 11040))
time_plus_5_minutes = strftime("%Y-%m-%d %H:%M", gmtime(time() + 11100))
current_hour = strftime("%H", gmtime(time() + 10800))
current_minute = strftime("%M", gmtime(time() + 10800))
current_minute_plus = strftime("%M", gmtime(time() + 11100))

current_r_minute = list(current_minute[0])
if int(list(current_minute)[1]) < 5:
    current_r_minute.append(0)
elif int(list(current_minute)[1]) >= 5:
    current_r_minute.append(5)
current_round_minute = int("".join(map(str, current_r_minute)))
if current_minute == 55:
    current_round_minute_plus = int("".join(map(str, current_r_minute))) -50
else:
    current_round_minute_plus = int("".join(map(str, current_r_minute))) +10


print(current_round_minute)
print(current_round_minute_plus)
print(time_plus_2_minutes)
print(time_plus_4_minutes)
print(time_plus_5_minutes)



