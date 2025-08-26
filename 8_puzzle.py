"""
    Họ Tên: Nguyễn Thái Bình        Họ Tên: Trương Hoài Chương      Họ Tên: Phạm Thị Kim Ngân
    MSSV:   23110080                MSSV:   2311081                 MSSV:   23110128
    
    Lớp: ARIN330585_05CLC
    Buổi: Sáng thứ 2 - thứ 6, tiết 1 - 4
"""

import tkinter as tk
import random
from tkinter import messagebox

class eight_puzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8 puzzle")
        self.position = [[0, 0], [0, 1]]
        self.create_widget()
        
    def create_widget(self):
        button1 = tk.Button(self.root, width=8, height=4, bg="red",
                            command=lambda x = 0, y = 0: self.toggle(x, y))
        button1.grid(row=0, column=0, padx=2, pady=2)
            
        button2 = tk.Button(self.root, width=8, height=4, bg="black",
                            command=lambda x = 0, y = 1: self.toggle(x, y))
        button2.grid(row=0, column=1, padx=2, pady=2)
    
    def toggle(self, x, y):
        near = [(x, y - 1), (x, y + 1)]
        for a, b in near:
            if 0 <= b < 2:
                if self.position[0][b] == 1:
                    self.position[0][b], self.position[0][x] = self.position[0][x], self.position[0][b]
                    print(self.position)
                    self.buttons[a][b].config(bg = "black")
                    self.buttons[x][y].config(bg = "red")
                
        
if __name__ == "__main__":
    root = tk.Tk()
    
    game = eight_puzzle(root)

    root.mainloop()