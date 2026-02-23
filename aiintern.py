import tkinter as tk
from tkinter  import messagebox,ttk,scrolledtext
main=tk.Tk()
main.geometry("1920x1080")
main.configure(bg="gray")
main.title("chatbot app")


# to create multiple pages i need container
container=tk.Frame(main,bg="pink")
container.place(x=0,y=0,width=1920,height=1080)

welcome_page=tk.Frame(container,bg="lightblue")
chatbot_page=tk.Frame(container,bg="lightgreen")

for page in (welcome_page,chatbot_page):
    page.place(x=0,y=0,width=1920,height=1080)

#switch page func
def sp(page):
    page.tkraise()
#-----wecome page-----
tk.Label(welcome_page,text="Welcome to chatbot",font=("Arial",20),bg="lightblue").pack(padx=20,pady=20)

un=tk.Entry(welcome_page,font=("Arial",14)).pack(pady=5)

tk.Button(welcome_page,text="start chat",command=lambda:sp(chatbot_page)).pack(pady=10)

#====chatbot page=====


tk.Label(chatbot_page,text="chatbot ready...search here").pack(pady=20)
tk.Button(chatbot_page,text="back",command=lambda:sp(welcome_page)).pack(pady=10)

sp(welcome_page)

main.mainloop()










