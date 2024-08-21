import tkinter as tk

from tkinter import *
from tkinter import Frame, Entry, Label, Button, LabelFrame, Canvas, Scrollbar, GROOVE, X, RIGHT

#from tkinter.ttk import Label

def close_window():
    obj.destroy()


# Maximize button function


obj = tk.Tk()
obj.title("Billing System")
obj.overrideredirect(True)

obj.geometry("1370x800")
# obj.iconbitmap('icon.ico')
headingLable = Label(obj
                     , text="Billing System",
                     font=('tine new roman', 25, "bold"),
                     bg="lightskyblue4",
                     fg='floral white',
                     bd=6,
                     relief="groove",
                     pady=5
                     )
# close button
close_button = Button(headingLable,
                      text="X",
                      font=25,
                      command=close_window,
                      bg="lightskyblue4",
                      fg="floral white",
                      bd=6
                      )
close_button.pack(side=tk.RIGHT)
# Maximize button
# maximize_button=Button(headingLable)

headingLable.pack(fill=X, pady=2)
customer_details_frame = LabelFrame(obj,
                                    text='Customer Details',
                                    font=('tine new roman', 15, "bold"),
                                    bg="lightskyblue4",
                                    fg='floral white',
                                    bd=6,
                                    relief="groove"
                                    )

# this is customer derails frame
customer_details_frame.pack(fill=X, pady=2)
# name label
nameLabel = Label(customer_details_frame,
                  text='Name',
                  font=('tine new roman', 15, "bold"),
                  bg="lightskyblue4",
                  fg='floral white'
                  )
nameLabel.grid(row=0, column=0, padx=25)
# Entery
nameEntery = Entry(customer_details_frame,
                   font=("arial", '15'),
                   bd='5',
                   width=15
                   )
nameEntery.grid(row=0, column=1, padx=10, pady=5)
# phone entry
manuLabel = Label(customer_details_frame,
                  text='Phone Number',
                  font=('tine new roman', 15, "bold"),
                  bg="lightskyblue4",
                  fg='floral white'
                  )
manuLabel.grid(row=0, column=2, padx=25)
manuEntery = Entry(customer_details_frame,
                   font=("arial", '15'),
                   bd='5',
                   width=15
                   )
manuEntery.grid(row=0, column=3, padx=10, pady=5)
# bill number entry
billLabel = Label(customer_details_frame,
                  text='bill Number',
                  font=('tine new roman', 15, "bold"),
                  bg="lightskyblue4",
                  fg='floral white'
                  )
billLabel.grid(row=0, column=4, padx=(170, 25))
billEntery = Entry(customer_details_frame,
                   font=("arial", '15'),
                   bd='5',
                   width=15
                   )
billEntery.grid(row=0, column=5, padx=10, pady=5)
# search button
searchButton = Button(customer_details_frame,
                      text="SEARCH",
                      font=("arial", 12, 'bold'),
                      bd=7
                      )
searchButton.grid(row=0, column=6, padx=25, pady=5)


# function-->scrolling of menu


# exercise
# create a scrollbar

