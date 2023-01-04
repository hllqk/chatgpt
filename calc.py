import tkinter

#window
window = tkinter.Tk()
window.title("Calculator")
window.geometry("400x400")

#label
lbl = tkinter.Label(window, text="Input", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

#input
txt = tkinter.Entry(window,width=50)
txt.grid(column=1, row=0)

#function
def clicked():
    res = float(txt.get())
    lbl.configure(text="Result: "+str(res))

#button
btn = tkinter.Button(window, text="Calculate", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()