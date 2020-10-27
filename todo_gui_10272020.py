from tkinter import *

OPTIONS = [
    "Hard",
    "Medium",
    "Easy",
    ]

bgColor = ["#0A1B2E", "#77A0A9", "#6F7D8C"]  # Blue shades
difficultyColor = ["#FF4242", "#FFC857", "#4DAA57"]  # Red, Yellow, Green

root = Tk()
root.title("Task Destroyer 9001")
root.geometry("1100x500")

# Instantiate an empty master task list
task_items = []
task_descriptions = []
task_priorities = []

# String Variable for difficulty dropdown
v = StringVar(root)
v.set(OPTIONS[0])


def addItem():
    input_text = taskEntry.get()  # Getting the text from the text box input
    input_description = taskBody.get("1.0", 'end')
    input_priority = v.get()
    task_items.append(input_text)  # Appends new item to master task list
    task_descriptions.append(input_description.rstrip("\n"))
    task_priorities.append(input_priority)
    taskBox.insert('end', input_text[0:20].upper() + "... //Priority: "
                   + input_priority)  # Insert the text variable in the listbox
    taskEntry.delete(0, 'end')  # Destroys text inside taskEntry
    taskBody.delete("1.0", 'end')

    print("\nitem added")
    print("Current items in task_items:", task_items)
    print("Current items in task_descriptions:", task_descriptions)
    print("Current items in task_priorities:", task_priorities)


def deleteItem():
    selectedItem = taskBox.curselection()
    taskBox.delete(selectedItem)
    item_index = ''.join(str(x) for x in selectedItem)  # tuple->string
    task_items.pop(int(item_index))
    task_descriptions.pop(int(item_index))
    task_priorities.pop(int(item_index))

    print("\nitem deleted", selectedItem)
    print("Current items in task_items:", task_items)
    print("Current items in task_descriptions:", task_descriptions)
    print("Current items in task_priorities:", task_priorities)


def deleteAll():
    taskBox.delete(0, len(task_items))
    task_items.clear()
    task_descriptions.clear()
    task_priorities.clear()

    print("\nlist cleared")
    print("Current items in task_items:", task_items)
    print("Current items in task_descriptions:", task_descriptions)
    print("Current items in task_priorities:", task_priorities)


def taskDetails():
    taskDetailsFrame = Frame(root, width=350, height=300, pady=10,
                             bg=bgColor[2])
    taskDetailsFrame.grid(row=0, column=2, sticky=N)
    Label(taskDetailsFrame,
          text="Task Details",
          bg=bgColor[2],
          fg="white").grid(row=0, column=0, columnspan=2, sticky=NSEW)

    selectedItem = taskBox.curselection()
    item_index = ''.join(str(x) for x in selectedItem)

    Label(taskDetailsFrame,
          text="Task: " + task_items[int(item_index)],
          bg=bgColor[2],
          fg='white').grid(row=1, column=0, columnspan=2, sticky=W)
    Label(taskDetailsFrame,
          text="Priority:",
          bg=bgColor[2],
          fg='white').grid(row=2, column=0, sticky=W)
    task_priority = Label(taskDetailsFrame,
                          text=task_priorities[int(item_index)],
                          bg=bgColor[2], fg='white', width=20)
    if task_priorities[int(item_index)] == OPTIONS[0]:
        task_priority.config(bg=difficultyColor[0])
    elif task_priorities[int(item_index)] == OPTIONS[1]:
        task_priority.config(bg=difficultyColor[1])
    elif task_priorities[int(item_index)] == OPTIONS[2]:
        task_priority.config(bg=difficultyColor[2])
    else:
        task_priority.config(bg='white')
    task_priority.grid(row=2, column=1, sticky=W)

    task_description = Text(taskDetailsFrame, width=25, wrap=WORD, height=3,
                            bg=bgColor[2], fg='white')
    task_description.insert("1.0", str(task_descriptions[int(item_index)]))
    task_description.config(state=DISABLED)
    task_description.grid(row=3, column=0, columnspan=2)

    Button(taskDetailsFrame, text="Close Details Pane",
           command=taskDetailsFrame.destroy).grid(row=10)


# Create and Layout Frames
leftFrame = Frame(root, width=350, height=300, pady=10, padx=50, bg=bgColor[0])
rightFrame = Frame(root, width=350, height=300, bg=bgColor[0])

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
leftFrame.grid(row=0, column=0, sticky="nsew")
rightFrame.grid(row=0, column=1, sticky="nsew")

# Create Label Widgets
enterTaskLabel = Label(leftFrame, text="Task Name: ", bg=bgColor[0],
                       fg="white")
taskBodyLabel = Label(leftFrame, text="Task Body: ", bg=bgColor[0], fg="white")
priorityLabel = Label(leftFrame, text="Task Priority: ", bg=bgColor[0],
                      fg="white")
blankLabelPad = Label(leftFrame, text="", width=5, bg=bgColor[0])
blankLabelPad2 = Label(leftFrame, text="", width=5, bg=bgColor[0])
blankLabelPad3 = Label(leftFrame, text="", width=5, bg=bgColor[0])
taskBoxLabel = Label(rightFrame, text="Tasks", width=39, height=2,
                     bg=bgColor[2], fg="white")

# Create Entry Widgets
taskEntry = Entry(leftFrame, width=67)
taskBody = Text(leftFrame, width=50, height=10)

# Create Dropdown for Priorities
priorityMenu = OptionMenu(leftFrame, v, *OPTIONS)
priorityMenu.config(width=10, pady=15)

# Create Button Widgets
addItemButton = Button(leftFrame, text="ADD TASK", command=addItem, width=56)
deleteItemButton = Button(rightFrame, text="Delete Selected Task",
                          command=deleteItem, width=38, pady=5)
deleteAllButton = Button(rightFrame, text="Delete All", command=deleteAll,
                         width=38, pady=5)
exitAppButton = Button(leftFrame, text="Quit", command=root.destroy, width=10,
                       fg="red")
viewTaskButton = Button(rightFrame, text="View Task", command=taskDetails,
                        width=38, pady=10)

# Create ListBox Widget
taskBox = Listbox(rightFrame, height=10, width=45, selectbackground=bgColor[1])

# Put Widgets on screen
enterTaskLabel.grid(row=1, column=0, sticky=W)
taskEntry.grid(row=1, column=1, sticky=W)
blankLabelPad.grid(row=2)
taskBodyLabel.grid(row=3, column=0, sticky=NW)
taskBody.grid(row=3, column=1, sticky=W)

blankLabelPad3.grid(row=4)

priorityLabel.grid(row=5, column=0, sticky=W)
priorityMenu.grid(row=5, column=1, sticky=W)

blankLabelPad2.grid(row=6)

addItemButton.grid(row=10, column=1, sticky=N)
deleteItemButton.grid(row=4, column=1, sticky=N)
deleteAllButton.grid(row=5, column=1, sticky=N)
viewTaskButton.grid(row=6, column=1, sticky=N)
exitAppButton.grid(row=11, column=1, sticky=S)

taskBoxLabel.grid(row=1, column=1, sticky=S)
taskBox.grid(row=2, column=1, sticky=NS)

root.mainloop()
