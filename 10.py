from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Крестики-нолики')

# Установка размеров окна
window_width = 350
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

game_run = True
field = []
cross_count = 0

style = ttk.Style()
style.configure('TButton.TLabel', font=('Verdana', 30, 'bold'), width=4, height=2)
style.configure('TButton', font=('Verdana', 30, 'bold'), width=4, height=2)

result_label = ttk.Label(root, text='')
result_label.grid(row=3, column=0, columnspan=3)

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['style'] = 'TButton'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0
    result_label.config(text='')

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['style'] = a2['style'] = a3['style'] = 'TButton.TLabel'
        global game_run
        game_run = False
        result_label.config(text=f'{smb} победил!')
    elif cross_count == 5:
        result_label.config(text='Ничья!')

def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = ttk.Button(root, text=' ', width=4,
                            style='TButton',
                            command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = ttk.Button(root, text='новая игра', command=new_game)
new_button.grid(row=4, column=0, columnspan=3, sticky='nsew')

root.update_idletasks()
root.mainloop()
