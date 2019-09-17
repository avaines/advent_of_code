"""
task summary/notes
""" 

from datetime import datetime, timedelta
from collections import Counter
import re
import fileinput
puzzle_input = sorted(fileinput.input('day4/day4.txt'))

def part1():

    guards = list()
    last_guard_id = 0
    sleep_minutes = []
    mins_asleep = 0

    # for each entry in the list
    for i in puzzle_input:
        line = part1_split(i)


        if "Guard" in line['entry']:
            if last_guard_id != 0:
                guards.append(  {'id':last_guard_id, 'mins_asleep':mins_asleep, 'sleep_minutes':sleep_minutes} )
    
            current_guard_id=(re.search('\#(.*?)\ ',line['entry']).group()).replace('#',"")
            last_guard_id = current_guard_id
            
            sleep_minutes = []
            mins_asleep = 0
            last_wake_time = line['datetime']

        if "asleep" in line['entry']:
            last_sleep_time = line['datetime']
        
        if "wakes" in line['entry']:
            delta = line['datetime'] - last_sleep_time + timedelta(minutes=1)

            mins_asleep += divmod(delta.total_seconds(),60)[0] 
            last_wake_time = line['datetime']
            
            while(last_sleep_time < last_wake_time ):
                sleep_minutes.append( last_sleep_time.minute )
                last_sleep_time = last_sleep_time + timedelta(minutes=1)

    # catch the last guard
    guards.append(  {'id':last_guard_id, 'mins_asleep':mins_asleep, 'sleep_minutes':sleep_minutes} )

    # we now have all the facts but each guard that works 2 shifts is in the
    # guards list multiple times so merge them


    guards_condensed = dict()
    for g in guards:
        data = guards_condensed.get(g['id'], {'mins_asleep':0, 'sleep_minutes':[]} )
        data['mins_asleep'] += g['mins_asleep']
        data['sleep_minutes'].extend(g['sleep_minutes'])
        guards_condensed[g['id']] = data


    best_sleeper = 0
    # Find the guard who slept the most and return his ID multiplied by his most sleep minute
    for guard_sleep in guards_condensed:
        current_guard = guards_condensed[guard_sleep]
        if current_guard['mins_asleep'] != 0:
            sleepiest_minute = max(set(current_guard['sleep_minutes']), key = current_guard['sleep_minutes'].count)
            sleepiest_minute_occurences = (current_guard['sleep_minutes']).count(sleepiest_minute)


            if current_guard['mins_asleep'] > best_sleeper:
                best_sleeper = current_guard['mins_asleep']
                # print("Guard", guard_sleep, "slept for", best_sleeper, "mostly on minute", sleepiest_minute, "times:",sleepiest_minute_occurences, " | = ", int(guard_sleep) * int(sleepiest_minute) )
                part1="Guard " + str(guard_sleep) + "was asleep most on minutes " +  str(sleepiest_minute) + " = " + str(int(guard_sleep) * int(sleepiest_minute))


    best_sleep_minute = 0
    # Find the guard who slept the most on the same minute and return his ID multiplied by his most sleep minute
    for guard_sleep in guards_condensed:
        current_guard = guards_condensed[guard_sleep]
        if current_guard['mins_asleep'] != 0:
            sleepiest_minute = max(set(current_guard['sleep_minutes']), key = current_guard['sleep_minutes'].count)
            sleepiest_minute_occurences = (current_guard['sleep_minutes']).count(sleepiest_minute)


            if sleepiest_minute_occurences > best_sleep_minute:
                best_sleep_minute = sleepiest_minute_occurences
                part2="Guard " + str(guard_sleep) + "was asleep most on minutes " +  str(sleepiest_minute) + " = " + str(int(guard_sleep) * int(sleepiest_minute))

    



    return "part1: " + part1 + " | part2: " + part2


def part1_split(line):

    d = dict()

    # Get the datetime by using regex
    date_string = re.search('[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]', line).group()
    d['datetime'] = datetime.strptime(date_string, '%Y-%m-%d %H:%M')

    
    # Get the log entry by splitting on the end brace and a 'space', the log will be the second part
    # the emntry will have a \n on the end so strip that off too
    d['entry'] = (line.split("] ")[1]).strip()
    return(d)



print(part1())
# print(part2())