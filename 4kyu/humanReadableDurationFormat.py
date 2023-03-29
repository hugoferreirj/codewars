#Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
#
#The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
#It is much easier to understand with an example:
#
#* For seconds = 62, your function should return 
#    "1 minute and 2 seconds"
#* For seconds = 3662, your function should return
#    "1 hour, 1 minute and 2 seconds"
#For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
#Note that spaces are important.
#
#Detailed rules
#The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
#
#The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.
#
#A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
#
#Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
#
#A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
#
#A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
#
def addSIfPlural(value, measureOfTime):
    return measureOfTime + "s" if value > 1 else measureOfTime
    
def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        minutes = seconds // 60
        seconds %= 60
        result = []
        if seconds > 0:
            result.append(str(seconds) + " " + addSIfPlural(seconds, "second"))
        if minutes > 0:
            hours = minutes // 60
            minutes %= 60
            if minutes > 0:
                result.append(str(minutes) + " " + addSIfPlural(minutes, "minute"))
            if hours > 0:
                days = hours // 24
                hours %= 24
                if hours > 0:
                    result.append(str(hours) + " " + addSIfPlural(hours, "hour"))
                if days > 0:
                    years = days // 365
                    days %= 365
                    if days > 0:
                        result.append(str(days) + " " + addSIfPlural(days, "day"))
                    if years > 0:
                        result.append(str(years) + " " + addSIfPlural(years, "year"))
        result.reverse()
        if len(result) > 1:
            andLastPart = " and " + result.pop(-1)
            return ", ".join(result) + andLastPart
        return "".join(result)