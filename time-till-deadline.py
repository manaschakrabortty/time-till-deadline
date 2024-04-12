#PROJECT -- COUNTDOWN APP

'''EXERSISE-
-> ACCEPT USER INPUT OG GOAL AND A DEADLINE
->PRINT BACK:
    HOW MUCH TIME REMAINS UNTIL THAT DEADLINE

#USE DATE TIME MODULE FOR CAL...

ex-learn python:10.02.2002

'''
# import datetime

# user_input=input("enter ur goal with a deadline separated by colo:--> ")
# input_list=user_input.split(":")

# goal=input_list[0]
# deadline=input_list[1]
# deadline_date=datetime.datetime.strptime(deadline, "%d.%m.%Y")
# #calculation how many days from now till deadline
# today_date=datetime.datetime.today()
# time_till=deadline_date-today_date
# # print(f"Dear User! Time Remaining for your goal:{goal} is {time_till.days} days")
# hours_till=int(time_till.total_seconds() / 60 / 60)
# print(f"Dear User! Time Remaining for your goal:{goal} is {hours_till} hours")



from datetime import datetime

user_input=input("enter ur goal with a deadline separated by colo:--> ")
input_list=user_input.split(":")

goal=input_list[0]
deadline=input_list[1]
deadline_date=datetime.strptime(deadline, "%d.%m.%Y")
#calculation how many days from now till deadline
today_date=datetime.today()
time_till=deadline_date-today_date
# print(f"Dear User! Time Remaining for your goal:{goal} is {time_till.days} days")
hours_till=int(time_till.total_seconds() / 60 / 60)
print(f"Dear User! Time Remaining for your goal:{goal} is {hours_till} hours")



