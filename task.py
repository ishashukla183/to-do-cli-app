

# -*- coding: utf-8 -*-
import sys
import os.path



dict = {}
def readtasks():
    global dict
    if os.path.isfile('task.txt'):	
        with open("task.txt", 'r') as task_f :
                lines = task_f.readlines()
                for line in lines:
                        line.strip()
                        if line:
                            same_pr_tasks = []
                            task = line[2:]
                            priority = line[0:1]
                            if priority in dict :
                               same_pr_tasks = dict.get(priority)
                               same_pr_tasks.append(task)
                               dict.update({priority : same_pr_tasks})
                            else:
                                same_pr_tasks.append(task)
                                dict.update({priority : same_pr_tasks})    
def help():
   taskHelp = """
$ ./task help
Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
"""
   sys.stdout.buffer.write(taskHelp.encode('utf8'))
    
def list():
   if os.path.isfile('task.txt'):		
       index = 1
       
       tasks=""
       with open("task.txt",'r') as taskf :
	       data = taskf.readlines()
	       
           
       for line in data:
	       line.strip()
	       task = line[2:].strip()
	       priority = line[0].strip('\n')
	       tasks+="{}. {} [{}]\n".format(index, task, priority)
	       index+=1
           
       sys.stdout.buffer.write(tasks.encode('utf8'))		
   else:
	   sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))
        
            

def add(priority, task):
    global dict
    readtasks()
    same_pr_tasks = []
    if str(priority) in dict :
       same_pr_tasks = dict.get(priority)
       same_pr_tasks.append(task)
       dict.update({priority : same_pr_tasks})
    else:
        same_pr_tasks.append(task)
        dict.update({priority : same_pr_tasks})
    dict = sorted(dict.items())
    dict = {k:v for k, v in dict }
    with open("task.txt", 'w') as task_f :
       for item in dict.items():
           priority_item = str(item[0]).strip()
           for eachtask in item[1]:
             task_item = str(eachtask).strip()  
             tasktodo = "{} {}".format(priority_item, task_item)
             task_f.write(tasktodo+'\n')
    print('Added task: "{}" with priority {}'.format(task, priority))
def report():
    counttask=0
    countcompl=0
    if os.path.isfile('task.txt'):
   	    with open("task.txt",'r') as taskf:
   	    	tasks=taskf.readlines()
   	    counttask=len(tasks)
    st= "Pending : " + str(counttask)
    sys.stdout.buffer.write(st.encode('utf8'))
    if os.path.isfile('task.txt'):		
        index = 1
        tasks=""
        with open("task.txt",'r') as taskf :
 	       data = taskf.readlines()
 	        
        for line in data:
 	       line.strip()
 	       task = line[2:].strip()
 	       priority = line[0].strip('\n')
 	       tasks+="\n{}. {} [{}]".format(index, task, priority)
 	       index+=1
            
        sys.stdout.buffer.write(tasks.encode('utf8'))		
    	   
              
    if os.path.isfile('completed.txt'):
    	 with open("completed.txt",'r') as complf:
    	    doneData=complf.readlines()
    	    countcompl=len(doneData)
    print("\nCompleted : "+ str(countcompl), end = " ")
    
    if os.path.isfile('completed.txt'):
    	index = 1
    	tasks=""
    	with open("completed.txt",'r') as complf :
 	       data = complf.readlines()
 	       data.reverse() 
    	for line in data:
 	       task = line.strip()
 	       tasks+="\n{}. {}".format(index, task)
 	       index+=1
            
    	sys.stdout.buffer.write(tasks.encode('utf8'))   

def delete(num):
    if os.path.isfile('task.txt'):
	    with open("task.txt",'r') as taskf:
	    	data=taskf.readlines()
	    count=len(data)
	    if num>count or num<=0:
	    	print("Error: task with index #{} does not exist. Nothing deleted.".format(num))
	    else:
	    	with open("task.txt",'w') as taskf:
	    		for line in data:
	    			if count!=num:
	    				taskf.write(line)
	    			count-=1
	    	print("Deleted task #{}".format(num))
    else:
	    print("Error: task with index #{} does not exist. Nothing deleted.".format(num))

def done(num):
    if os.path.isfile('task.txt'):
	    with open("task.txt",'r') as taskfile:
	    	taskitems=taskfile.readlines()
	    count=len(taskitems)
	    if num>count or num<=0:
	    	print("Error: no incomplete item with index #{} exists.".format(num))
	    else:
	    	with open("task.txt",'w') as taskfile:
	    		if os.path.isfile('completed.txt'):						# Produces output according to the availability of done.txt file.
	    			with open("completed.txt",'a') as complfile:
			    		for line in taskitems:
			    			if count==num:
			    				complfile.write(line[2:])
			    			else:
			    				taskfile.write(line)
			    			count-=1
			    		
	    		else:
		    		with open("completed.txt",'w') as complfile:
			    		for line in taskitems:
			    			if count==num:
			    				complfile.write(line[2:])
			    			else:
			    				taskfile.write(line)
			    			count-=1

	    	print("Marked item as done.")
    else:
	    print("Error: no incomplete item with index #{} exists.".format(num))
def main(): 

	if len(sys.argv)==1:
		help()
	elif sys.argv[1]=='help':
		help()
	elif sys.argv[1]=='ls':
		list()
	elif sys.argv[1]=='add':
		if len(sys.argv)>2:
			add(sys.argv[2], sys.argv[3])
		else:
			print("Error: Missing tasks string. Nothing added!")
	elif sys.argv[1]=='del':
		if len(sys.argv)>2:
			delete(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for deleting tasks.")
	elif sys.argv[1]=='done':
		if len(sys.argv)>2:
			done(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for marking tasks as done.")
	elif sys.argv[1]=='report':
		report()
	else:
		print('Option Not Available. Please use "./task help" for Usage Information')

if __name__=="__main__": 
    main()