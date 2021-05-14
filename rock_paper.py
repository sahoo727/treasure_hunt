from tkinter import *
from random import randint
from tkinter import ttk

root=Tk()
#root.iconbitmap('rock.png')
photo=PhotoImage(file='rock.png')
root.iconphoto(False,photo)
root.title('Rock Paper Scissors')
root.geometry("500x600")
root.config(bg='white')

#Define our images

rock=PhotoImage(file='cave-painting.png')
paper=PhotoImage(file='paper.png')
scissor=PhotoImage(file='scissor.png')

#Add Images to a list
image_list=[rock,paper,scissor]  #rock=0,paper=1,scissor=2

#Pick random number between 0 and 2
pick_number=randint(0,2)


#Throw up an image when the program starts
image_label=Label(root,image=image_list[pick_number])
image_label.pack(pady=20)

#Create Spin function
def spin():
    #pick random number
    pick_number=randint(0,2)
    #show image
    image_label.config(image=image_list[pick_number])

    #game logic

    #Convert Dropdown choice to a number
    if user_choice.get()=="Rock":
        user_choice_value=0
    elif user_choice.get()=="Paper":
        user_choice_value=1
    elif user_choice.get()=="Scissor":
        user_choice_value=2

    #Determine if we won or lost(camparing above rock paper scissor to dropdown Rock Paper Scissor)
#If user picks rock    
    if user_choice_value==0: #Rock   #this is picked by us
        if pick_number==0:#rock   #this is picked by computer
            win_lose_label.config(text="It's a tie! Spin again")
        elif pick_number==1:#paper
            win_lose_label.config(text="Paper covers rock,U LOSE..")
        elif pick_number==2:#scissor
            win_lose_label.config(text="Rock smashes scissor,U WIN!")   
    
#If user picks paper
    if user_choice_value==1: #Paper   #this is picked by us
        if pick_number==1:#paper  #this is picked by computer
            win_lose_label.config(text="It's a tie! Spin again")
        elif pick_number==0:#rock
            win_lose_label.config(text="Paper covers rock,U WIN!")
        elif pick_number==2:#scissor
            win_lose_label.config(text="Scissor cuts paper,U LOSE..")   

#If user picks scissor
    if user_choice_value==2: #Scissor   #this is picked by us
        if pick_number==2:#scissor  #this is picked by computer
            win_lose_label.config(text="It's a tie! Spin again")
        elif pick_number==0:#rock
            win_lose_label.config(text="Rock smashes scissor U LOSE..")
        elif pick_number==1:#paper
            win_lose_label.config(text="Scissor cuts paper.U WIN!")   



#Make our choice(Dropdown)
user_choice=ttk.Combobox(root,value=("Rock","Paper","Scissor"))
user_choice.current(0)  #box is initialized to rock
user_choice.pack(pady=20)

#Label for showing if you won or not
win_lose_label=Label(root,text="",font=("Helvetica",18))
win_lose_label.pack(pady=50)


#Create Spin Button
spin_button=Button(root,text="Spin!",command=spin)
spin_button.pack(pady=10)


root.mainloop()

