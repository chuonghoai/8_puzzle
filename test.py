import tkinter as tk
import random
from tkinter import messagebox

class eight_puzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8 puzzle")
        self.position = [[1, 0]]  # 1: red, 0: black
        self.buttons = [[None, None]]
        self.create_widget()
        
    def create_widget(self):
        self.buttons[0][0] = tk.Button(self.root, width=8, height=4, bg="red",
                                       command=lambda x=0, y=0: self.toggle(x, y))
        self.buttons[0][0].grid(row=0, column=0, padx=2, pady=2)
        self.buttons[0][1] = tk.Button(self.root, width=8, height=4, bg="black",
                                       command=lambda x=0, y=1: self.toggle(x, y))
        self.buttons[0][1].grid(row=0, column=1, padx=2, pady=2)
    
    def toggle(self, x, y):
        # Đổi màu giữa 2 nút khi click
        if x == 0 and y in [0, 1]:
            # Đảo vị trí màu
            self.position[0][0], self.position[0][1] = self.position[0][1], self.position[0][0]
            self.buttons[0][0].config(bg="red" if self.position[0][0] == 1 else "black")
            self.buttons[0][1].config(bg="red" if self.position[0][1] == 1 else "black")
                
        
if __name__ == "__main__":
    root = tk.Tk()
    game = eight_puzzle(root)
    root.mainloop()