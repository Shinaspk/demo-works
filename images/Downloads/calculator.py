import parser
from tkinter import *
root=Tk()
output=Entry(root)
output.grid(row=0,columnspan=8)
i=0
def variable(num):
    global i
    output.insert(i,num)
    i+=1
def clearall():
    output.delete(0,END)
def back():
    global i
    out=output.get()
    if len(out):
        newout=out[:-1]
        clearall()
        output.insert(i,newout)
    else:
        clearall()
        output.insert(i,"error")
def operator(op):
    global i
    length=len(op)
    output.insert(i,op)
    i+=length
def result():
    a = output.get()
    try:

       ans=parser.expr(a).compile()
       res=eval(ans)
       clearall()
       output.insert(0,res)
    except:
        clearall()
        output.insert(0,"error")


Button(root,text="1",command=lambda :variable(1)).grid(row=1,column=0)

Button(root,text="2",command=lambda :variable(2)).grid(row=1,column=1)
Button(root,text="3",command=lambda :variable(3)).grid(row=1,column=2)
Button(root,text="4",command=lambda :variable(4)).grid(row=2,column=0)
Button(root,text="5",command=lambda :variable(5)).grid(row=2,column=1)
Button(root,text="6",command=lambda :variable(6)).grid(row=2,column=2)
Button(root,text="7",command=lambda :variable(7)).grid(row=3,column=0)
Button(root,text="8",command=lambda :variable(8)).grid(row=3,column=1)
Button(root,text="9",command=lambda :variable(9)).grid(row=3,column=2)
Button(root,text="0",command=lambda :variable(0)).grid(row=4,column=0)
Button(root,text=".",command=lambda :operator('.')).grid(row=1,column=3)
Button(root,text="/",command=lambda :operator("/")).grid(row=1,column=4)
Button(root,text="pi",command=lambda:operator("*3.14")).grid(row=4,column=2)
Button(root,text="C",command=lambda :back()).grid(row=4,column=1)
Button(root,text="+",command=lambda :operator('+')).grid(row=2,column=3)
Button(root,text="-",command=lambda :operator("-")).grid(row=3,column=3)
Button(root,text="=",command=lambda :result()).grid(row=4,column=3)
Button(root,text="AC",command=lambda :clearall()).grid(row=1,column=4)
Button(root,text="*",command=lambda :operator("*")).grid(row=2,column=4)
root.mainloop()