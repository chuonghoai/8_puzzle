import tkinter as tk
from tkinter import messagebox
import random

class eight_puzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8 puzzle")
        self.root.config(bg="lightgray")
        self.position = []
        self.position_order = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.position_win = [[[1, '1'], [2, '2'], [3, '3']],
                             [[4, '4'], [5, '5'], [6, '6']],
                             [[7, '7'], [8, '8'], [0, '']]]
        self.game_size = 3
        self.buttons = []
        self.quickWin = False
        self.create_widgets(self.position_order)
    
    def random_position(self, order):
        if not self.quickWin:
            random.shuffle(order)
        index = 0
        for i in range(self.game_size):
            row = []
            for j in range(self.game_size):
                txt = "" if order[index] == 0 else f"{order[index]}" 
                pos = [order[index], f"{txt}"]
                row.append(pos)
                index += 1
            self.position.append(row)
            
    def create_widgets(self, order):
        self.random_position(order)
        for i in range(self.game_size):
            row = []
            for j in range(self.game_size):
                color = "lightpink" if self.position[i][j][0] != 0 else "white"
                num = tk.Button(self.root, width = 8, height = 4, bg = color, 
                                command=lambda x = i, y = j: self.toggle(x, y),
                                text=self.position[i][j][1])
                num.grid(row = i, column = j, padx=2, pady=2)
                row.append(num)
            self.buttons.append(row)
            
            reset_btn = tk.Button(self.root, text="Reset", command=self.reset)
            reset_btn.grid(row = self.game_size, column = 0, columnspan = 2, pady=10)
            
            quick_win_btn = tk.Button(self.root, text="Quick win", command=self.quick_win)
            quick_win_btn.grid(row = self.game_size, column = 1, columnspan = 2, pady=10)
            
    def toggle(self, x, y):
        near = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for a, b in near:
            if 0 <= a < self.game_size and 0 <= b < self.game_size:
                if self.position[a][b][0] == 0:
                    self.position[a][b], self.position[x][y] = self.position[x][y], self.position[a][b]
                    self.buttons[a][b].config(text=self.position[a][b][1], bg = "lightpink")
                    self.buttons[x][y].config(text=self.position[x][y][1], bg = "white", )
        self.check_win()

    def check_win(self):
        if self.position == self.position_win:
            messagebox.showinfo("Congratulations", "You win!")
    
    def reset(self):
        self.quickWin = False
        self.position = []
        self.buttons = []
        self.create_widgets(self.position_order)
    
    def quick_win(self):
        self.position = []
        self.buttons = []
        pos_QW = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        self.quickWin = True
        self.create_widgets(pos_QW)
        

if __name__ == "__main__":
    root = tk.Tk()
    game = eight_puzzle(root)
    
    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    x = int((root.winfo_screenwidth() / 2) - (w / 2))
    y = int((root.winfo_screenheight() / 2) - (h / 2))

    root.geometry(f"{w}x{h}+{x}+{y}")
    root.mainloop()