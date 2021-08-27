from tkinter import *
from Assigment9_part_1_2 import *

def enter_button():
    costumer=Rates(firstname_text.get(),lastname_entry.get(),year_birth_entry.get(),current_year_entry.get())
    max_rate_text.set(costumer.maximum_heart_ate)
    min_rate_text.set(costumer.minimum_heart_ate)
# Create window object
app = Tk()



#part
firstname_text =StringVar()
firstname_lable = Label(app,text= "First Name",font=('bold',14),pady=20)
firstname_lable.grid(row=0 ,column=0,sticky=W)
firstname_entry = Entry(app,textvariable=firstname_text)
firstname_entry.grid(row=0 ,column=1)

#part
lastname_text =StringVar()
lastname_lable = Label(app,text= "Last Name",font=('bold',14),pady=20)
lastname_lable.grid(row=1 ,column=0,sticky=W)
lastname_entry = Entry(app,textvariable=lastname_text)
lastname_entry.grid(row=1 ,column=1)


#part
year_birth_text =StringVar()
year_birth_lable = Label(app,text= "Year of birth",font=('bold',14),pady=20)
year_birth_lable.grid(row=0 ,column=3,sticky=W)
year_birth_entry = Entry(app,textvariable=year_birth_text)
year_birth_entry.grid(row=0 ,column=4)

#part
current_year_text =StringVar()
current_year_lable = Label(app,text= "Current year",font=('bold',14),pady=20)
current_year_lable.grid(row=1 ,column=3,sticky=W)
current_year_entry = Entry(app,textvariable=current_year_text)
current_year_entry.grid(row=1 ,column=4)

#part
max_rate_text =StringVar()
max_rate_lable = Label(app,text= "Maximum Rate",font=('bold',14),pady=20)
max_rate_lable.grid(row=4 ,column=0,sticky=W)
max_rate_entry = Entry(app,textvariable=max_rate_text)
max_rate_entry.grid(row=4 ,column=1)

min_rate_text =StringVar()
min_rate_lable = Label(app,text= "Minimum Rate",font=('bold',14),pady=0)
min_rate_lable.grid(row=5 ,column=0,sticky=W)
min_rate_entry = Entry(app,textvariable=min_rate_text)
min_rate_entry.grid(row=5 ,column=1)



#Buttons
add_btn = Button(app,text='Enter',width=30,command=enter_button)
add_btn.grid(row=2,column=2,columnspan=2,pady=20)
# add_bon =Button(app,text ='Enter',width=12,command=)

part_list = Listbox(app, height=8 , width=50)




app.title('Heart Beat Rate')
app.geometry('700x350')

# Start program
app.mainloop()
