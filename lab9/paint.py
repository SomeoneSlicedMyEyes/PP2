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
        canvas.create_oval(event.x, event.y, event.x+3, event.y+3, fill=pen_color)
    elif selected_tool == "circle":
        canvas.create_oval(event.x, event.y, event.x+25, event.y+25, outline=pen_color)
    elif selected_tool == "square":
        canvas.create_rectangle(event.x, event.y, event.x+25, event.y+25, outline=pen_color)
    elif selected_tool == "rhombus":
        canvas.create_polygon(event.x, event.y-20, event.x+20, event.y, event.x, event.y+20, event.x-20, event.y, outline=pen_color)
    elif selected_tool == "right_triangle":
        canvas.create_polygon(event.x, event.y, event.x, event.y+30, event.x+30, event.y, outline=pen_color)
    elif selected_tool == "equilateral_triangle":
        canvas.create_polygon(event.x, event.y, event.x+15, event.y+26, event.x-15, event.y+26, outline=pen_color)

root = tk.Tk()
root.title("Simple Paint")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

selected_tool = "pen"
pen_color = "black"

pen_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/pen_cursor.png")
circle_selected_false_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/circle_selected_false.png")
circle_selected_true_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/circle_selected_true.png")
square_selected_false_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/square_selected_false.png")
square_selected_true_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/square_selected_true.png")
rhombus_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/rhombus.png")
right_triangle_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/right_triangle.png")
equilateral_triangle_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/equilateral_triangle.png")
change_color_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/change_color.png")
eraser_img = PhotoImage(file="C:/Visual Studio Code/PP2/PP2/PP2/lab9/materials/eraser.png")

tool_menu = Menu(menu)
menu.add_cascade(label="Tool", menu=tool_menu)
tool_menu.add_command(label="Pen", image=pen_img, compound=tk.LEFT, command=lambda: change_tool("pen"))
tool_menu.add_command(label="Circle", image=circle_selected_false_img, compound=tk.LEFT, command=lambda: change_tool("circle"))
tool_menu.add_command(label="Square", image=square_selected_false_img, compound=tk.LEFT, command=lambda: change_tool("square"))
tool_menu.add_command(label="Rhombus", image=rhombus_img, compound=tk.LEFT, command=lambda: change_tool("rhombus"))
tool_menu.add_command(label="Right Triangle", image=right_triangle_img, compound=tk.LEFT, command=lambda: change_tool("right_triangle"))
tool_menu.add_command(label="Equilateral Triangle", image=equilateral_triangle_img, compound=tk.LEFT, command=lambda: change_tool("equilateral_triangle"))
tool_menu.add_command(label="Change Color", image=change_color_img, compound=tk.LEFT, command=lambda: change_color("red"))
tool_menu.add_command(label="Eraser", image=eraser_img, compound=tk.LEFT, command=eraser)

canvas.bind("<B1-Motion>", draw)

root.mainloop()
