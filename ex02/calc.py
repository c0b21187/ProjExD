import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"] #クリックされたボタンの文字
    #tkm.showinfo("", f"{num}のボタンがクリックされました")
    #entry.insert(tk.END, num)
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    
    elif num == "AC": 
        entry.delete(0,tk.END) #オールクリアされます
    
    elif num == "+/-":
        eqn = entry.get()
        res = eval(eqn)
        res = res * -1
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    
    elif num == "%":
        eqn = entry.get()
        res = eval(eqn)
        res = res * 0.01
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    
    else:
        entry.insert(tk.END,num)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk")
    #root.geometry("300x500")

    btn = tk.Button(root, text="9",
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
                    )

    entry = tk.Entry(root, justify="right", width=14, font=(("Times New Roman", 40)))
    entry.grid(row =0, column =0, columnspan =4) #横方向に3マス結合

    r,c = 1, 0 #r 行番号 c 列番号
    
    for i, num in enumerate(["AC", "+/-", "%", "//",7, 8, 9,"*", 4, 5, 6, "-", 1, 2, 3, "+",0, "00", ".", "="]):
        btn = tk.Button(root,
                        text=f"{num}",
                        width=4,
                        height=2,
                        font=("Times New Roman",30)
                    )

        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)

        
        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0

    root.mainloop()