import tkinter as tk  
import main

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  

def read_data():  

    with open('data.txt', 'r', encoding='utf-8') as file:  
        data = file.read()
    return data  


def go_game():  
    main.start_game()  
    output = "Сообщения из функции go_game:\n"  
    output += f"{read_data()}...\n"

    console_output_area.config(state=tk.NORMAL) 
    console_output_area.delete("1.0", tk.END) 
    console_output_area.insert(tk.END, output)
    console_output_area.config(state=tk.DISABLED)

    display_output()


def execute_tasks():
    main.process_tasks()
    output = "Задачи выполняются..\n"
    output += f"{read_data()}...\n"

    console_output_area.config(state=tk.NORMAL) 
    console_output_area.delete("1.0", tk.END)    
    console_output_area.insert(tk.END, output) 
    console_output_area.config(state=tk.DISABLED) 

    display_output()

def display_output():  
    text = main.main()  
    text_to_display = [  
        f"Баланас равен = {text[0]}",  
        f"Play passes = {text[1]}",  
        f"Фарминг: {text[2]}",  
        f"{text[3]}"  
    ]  

    for i, text_area in enumerate(output_text_areas):  
        text_area.config(state=tk.NORMAL)          
        text_area.delete("1.0", tk.END)            
        text_area.insert(tk.END, text_to_display[i])  
        text_area.config(state=tk.DISABLED)        


root = tk.Tk()  
root.title("Text Output Fields")  


output_text_areas = []  


for i in range(4):  
    output_area = tk.Text(root, height=2, width=25)  
    output_area.pack(pady=5)  
    output_area.config(state=tk.DISABLED)  
    output_text_areas.append(output_area)  

 
main_output_button = tk.Button(root, text="Display Output", command=display_output)  
main_output_button.pack(pady=5)  

 
go_game_button = tk.Button(root, text="Go game", command=go_game)  
go_game_button.pack(pady=5)  


execute_tasks_button = tk.Button(root, text="Выполнить задачи", command=execute_tasks)  
execute_tasks_button.pack(pady=5)  

  
console_output_area = tk.Text(root, height=10, width=50)  
console_output_area.pack(pady=10)  
console_output_area.config(state=tk.DISABLED)  


display_output()  

  
root.mainloop()