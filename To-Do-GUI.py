from tkinter import *

root = Tk()
root.title("Task Destroyer 9001")
root.geometry("720x300")

def addItem():
    input_text = taskEntry.get()  #getting the text from the text box input
    taskBox.insert('end',input_text)   #inserting the text input variable in the listbox
    #PUT LOGIC FOR ADDING ITEM FROM 'taskEntry' TO MASTER TASK LIST
    taskEntry.delete(0, 'end')      # Destroys text inside taskEntry
    print("item added")

def deleteItem():
    #PUT LOGIC FOR DELETING SELECTED TASK FROM MASTER TASK LIST
    print("item deleted")

def deleteAll():
    #PUT LOGIC FOR DELETING THE LIST
    print("list cleared")



# Create and Layout Frames
leftFrame = Frame(root, width=350, height=300, bg="cyan", pady=100, padx=50)
rightFrame = Frame(root, width=350, height=300, bg="blue")

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

leftFrame.grid(row=0, column=0, sticky="nsew")
rightFrame.grid(row=0, column=1, sticky="nsew")

# Create Label Widgets
enterTaskLabel = Label(leftFrame, text="Enter New Task")
blankLabelPad = Label(leftFrame, text="", width=5)

# Create Entry Widgets
taskEntry = Entry(leftFrame, width=30)

# Create Button Widgets
addItemButton = Button(leftFrame, text="ADD>>", command=addItem, padx=20)
deleteItemButton = Button(leftFrame, text="Delete", command=deleteItem, width=10)
deleteAllButton = Button(leftFrame, text="Delete All", command=deleteAll, width=10)
exitAppButton = Button(leftFrame, text="Quit", command=root.destroy, width=10, fg="red")

# Create ListBox Widget
taskBox = Listbox(rightFrame, height=30,width=30)

# Put Widgets on screen
enterTaskLabel.grid(row=1, column=1, columnspan=2, sticky=W)
taskEntry.grid(row=3, column=1, sticky=W)
blankLabelPad.grid(row=3, column=2)
addItemButton.grid(row=3, column=4, sticky=E)
deleteItemButton.grid(row=4, column=1, sticky=W)
deleteAllButton.grid(row=5, column=1, sticky=W)
exitAppButton.grid(row=6, column=1, sticky=W)
taskBox.grid(row=2,column=1,sticky=W)
root.mainloop()
