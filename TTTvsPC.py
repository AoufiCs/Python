from tkinter import *
from tkinter import messagebox
import random
root= Tk()
root.title("Tic Tac Toe !!       made by: (SwiftyGuy) ")
#Button click

def b_click(b):
    global count
    if b["text"]==" " :
        b["text"]="X"
        Win()
        count +=1
        if count!=9 and winning==0:
            Pc_Move()
            Win()
            count+=1
        
    else:
        messagebox.showerror("Tic Tac Toe","This BOX is already selected !\nPlease choose another BOX!")
    if count==9 and winning==0:
        messagebox.showinfo("Tic Tac Toe", "Oh no!\nIt's a DRAW!!")
        disable_all_buttons()
#Main_game
def Reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,T,winning,count,Move
    winning=0
    count=0
    Move=0
    #Buttons
    b1=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b1))
    b2=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b2))
    b3=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b3))
    b4=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b4))
    b5=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b5))
    b6=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b6))
    b7=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b7))
    b8=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b8))
    b9=Button(root,text=" ", font=("Arial",20),height=3,width=6,bg="Light Blue",command=lambda: b_click(b9))
    T=[[b1,b2,b3],[b4,b5,b6],[b7,b8,b9]]
    #Button grid
    for i in range(3):
        for j in range(3):
            T[i][j].grid(row=i, column=j)
    
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            T[i][j].config(state=DISABLED)
#Pc_Playmoves
def SecondSequence():
    global Move
    Move=0
    #Check if the player can win and stop him
    for i in range(3):
        if T[i][0]["text"]==T[i][1]["text"]=="X"  and T[i][2]["text"]==" ":
            Move=T[i][2]
        elif T[i][0]["text"]==T[i][2]["text"]=="X"  and T[i][1]["text"]==" ":
            Move=T[i][1] 
        elif T[i][1]["text"]==T[i][2]["text"]=="X"  and T[i][0]["text"]==" ":
            Move=T[i][0] 
        elif T[0][i]["text"]==T[1][i]["text"]=="X" and T[2][i]["text"]==" ":
            Move=T[2][i] 
        elif T[0][i]["text"]==T[2][i]["text"]=="X"  and T[1][i]["text"]==" ":
            Move=T[1][i] 
        elif T[1][i]["text"]==T[2][i]["text"]=="X" and T[0][i]["text"]==" ":
            Move=T[0][i] 
    if T[0][0]["text"]==T[1][1]["text"]=="X" and T[2][2]["text"]==" ":
            Move=T[2][2]
    elif T[0][0]["text"]==T[2][2]["text"]=="X"and T[1][1]["text"]==" ":
            Move=T[1][1]
    elif T[1][1]["text"]==T[2][2]["text"]=="X" and T[0][0]["text"]==" ":
            Move=T[0][0]
    elif T[0][2]["text"]==T[1][1]["text"]=="X"  and T[2][0]["text"]==" ":
            Move=T[2][0]
    elif T[0][2]["text"]==T[2][0]["text"]=="X" and T[1][1]["text"]==" ":
            Move=T[1][1]
    elif T[1][1]["text"]==T[2][0]["text"]=="X" and T[0][2]["text"]==" ":
            Move=T[0][2]
    if Move!=0:
        Move["text"]="O"
    else:
        #Check if center is free and take a side so it's always a draw
        if T[1][1]["text"]==" ":
            Move=T[1][1]
            Move["text"]="O"
        elif T[1][1]["text"]=="O" and T[1][0]["text"]==" ":
            Move=T[1][0]
            Move["text"]="O"
        elif T[1][1]["text"]=="O" and T[1][2]["text"]==" ":
            Move=T[1][2]
            Move["text"]="O"
        else:
            #Check if a corner is free
            C=[]
            S=[]
            T1=[T[0][0],T[0][2],T[2][0],T[2][2]]
            for i in T1 : #C.append(i) if i["text"]==" " for i in T1
                if i["text"]==" ":
                    C.append(i)
        
            
            if C!=[]:
                Move = random.choice(C)
                Move["text"]="O"
            else:
                #Check if sides are free
                T2=[T[0][1],T[1][0],T[1][2],T[2][1]]
                for i in T2 : #S.append(i) if i["text"]==" " for i in T2
                    if i["text"]==" ":
                        S.append(i)
                if S!=[]:
                    Move = random.choice(S)
                    Move["text"]="O" 
