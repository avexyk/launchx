# Defino mi función
def rocket_parts():
    print('payload, propellant, structure')
    return 'payload, propellant, structure'

output = rocket_parts()
print(output)


def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


# from datetime import timedelta, datetime
# def arrival_time(hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime('Arrival: %A %H:%M')

from datetime import timedelta, datetime
def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')


def variable_length(*args):
    print(args)


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

sequence_time(4, 14, 18)


def variable_length(**kwargs):
    print(kwargs)


def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')


variable_length(tanks=1, day='Wednesday', pilots=3)


total_days = days_to_complete(238855, 75)
print(round(total_days))
# print(arrival_time())
# print(arrival_time(hours=0))
print(arrival_time('Moon'))
print(arrival_time('Orbit', hours=0.13))

