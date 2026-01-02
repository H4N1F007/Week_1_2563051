import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("GradeMate")
root.geometry("400x500")
root.resizable(False,False)
header=tk.Frame(root,bg="#1f2937",height=60)
header.pack(fill="x")
header.pack_propagate(False)
logo=tk.Label(header,text="🎓",bg="#1f2937",fg="white",font=("Arial",20))
logo.pack(side="left",padx=10)
title=tk.Label(header,text="GradeMaster",bg="#1f2937",fg="white",font=("Ariel",16,"bold"))
title.pack(side="left")
back=tk.Button(header,text="Back",font=("Ariel",10),padx=10)
back.pack(side="right",padx=10)
body=tk.Frame(root,bg="white")
body.pack(fill="both",expand=True)
input1=tk.Frame(body,bg="white")
input1.pack(fill="both",expand=True)
tk.Label(input1,text="Welcome to GradeMaster\nEnter your marks to analyze result",font=("Ariel",12),bg="white").pack(pady=20)
tk.Label(input1,text="Subject 1(0-100)",bg="white").pack()
sub1=tk.Entry(input1)
sub1.pack(pady=6)
tk.Label(input1,text="Subject 2(0-100)",bg="white").pack()
sub2=tk.Entry(input1)
sub2.pack(pady=6)
tk.Label(input1,text="Subject 3(0-100)",bg="white").pack()
sub3=tk.Entry(input1)
sub3.pack(pady=6)
stats=tk.Label(input1,text="",fg="green",bg="white")
stats.pack(pady=10)

result=tk.Frame(body,bg="white")
tk.Label(result,text="Result Analysis",font=("Ariel",14,"bold"),bg="white").pack(pady=20)
total=tk.Label(result,text="",font=("Ariel",12),bg="white")
total.pack(pady=5)

avg=tk.Label(result,text="",font=("Ariel",12),bg="white")
avg.pack(pady=5)

grade=tk.Label(result,text="",font=("Ariel",14),bg="white")
grade.pack(pady=10)
again=tk.Button(result,text="Analyze Again",font=("Ariel",10,"bold"),bg="#1f2937",fg="white")
again.pack(pady=20)
def show(frame):
    frame.tkraise()

def calculate_result():
    try:
        m1=int(sub1.get())
        m2=int(sub2.get())
        m3=int(sub3.get())
        for m in (m1,m2,m3):
            if m < 0 or m > 100:
                raise ValueError
        total1=m1+m2+m3
        avg1=total1/3
        if avg1>=90:
            grade1="A"
            color="green"
        elif avg1>=75:
            grade1="B"
            color="green"
        elif avg1>=60:
            grade1="C"
            color="orange"
        elif avg1>=40:
            grade1="D"
            color="orange"
        else:
            grade1="Fail"
            color="red"
        total.config(text=f"Total Marks : {total1} / 300")
        avg.config(text=f"Average : {avg1:.2f}")
        grade.config(text=f"Final Grade : {grade1}",fg=color)
        show(result)
    except:
        messagebox.showerror("Error","Please enter valid marks (0-100)")
def go_back():
    sub1.delete(0,tk.END)
    sub2.delete(0,tk.END)
    sub3.delete(0,tk.END)
    show(input1)
analyze=tk.Button(input1,font=("Ariel",10,"bold"),bg="#1f2937",fg="white",text="Analyze Result",command=calculate_result)
analyze.pack(pady=20)
again.config(command=go_back)
back.config(command=go_back)

for frame in (input1,result):
    frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    show(input1)
    
            



root.mainloop()