def Pc_Move():
    global Move,count
    Move=0
    #Check if Pc can win:
    for i in range(3):
        if T[i][0]["text"]==T[i][1]["text"]=="O"  and T[i][2]["text"]==" ":
            Move=T[i][2]
        elif T[i][0]["text"]==T[i][2]["text"]=="O"  and T[i][1]["text"]==" ":
            Move=T[i][1] 
        elif T[i][1]["text"]==T[i][2]["text"]=="O"  and T[i][0]["text"]==" ":
            Move=T[i][0] 
        elif T[0][i]["text"]==T[1][i]["text"]=="O" and T[2][i]["text"]==" ":
            Move=T[2][i] 
        elif T[0][i]["text"]==T[2][i]["text"]=="O"  and T[1][i]["text"]==" ":
            Move=T[1][i] 
        elif T[1][i]["text"]==T[2][i]["text"]=="O" and T[0][i]["text"]==" ":
            Move=T[0][i] 
    if T[0][0]["text"]==T[1][1]["text"]=="O" and T[2][2]["text"]==" ":
            Move=T[2][2]
    elif T[0][0]["text"]==T[2][2]["text"]=="O"and T[1][1]["text"]==" ":
            Move=T[1][1]
    elif T[1][1]["text"]==T[2][2]["text"]=="O" and T[0][0]["text"]==" ":
            Move=T[0][0]
    elif T[0][2]["text"]==T[1][1]["text"]=="O"  and T[2][0]["text"]==" ":
            Move=T[2][0]
    elif T[0][2]["text"]==T[2][0]["text"]=="O" and T[1][1]["text"]==" ":
            Move=T[1][1]
    elif T[1][1]["text"]==T[2][0]["text"]=="O" and T[0][2]["text"]==" ":
            Move=T[0][2]
    if Move==0:
        SecondSequence()
    else:
        Move["text"]="O"
#Win Function
def Win():
    global winning
    for i in range(3):
        if T[i][0]["text"]==T[i][1]["text"]==T[i][2]["text"]!=" ":
            T[i][0].config(bg="red") 
            T[i][1].config(bg="red") 
            T[i][2].config(bg="red") 
            Message="Congratulations!!\n"+ T[i][0]["text"]+ " has won this time!!"
            messagebox.showinfo("Tic Tac Toe",Message)
            winning=1
            disable_all_buttons()
        elif T[0][i]["text"]==T[1][i]["text"]==T[2][i]["text"]!=" ":
            T[0][i].config(bg="red") 
            T[1][i].config(bg="red") 
            T[2][i].config(bg="red")  
            Message="Congratulations!!\n"+ T[0][i]["text"]+ " has won this time!!"
            messagebox.showinfo("Tic Tac Toe",Message)
            winning=1
            disable_all_buttons()
    if b1["text"]==b5["text"]==b9["text"]!=" ":
            b1.config(bg="red") 
            b5.config(bg="red") 
            b9.config(bg="red") 
            Message="Congratulations!!\n"+ b1["text"]+ " has won this time!!"
            messagebox.showinfo("Tic Tac Toe",Message)
            winning=1
            disable_all_buttons()
    elif b3["text"]==b5["text"]==b7["text"]!=" ":
            b3.config(bg="red") 
            b5.config(bg="red") 
            b7.config(bg="red") 
            Message="Congratulations!!\n"+ b3["text"]+ " has won this time!!"
            messagebox.showinfo("Tic Tac Toe",Message)
            winning=1
            disable_all_buttons()
#Menu
Game_menu= Menu(root)
root.config(menu=Game_menu)
#Options in Menu
options=Menu(Game_menu, tearoff=False)
Game_menu.add_cascade(label="Options",menu=options)
options.add_command(label="Reset game", command = Reset)
#Game
Reset()
root.mainloop()
