 import tkinter as tk
from PIL import ImageTk,Image

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        
        calculation = str((eval(calculation)))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, "Error") 


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")
    
root = tk.Tk()
root.geometry("320x520+500+100")
root.resizable(False,False)
root.config(bg='black')
root.title('Calculator')

my_image=ImageTk.PhotoImage(file="C:/Users/Chamee/Desktop/calBG.jpg")
lbl_image=tk.Label(root,image=my_image,bd=0).place(x=0,y=0)

text_result = tk.Text(root,height=2, font=('times',35,'bold'), bg="#3C3C3C",fg='white',bd=0)
text_result.place(x=24,y=40,height=55,width=270)

btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation("1") ,font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_1.place(x=29,y=155,width=38,height=42)

btn_2=tk.Button(root,text="2", command=lambda:add_to_calculation("2"),font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_2.place(x=103,y=155,width=38,height=42)

btn_2=tk.Button(root,text="3", command=lambda:add_to_calculation("3"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_2.place(x=180,y=155,width=38,height=42)

btn_plus=tk.Button(root,text="+", command=lambda:add_to_calculation("+"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_plus.place(x=255,y=155,width=38,height=42)


btn_4=tk.Button(root,text="4",command=lambda:add_to_calculation("4") ,font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_4.place(x=29,y=227,width=38,height=42)

btn_5=tk.Button(root,text="5", command=lambda:add_to_calculation("5"),font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_5.place(x=103,y=227,width=38,height=42)

btn_6=tk.Button(root,text="6", command=lambda:add_to_calculation("6"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_6.place(x=180,y=227,width=38,height=42)

btn_minus=tk.Button(root,text="-", command=lambda:add_to_calculation("-"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_minus.place(x=255,y=227,width=38,height=42)



btn_7=tk.Button(root,text="7",command=lambda:add_to_calculation("7") ,font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_7.place(x=29,y=301,width=38,height=42)

btn_8=tk.Button(root,text="8", command=lambda:add_to_calculation("8"),font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_8.place(x=103,y=301,width=38,height=42)

btn_9=tk.Button(root,text="9", command=lambda:add_to_calculation("9"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_9.place(x=180,y=301,width=38,height=42)

btn_multi=tk.Button(root,text="*", command=lambda:add_to_calculation("*"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_multi.place(x=255,y=305,width=38,height=42)




btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("(") ,font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_open.place(x=29,y=367,width=38,height=42)

btn_0=tk.Button(root,text="0", command=lambda:add_to_calculation("0"),font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_0.place(x=103,y=370,width=38,height=42)

btn_close=tk.Button(root,text=")", command=lambda:add_to_calculation(")"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_close.place(x=180,y=367,width=38,height=42)

btn_devi=tk.Button(root,text="/", command=lambda:add_to_calculation("/"), font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_devi.place(x=255,y=367,width=38,height=42)



btn_clear=tk.Button(root,text="C", command= clear_field, font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_clear.place(x=60,y=440,width=38,height=42)

btn_equal=tk.Button(root,text="=", command=evaluate_calculation, font=('calibri',30,'bold'),fg='white', bg="#3C3C3C",bd=0,cursor='hand2',activebackground="#3C3C3C")
btn_equal.place(x=225,y=440,width=38,height=42)






root.mainloop()



