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
        self.root.config(bg="lightgray")
        
        self.position = [   [[4, '4'], [1, '1'], [8, '8']],
                            [[3, '3'], [0, ''], [2, '2']],
                            [[6, '6'], [5, '5'], [7, '7']]]
        
        self.position_order = [0, 1, 2, 3, 4, 5, 6, 7, 8]      
        self.position_win = [[[1, '1'], [2, '2'], [3, '3']],
                             [[4, '4'], [5, '5'], [6, '6']],
                             [[7, '7'], [8, '8'], [0, '']]]
        self.game_size = 3
        self.buttons = []
        
        #Tạo giao diện
        self.create_widget()
        
    def create_widget(self):
        for i in range(self.game_size):
            row = []
            for j in range(self.game_size):
                color = "white" if self.position[i][j][0] == 0 else "lightpink"

                button = tk.Button(self.root, width=8, height=4, bg=color,
                                   command=lambda x=i, y=j: self.toggle(x, y),
                                   text=self.position[i][j][1])
                row.append(button)
            self.buttons.append(row)
    
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