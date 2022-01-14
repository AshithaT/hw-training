import json
from datetime import datetime

class employeetrack:
  count=0
  def __init__(self, emp_id, emp_name, date, login_time, logout_time):
      self.emp_id=emp_id
      self.emp_name=emp_name
      self.date=date
      self.logintime=login_time
      self.logoutime=logoutime
      employeetrack.count+=1

  def time():
    today = date.today()
    print("Today's date:", today)

  def displayCount(self):
      print("The number of employees in the organization are: ", self.count)
  def logtask(self):
      data={
               
               "Enter emp_id": emp_id,
               "Enter emp_name":emp_name,
               "Enter date ":date,               
               "Enter login_time":login_time ,
               "Enter logout_time": logout_time,
               "Enter tasks":[
                        { "task 1 details" },
                        { "task 2 details"},
                        { "task 3 details" }]}
data = [{"emp_id": 1, "emp_name": "Ashitha", "date":"14-1-22" ,"login_time":"9:00","log_out":"6:00"},
        {"emp_id": 2, "emp_name": "Renin", "date":"14-1-22","login_time":"9:00","log_out":"6:00"}]
 
with open("filename.json", "w") as write_file:
    json.dump(data, write_file)
    
f = open('filename.json')
data = json.load(f)
for i in data [0]:
 print(i)
f.close()   
 




