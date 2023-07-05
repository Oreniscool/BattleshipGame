#imports
from random import randint
import tkinter as tk

version="v1.3"

#custom colours
ocean="#2B65EC"
burgundy="#800020"

#Main window 
main_window= tk.Tk()
main_window.title(f"Battleship Game {version} by Qitiya")
main_window.configure(bg=ocean)
main_window.geometry("400x500")
main_window.resizable(False, False)

#board
size=5

#Game
but_holder={}
def game():
    tries=size**2//3
    randnum=str(f"{randint(0,size-1)}{randint(0,size-1)}")

    #configuration
    def config():
        global size
        def c_apply():
            global size
            try:
                value=int(config_entry.get())
            except ValueError:
                error_label=tk.Label(master=config_frame,text="\nPlease enter a number!\n", fg="red")
                error_label.grid(row=1, column=0)
            else:
                if value<=10 and value>=3:               
                    size=value
                    size=value
                    reset()
                    main_window.wm_geometry(f"{size*75+25}x{size*100}")
                    config_window.destroy()
                else:
                    error_label=tk.Label(master=config_frame,text="Please enter a valid size \nbetween 3 and 10!", fg="red")
                    error_label.grid(row=1, column=0)
        #config window
        config_window=tk.Toplevel()
        config_window.title("Configure")
        config_window.geometry("250x100")
        config_window.resizable(False, False)
        config_frame=tk.Frame(master=config_window)
        for i in range(2):
            config_frame.columnconfigure(i, weight=1, minsize=50)
            config_frame.rowconfigure(i, weight=1, minsize=50)
        
        #labels    
        size_label=tk.Label(master=config_frame,
                            text="Size:",
                            font=4)
        size_label.grid(row=0,column=0)

        #entry box
        config_entry=tk.Entry(master=config_frame, font=4, width=3)
        config_entry.insert(0, f"{size}")
        config_entry.grid(row=0,column=1)

        #Button
        config_apply=tk.Button(master=config_frame,
                               text="Apply", 
                               height=2,
                               width=2, 
                               command=c_apply)
        config_apply.grid(row=1, column=1, sticky="ew")

        #Packing
        config_frame.pack(expand=True)
        config_window.grab_set()
        config_window.mainloop()
        
    def info():
        info_window=tk.Toplevel()
        info_window.title("Information")
        info_window.geometry("500x300")
        info_label=tk.Label(master=info_window, font=5, justify=tk.LEFT, text=f"Qitiya's Battleship Game {version}."+ "\nLatest features:\n•New info and configure features."+"\n\t>Info: Information about game version.\n"+"\n\t>Configure: Option to change board size, \n\t\tLives scale as size²/3."+"\n•The Battleship is now 2 tiles long"+"\n•Cosmetic improvements. \n\nMade in Python with Tkinter GUI.")
        info_label.pack()
        info_window.resizable(False,False)
        info_window.grab_set()
    
    def disableb():
        for i in range(size):
                for j in range(size):
                    but_holder["butt",str(i)+str(j)].configure(state= tk.DISABLED)

    def reset():
        frame_reset.destroy()
        button_reset.destroy()
        frame_info.destroy()
        frame_ocean.destroy()
        button_config.destroy()
        button_i.destroy()
        game()

    def try_b(row,column):
        try:
            button2r=but_holder["butt",str(row)+str(column+1)]
            button2l=but_holder["butt",str(row)+str(column-1)]
        except:
            button1=but_holder["butt",str(row)+str(column)]
        else:
            button1=but_holder["butt",str(row)+str(column)]
            button2r=but_holder["butt",str(row)+str(column+1)]
            button2l=but_holder["butt",str(row)+str(column-1)]
        

        if str(f"{row}{column}") == randnum:
            try:
                button2r.configure(bg="green")
            except:
                button1.configure(bg="green")
            else:
                button1.configure(bg="green")
                button2r.configure(bg="green")
            lives_name['text']="You won!"
            disableb()
        elif str(f"{row}{column}") == str(int(randnum)+1):
            try:
                button2l.configure(bg="green")
            except:
                button1.configure(bg="green")
            else:
                button1.configure(bg="green")
                button2l.configure(bg="green")
            lives_name['text']="You won!"
            disableb()

        else:
            button1.configure(bg="red")
            button1.configure(state= tk.DISABLED)
            value=int(lives['text'])
            lives['text']=f"{value-1}"
        if int(lives['text'])==0:
            lives_name['text']="You lost sucker"


            disableb()

    #Frames
    frame_info=tk.Frame(master=main_window,bg=ocean)
    frame_ocean=tk.Frame(master=main_window,bg=ocean)
    frame_reset=tk.Frame(master=main_window,bg=ocean)
    frame_i=tk.Frame(master=main_window,bg=ocean)
    frame_c=tk.Frame(master=main_window,bg=ocean)
    #Labels
    lives_name=tk.Label(master=frame_info,
                        text="Lives:",
                        font=12, bg=ocean)
    
    lives=tk.Label(master=frame_info, 
                   text=str(tries),  
                   font=12, fg="white", 
                   bg=ocean)
    
    #buttons
    button_reset=tk.Button(master=frame_reset,
                           text="Reset", command=reset, 
                           bg=ocean, 
                           height=2, 
                           width=8)
    button_i=tk.Button(master=frame_i,
                   text="Info",
                   height=2, 
                   width=8,
                   bg=ocean,
                   command=info)
    button_config=tk.Button(master=frame_c,
                            text="Configure",
                            height=2, 
                            width=8,
                            bg=ocean,
                            command=config)
    
    #Label/Button packing
    button_reset.pack()
    button_i.pack(side=tk.RIGHT)
    lives_name.pack(side=tk.LEFT)
    lives.pack(side=tk.RIGHT)
    button_config.pack(side=tk.LEFT)

    #Loop for main board
    for i in range(size+2):
        main_window.rowconfigure(i, weight=1, minsize=50)
    for i in range(size):
        frame_ocean.columnconfigure(i, weight=1, minsize=75)
        frame_ocean.rowconfigure(i, weight=1, minsize=50)
        main_window.columnconfigure(i, weight=1, minsize=75)
        for j in range(size):
            but_holder["butt",str(i)+str(j)]=tk.Button(master=frame_ocean,
                                                       bg="brown",
                                                       activebackground=burgundy,
                                                       height=2, 
                                                       width=4, 
                                                       command=lambda i=i, j=j: try_b(but_holder["butt",str(i)+str(j)].grid_info()["row"],but_holder["butt",str(i)+str(j)].grid_info()["column"]))
            locals().update(but_holder)
            but_holder["butt",str(i)+str(j)].grid(row=i, column=j, pady=15)
    
    #Frame griding
    frame_info.grid(row=0, column=0, columnspan=2, sticky="s")
    frame_ocean.grid(row=1,column=0, rowspan=size, columnspan=size)
    frame_reset.grid(row=size+1, column=size//2)
    frame_i.grid(row=size+1, column=(size//2)-1)
    frame_c.grid(row=size+1, column=(size//2)+1)


#run
game()
main_window.mainloop()