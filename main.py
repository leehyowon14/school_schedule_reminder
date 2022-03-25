import schedule
from win10toast import ToastNotifier
from time import sleep
from datetime import datetime
import json
with open('./config/schedule.json', "r", encoding='UTF8') as f:
    schedule_dict = json.load(f)
    

schedule_time  = schedule_dict["time"]

weekday_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

if len(schedule_dict["schedule"]) - 1 < datetime.now().weekday():
    print("오늘은 어떠한 스케줄도 없습니다.")
    exit()

subject_dict = schedule_dict["schedule"][weekday_dict[datetime.now().weekday()]]

def reminder(subject):
    toaster = ToastNotifier()
    toaster.show_toast("'"+subject+"' 시간입니다.", "온라인 수업에 참석하여 주세요.", duration=10)
    return schedule.CancelJob

Class = 1
for key in schedule_time:
    schedule.every().day.at(schedule_time[key]).do(reminder, subject_dict[str(Class)])
    Class += 1

print("리마인더가 실행되었습니다.")

while True:
    schedule.run_pending()
    sleep(1)