class ListFrame(Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master=parent)
        self.pack(expand=True, fill="x")

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        # scrollregion( l,t,r,b)
        self.canvas = Canvas(self, background='white', scrollregion=(0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand=True, fill='x')

        # display frame
        self.frame = Frame(self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both',pady=0,padx=0)

        # scrollbar
        self.scrollbar = Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # events
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 40), "units"))
        self.bind('<Configure>', self.update_size)
        self.canvas.bind("<Enter>")
        self.canvas.bind("<Leave>")

    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>',
                                 lambda event: self.canvas.yview_scroll(-int(event.delta / 40), "units"))
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')
            self.scrollbar.place_forget()

        self.canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor='nw',
            width=self.winfo_width(),
            height=height)

    def create_item(self, index, item):
        frame = Frame(self.frame,
                      bg='lightskyblue4',
                      bd=4,
                      relief=GROOVE
                      )
        def increment_item(entry_widget):
            current_value = int(entry_widget.get() or 0)
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, str(current_value + 1))

        def decrement_item(entry_widget):
            current_value = int(entry_widget.get() or 0)
            if current_value > 0:
                entry_widget.delete(0, tk.END)
                entry_widget.insert(0, str(current_value - 1))




        # def on_entry_click(event):
        #
        #     if menuEntery.get() == text:
        #         menuEntery.delete(0, "end")  # delete all the text in the entry
        #         menuEntery.config(fg='black')
        #
        # def on_focusout(event):
        #
        #     if menuEntery.get() == "":
        #         menuEntery.insert(0, text)
        #         menuEntery.config(fg='grey')

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 1, 1), weight=1, uniform='a')

        # widgets
        menuLabel = Label(frame,
                          text=f'{item}',
                          font=('tine new roman', 10, "bold"),
                          bg="lightskyblue4",

                          )
        menuLabel.grid(row=index, column=0, padx=2, pady=2, sticky="w")

        menuEntery =Frame(frame,



                           width=6,
                           bg="lightskyblue4",
                           )
        menuEntry = Entry(frame,
                          width=4,
                          font=('times new roman', 10),
                          )
        menuEntry.grid(row=index, column=2, padx=0, pady=2)

        # Add and subtract buttons
        minusButton = Button(frame,
                             text='-',
                             bg="red",
                             command=lambda: decrement_item(menuEntry))
        minusButton.grid(row=index, column=1, padx=0, pady=8)

        addButton = Button(frame,
                           text="+",
                           command=lambda: increment_item(menuEntry))
        addButton.grid(row=index, column=3, padx=0, pady=8)
        # minusButton=Button(menuEntery,
        #                    text='-',
        #                    bg="red",
        #                    # fg="white"
        #                    )
        # minusButton.grid(row=0,column=0,padx=1,pady=8)
        # itemLabel=Entry(menuEntery,
        #                 width=4,
        #                 )
        # itemLabel.grid(row=0,column=1,padx=1,pady=0)
        # addButton = Button(menuEntery,
        #                    text="+",
        #                    command=lambda:
        #
        #                    )
        # addButton.grid(row=index, column=2, padx=1, pady=8)


        # text = "No.Of Items"
        # menuEntery.insert(0, text)
        # menuEntery.bind('<FocusIn>', on_entry_click)
        # menuEntery.bind('<FocusOut>', on_focusout)

       #menuEntery.grid(row=index, column=1, padx=1, pady=8)

        return frame


text_list_1 = ['Glouti Kebab', "Tunday Kebab", 'Korma', 'Nihari', 'Sheermal', "Kakori Kebab", 'Awadhi Biryani',
               'Murgha Musallam',
               'Mutton Korma', 'Kofta', 'Dum Biryani', 'Tandoori Roti', 'Roomali Roti', 'Buttar Roti', 'Sadi Roti']
text_list_2 = ['Classic CheeseBurger', 'Spicy Chicken Burger', 'Veggie Burger', 'Cheese Sandwich', 'Delight Sandwich',
               'Cheese Pizza',
               'Pepperoni Pizza', 'Meat Lover Pizza', 'French Fries', 'Onion Ring', 'Cheese Pasta']
# run

# FOOD LIST

foodManuframe = Frame(obj,
                      bd=3,
                      relief="groove",
                      bg='lightskyblue4',
                      height=40)

foodManuframe.pack(fill=X, pady=2)
FoodFrame = LabelFrame(foodManuframe,
                       text="Lucknowi Dishes",
                       font=("times new roman", 15, "bold"),
                       fg="white",
                       bd=5,
                       relief="groove",
                       bg='lightskyblue4',

                       )

FoodFrame.grid(row=0, column=0, padx=2)
FastFoodFrame = LabelFrame(foodManuframe,
                           text="Fast Food",
                           font=("times new roman", 15, "bold"),
                           fg="white",
                           bd=5,
                           relief="groove",
                           bg='lightskyblue4',
                           )

