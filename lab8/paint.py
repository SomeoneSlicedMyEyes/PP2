import tkinter as tk
from tkinter import Menu, Canvas, PhotoImage

def change_tool(tool_name):
    global selected_tool
    selected_tool = tool_name

def change_color(color):
    global pen_color
    pen_color = color

def eraser():
    global pen_color
    pen_color = "white"

def draw(event):
    if selected_tool == "pen":
        # Рисует маленькие круги при движении мыши, чтобы создать эффект пера
        canvas.create_oval(event.x, event.y, event.x+3, event.y+3, fill=pen_color)
    elif selected_tool == "circle":
        # Рисует окружности с определенным размером
        canvas.create_oval(event.x, event.y, event.x+25, event.y+25, outline=pen_color)
    elif selected_tool == "square":
        # Рисует квадраты с определенным размером
        canvas.create_rectangle(event.x, event.y, event.x+25, event.y+25, outline=pen_color)

root = tk.Tk()
root.title("Simple Paint")

menu = Menu(root)
root.config(menu=menu)

# Создаем холст для рисования
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

selected_tool = "pen"
pen_color = "black"

# Путь к изображениям инструментов
pen_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/pen_cursor.png")
circle_selected_false_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/circle_selected_false.png")
circle_selected_true_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/circle_selected_true.png")
square_selected_false_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/square_selected_false.png")
square_selected_true_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/square_selected_true.png")
change_color_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/change_color.png")
eraser_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/eraser.png")

tool_menu = Menu(menu)
menu.add_cascade(label="Tool", menu=tool_menu)

# Добавляем инструменты в меню и привязываем к ним соответствующие функции
tool_menu.add_command(label="Pen", image=pen_img, compound=tk.LEFT, command=lambda: change_tool("pen"))
tool_menu.add_command(label="Circle", image=circle_selected_false_img, compound=tk.LEFT, command=lambda: change_tool("circle"))
tool_menu.add_command(label="Square", image=square_selected_false_img, compound=tk.LEFT, command=lambda: change_tool("square"))
tool_menu.add_command(label="Change Color", image=change_color_img, compound=tk.LEFT, command=lambda: change_color("red"))
tool_menu.add_command(label="Eraser", image=eraser_img, compound=tk.LEFT, command=eraser)

canvas.bind("<B1-Motion>", draw)

root.mainloop()
