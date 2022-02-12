# to-do-cli-app
A simple to-do list application that can be run on command line interface. This was created for the GDC engineering fellowship program.
## Getting started

1. Install Python: Python is usually installed by default on most modern systems. To check what your currently have, open a terminal and run the following command:

   ```
   python3 --version
   ```

   This should output some information on the installed Python version.
   You can also install python by following these instructions: https://installpython3.com/
2. Change directory to the location where the file is stored.
3. Run task.py on terminal with the instruction task.py python.
4. 3. Once you are done with the changes you should be able to execute the task app by running the following command from the terminal.

   **On Windows:**

   ```
   .\task.bat
   ```

   **On \*nix:**

   ```
   ./task.sh
   ```
1. The app can be run in the console with `./task`.

2. The app can read from and write to a task.txt text file. Each task occupies a single line in this file. Each line in the file should be in this format :

   ```
   p task
   ```

   where `p` is the priority ( priority will be a number) and `task` is the task description.

   > Priority denotes how important a task is, if it is a high priority task, it should be completed earlier. Priority is denoted using an integer, the lower the number, the higher the priority.

   Here is an example file that has 2 items.

   ```
   1 Buy milk
   2 Complete the project
   ```

3. Completed task are writted to a completed.txt file. Each task occupies a single line in this file. Each line in the file should be in this format :

   ```
   task
   ```

   where task is the task description.

   Here is an example file that has 2 items.

   ```
   Buy milk
   Complete the project
   ```

4. Priority can be any integer _greater than_ or _equal to_ 0. 0 being the highest priority

5. If two task have the same priority, the task that was added first is displayed first.

   The application opens the files task.txt and completed.txt from where the app is run, and not where the app is located. 

6. The files is always sorted in order of the priority, ie, the task with the highest priority should be first item in the file.

## Usage

### 1. Help

Executing the command without any arguments, or with a single argument help prints the CLI usage.

```
$ ./task help
Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
```

### 2. List all pending items

Use the ls command to see all the items that are not yet complete, in ascending order of priority.

Every item is printed on a new line. with the following format

```
[index] [task] [priority]
```

Example:

```
$ ./task ls
1. change light bulb [2]
2. water the plants [5]
```

index starts from 1, this is used to identify a particular task to complete or delete it.

### 3. Add a new item

Use the add command. The text of the task is enclosed within double quotes (otherwise only the first word is considered as the item text, and the remaining words are treated as different arguments).

```
$ ./task add 5 "the thing i need to do"
Added task: "the thing i need to do" with priority 5
```

### 4. Delete an item

Use the del command to remove an item by its index.

```
$ ./task del 3
Deleted item with index 3
```

Attempting to delete a non-existent item displays an error message.

```
$ ./task del 5
Error: item with index 5 does not exist. Nothing deleted.
```

### 5. Mark a task as completed

Use the done command to mark an item as completed by its index.

```
$ ./task done 1
Marked item as done.
```

Attempting to mark a non-existed item as completed will display an error message.

```
$ ./task done 5
Error: no incomplete item with index 5 exists.
```

### 6. Generate a report

Show the number of complete and incomplete items in the list. and the complete and incomplete items grouped together.

```
$ ./task report
Pending : 2
1. this is a pending task [1]
2. this is a pending task with priority [4]

Completed : 3
1. completed task
2. another completed task
3. yet another completed task
```
