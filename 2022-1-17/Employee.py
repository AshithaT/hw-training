from datetime import datetime
import json

task1=[]

class Employee:
     def __init__(self, emp_name, emp_id):
         self.emp_name = emp_name
         self.emp_id = emp_id

     def login_time(self):
         return datetime.now().strftime("%Y-%m-%d %H:%M")

     def logout_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

     def start_task(self,task_title , task_description):
        return task_title,task_description

     def end_task(self,task_success):
        return task_success

     def start_time(self):
         
        return datetime.now().strftime("%Y-%m-%d %H:%M")

     def end_time(self):
         return datetime.now().strftime("%Y-%m-%d %H:%M")

def main():

    emp_id=int(input("Enter the id \n"))
    emp_name=input("Enter the name \n")
    emp_detail=Employee(emp_name,emp_id)
    login_time=emp_detail.login_time()
    task=taskdetail(emp_name,emp_id)

   
    details = {
                'name': emp_detail.emp_name,
                'emp_id':emp_detail.emp_id,
                'login_time': login_time,
                'logout_time':emp_detail.logout_time(),
                'task': task
        }
    details=json.dumps(details)
    print(details)
    with open(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+emp_detail.emp_name+'.json',"w") as fp:
            fp.write(json.dumps(json.loads(details),indent=4))


def taskdetail(emp_name,emp_id):
    while True:

        emp_detail=Employee(emp_name,emp_id)
        task_t1=input("Enter the task title \n")
        task_t2=input("Enter the task description \n")
        task_status=input("Enter the task status (True/False)\n")
        task_t1,task_t2=emp_detail.start_task(task_t1,task_t2)

        task={
        'task_title':task_t1,
        'task_description':task_t2,
        'start_time':emp_detail.start_time(),
        'end_time':emp_detail.end_time(),
        'task_status':emp_detail.end_task(task_status)
        }
        task1.append(task)
        val=input("Enter a new task?(yes/no) \n")
        if val!="yes":
            break

    return task1



if __name__=="__main__":
    main()