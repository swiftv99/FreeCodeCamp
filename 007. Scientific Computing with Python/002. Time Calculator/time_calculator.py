def add_time(start, duration, weekday='none'):
    start_day = start.split()
    start_hour = start_day[0].split(':')[0]
    start_minute = start_day[0].split(':')[1]
    am_pm = start_day[1]
    dur_hour = duration.split(':')[0]
    dur_minute = duration.split(':')[1]
    # print(start_hour + ':' + start_minute, am_pm, dur_hour + ':' + dur_minute)

    # integer
    temp_minute = int(start_minute) + int(dur_minute)
    temp_hour = int(start_hour) + int(dur_hour)
    result_minute = int(temp_minute % 60)
    total_hour = temp_hour + int(temp_minute // 60)
    partial_hour = total_hour % 12

    if am_pm == 'AM':
        days = total_hour // 24
    elif am_pm == 'PM':
        days = (total_hour + 12) // 24

    if am_pm == 'AM' and (total_hour // 12) % 2 == 1:
        am_pm = 'PM'
    elif am_pm == 'PM' and (total_hour // 12) % 2 == 1:
        am_pm = 'AM'
    # print(str(partial_hour) + ':' + str(result_minute), am_pm)

    week_days = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if weekday != 'none':
        weekday = weekday.capitalize()
        index_week = week_days.index(weekday)
        current_day = (days + index_week) % 7

    if partial_hour == 0:
        partial_hour = 12
    if result_minute < 10:
        result_minute = '0' + str(result_minute)

    if days == 0 and weekday == 'none':
        final_result = "{0}:{1} {2}".format(
            str(partial_hour), str(result_minute), am_pm)
    elif days == 0 and weekday != 'none':
        final_result = "{0}:{1} {2}, {3}".format(str(partial_hour), str(
            result_minute), am_pm, week_days[current_day])
    if days == 1 and weekday == 'none':
        final_result = "{0}:{1} {2} (next day)".format(
            str(partial_hour), str(result_minute), am_pm)
    elif days == 1 and weekday != 'none':
        final_result = "{0}:{1} {2}, {3} (next day)".format(str(partial_hour),
                                                            str(result_minute), am_pm, week_days[current_day])
    if days > 1 and weekday == 'none':
        final_result = "{0}:{1} {2} ({3} days later)".format(
            str(partial_hour), str(result_minute), am_pm, days)
    elif days > 1 and weekday != 'none':
        final_result = "{0}:{1} {2}, {3} ({4} days later)".format(
            str(partial_hour), str(result_minute), am_pm, week_days[current_day], days)
    return final_result


# add_time("3:30 PM", "2:12")
# add_time("11:55 AM", "3:12")
# add_time("9:15 PM", "5:30")
# add_time("11:40 AM", "0:25")
# add_time("2:59 AM", "24:00")
# add_time("11:59 PM", "24:05")
# add_time("8:16 PM", "466:02")
# add_time("5:01 AM", "0:00")
# add_time("3:30 PM", "2:12", "Monday")
# add_time("2:59 AM", "24:00", "saturDay")
# add_time("11:59 PM", "24:05", "Wednesday")
# print(add_time("8:16 PM", "466:02", "tuesday"))
