# 0 <= quarters < 1000
quarters = int(input())

# three slot machines
machine1_played = int(input())
machine2_played = int(input())
machine3_played = int(input())
''' each play costs 1 quarter 
machine1 pay 30,  every 35times
machine2 pay 60,  every 100times
machine3 pay 9, every 10times 
'''

play_times = 0
machine = 0

while quarters > 0:
    quarters = quarters - 1
    play_times += 1

    if machine == 0:
        machine1_played += 1
        if machine1_played == 35:
            quarters = quarters + 30
            machine1_played = 0

    elif machine == 1:
        machine2_played += 1
        if machine2_played == 100:
            quarters = quarters + 60
            machine2_played = 0

    elif machine == 2:
        machine3_played += 1
        if machine3_played == 10:
            quarters = quarters + 9
            machine3_played = 0

    machine = machine + 1
    if machine == 3:
        machine = 0

print('Martha plays', play_times, 'times before going broke.')

