from datetime import datetime
import json
import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient() 
db=client.employee
result = db.emp.create_index([('emp_id', pymongo.ASCENDING)],
                                  unique=True)
task1=[]

class employ():
    

    def __init__(self, emp_id, emp_name):
        self.emp_id=emp_id
        self.emp_name=emp_name

    def login(self):
        self.login_time=datetime.now().strftime("%Y-%m-%d %H:%M")
        return

    def add_task(self,task_title , task_description):
        self.task={
        'task_title':task_title,
        'task_description':task_description,
        'start_time': datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        return

    def end_task(self,task_success):
        self.task.update(end_time = datetime.now().strftime("%Y-%m-%d %H:%M"), task_status=task_success)
        task1.append(self.task)
        self.task=0
        return task1
    
    def logout(self):
        
        details = {
            'name': self.emp_name,
            'emp_id':self.emp_id,
            'login_time': self.login_time,
            'logout_time':datetime.now().strftime("%Y-%m-%d %H:%M"),
            'task': task1

        }
        try:
            post=db.emp.insert_one(details)
        except : 
            print("Duplicate key error")
            
        
    def show_task(self,emp_id):
        
        pprint.pprint(db.emp.find_one({"emp_id": emp_id}))  
       
        
        # details=json.dumps(details)
        # print(details)
        # with open(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+self.emp_name+'.json',"w") as fp:
        #    fp.write(json.dumps(json.loads(details),indent=4))