FastFoodFrame.grid(row=0, column=1, pady=1, padx=2)
list_frame = ListFrame(FoodFrame, text_list_1, 50)
list_frame_1 = ListFrame(FastFoodFrame, text_list_2, 50)
# update Button


buttonsFrame = LabelFrame(foodManuframe,
                          bd=7,
                          relief="groove",
                          )
buttonsFrame.grid(row=0, column=3, pady=2, padx=5)

TotalButton = Button(buttonsFrame, text='Total',
                     font=("times new roman", 15, "bold"),
                     fg="white",
                     bd="3",
                     relief="groove",
                     bg='lightskyblue4',
                     width=8,

                     )
TotalButton.grid(row=0, column=0, pady=7, padx=10)
# Bill Buton
BillButton = Button(buttonsFrame, text='Bill',
                    font=("times new roman", 15, "bold"),
                    fg="white",
                    bd="3",
                    relief="groove",
                    bg='lightskyblue4',

                    width=8,
                    anchor='n'

                    )
BillButton.grid(row=1, column=0, pady=7, padx=10)
EmailButton = Button(buttonsFrame, text='Email',
                     font=("times new roman", 15, "bold"),
                     fg="white",
                     bd="3",
                     relief="groove",
                     bg='lightskyblue4',
                     width=8,

                     )
EmailButton.grid(row=2, column=0, pady=7, padx=10)
PrintButton = Button(buttonsFrame, text='Print',
                     font=("times new roman", 15, "bold"),
                     fg="white",
                     bd="3",
                     relief="groove",
                     bg='lightskyblue4',
                     width=8,

                     )
PrintButton.grid(row=3, column=0, pady=7, padx=10)
ClearButton = Button(buttonsFrame, text='Clear',
                     font=("times new roman", 15, "bold"),
                     fg="white",
                     bd="3",
                     relief="groove",
                     bg='lightskyblue4',
                     width=8,

                     )
ClearButton.grid(row=4, column=0, pady=7, padx=10)
# 3rd frame creatioin
rd_frame = Frame(obj,
                 bd=3,
                 relief="groove",
                 bg='lightskyblue4'
                 )

# this is customer derails frame
rd_frame.pack(fill=X, pady=2)
VegfoodFrame = LabelFrame(rd_frame,
                          text="Veg Food",
                          font=("times new roman", 15, "bold"),
                          fg="white",
                          bd=7,
                          relief="groove",
                          bg='lightskyblue4',

                          )

VegfoodFrame.grid(row=0, column=0, pady=1, padx=2)
list_frame = ListFrame(VegfoodFrame, text_list_1, 50)

FFrame = LabelFrame(rd_frame,
                    text="Veg Food",
                    font=("times new roman", 15, "bold"),
                    fg="white",
                    bd=7,
                    relief="groove",
                    bg='lightskyblue4',

                    )

FFrame.grid(row=0, column=1, pady=1, padx=2)
list_frame = ListFrame(FFrame, text_list_1, 50)

# bill frame
BillFrame = Frame(foodManuframe,
                  bd=7,
                  relief=GROOVE
                  )
BillFrame.grid(row=0, column=2, padx=5, pady=10)

BillAreaLabel = Label(BillFrame,
                      text="Bill",
                      font=("times new roman", 15, "bold"),
                      bd=7,
                      relief=GROOVE
                      )
BillAreaLabel.pack(fill=X)

scrollbar = Scrollbar(BillFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textArea = Text(BillFrame,
                yscrollcommand=scrollbar.set,
                height=15,
                width=45
                )
textArea.pack()
scrollbar.config(command=textArea.yview)

# bill menu frame
billmenu = Frame(rd_frame,
                 bd=7,
                 relief=GROOVE
                 )
billmenu.grid(row=0, column=2, padx=5, pady=5)

obj.mainloop()
