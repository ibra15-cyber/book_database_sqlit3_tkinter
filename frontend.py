from distutils import command
from tkinter import *
import backend

window=Tk()

def view_command():
    list1.delete(0, END) #a measure to block our view repeating after clicking the view all tab 
    for row in backend.view():
        list1.insert(END, row)

# view = backend.view() #this will be wrong bc it is expecting a fn and not a variable

def search_command():
    list1.delete(0, END)
    #for any entry passed in the search 
    #get that entry using the .get
    #pass that value into search
    #and search does its job ie using the Database command
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


#list1.curselection() returns (0,)
#list1.curselection()[0] returns only the 0
#this fn creates the list or tuple we need
#so when we pass it with an index, it returns the id
#so its like passing an id in the delete_command
def get_selected_row(event):
    #save the first item in the cur selection as index for ID
    index=list1.curselection()[0] #get the index 0 using the cursor
    # print(index)
    #passing the index into our get list
    global selected_tuple
    selected_tuple = list1.get(index) #this is getting a row ie everything in every line using the id
    print (selected_tuple)
    e1.delete(0,END) #delete everything in the entry
    e1.insert(END, selected_tuple[1]) #insert the second item in the tuple ie title
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    return selected_tuple

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    #insert takes 4 parameters so we use the selected tuple that returns the our items in tuple
    #then we get each using the index
    #but how did this happen without the fn the returns being ran 
    #i suspect its because its an event so its running
    # backend.update(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])
    #the above
    #but update also takes 5, ie with id which isnt going to be used here
    #but we still have to insert it to make up to the 5 input
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
 
#labels
l1=Label(window,text="Title")
l1.grid(row=0, column=0)

l2=Label(window,text="Author")
l2.grid(row=0, column=2)

l3=Label(window,text="Year")
l3.grid(row=1, column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1, column=2)

#entry
title_text = StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1, column=1)


isbn_text = StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1, column=3)

#list box
list1=Listbox(window, height=6, width=35 ) #we create a list
list1.grid(row=2, column=0, rowspan=7, columnspan=2) #we grid it

list1.bind('<<ListboxSelect>>', get_selected_row) #binding our list1 with listboxselector and row selector through a fn



#scrollbar
sb1=Scrollbar(window) #scrollbar obj
sb1.grid(row=3, column=2, rowspan=7) #grid it to appear where we want it

list1.configure(yscrollcommand=sb1.set) # add our scrollbar to the list created

sb1.configure(command=list1.yview) #configure sb1 to our list

#button
b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.wm_title("BookStore")
window.mainloop() #without this it will not show