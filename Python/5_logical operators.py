# Logical Operators =  evaluate multiple conditions and return a boolean value (True or False) based on the evaluation.
#                or = True if at least one of the conditions is True
#               and = True if all conditions are True
#               not = Inverts the condition (not False, not True)

temp = 25
is_raining =  False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled")

temp = -5
is_sunny = False
if temp > 28 and is_sunny:
    print("It is HOT outside.")
    print("It is Sunny.")
elif temp <= 0 and is_sunny:
    print("It is COLD outside.")
    print("It is Sunny.")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside.")
    print("It is Sunny.")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside.")
    print("It is Cloudy.")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside.")
    print("It is Cloudy.")
