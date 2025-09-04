import tkinter as tk
from tkinter import messagebox
import random

class eight_puzzle:
    #1. Khởi tạo các biến
    def __init__(self, root):
        self.root = root
        self.root.title("8 puzzle")
        self.root.config(bg="lightgray")
        self.position = []
        #Các con số sẽ xuất hiện trong trò chơi:
        self.position_order = [0, 1, 2, 3, 4, 5, 6, 7, 8]       #Số 0 là vị trí trống
        self.position_win = [[[1, '1'], [2, '2'], [3, '3']],    #Mảng 2 chiều dùng để kiểm tra người dùng có sắp xếp đúng ko
                             [[4, '4'], [5, '5'], [6, '6']],
                             [[7, '7'], [8, '8'], [0, '']]]
        self.game_size = 3
        self.buttons = []
        self.quickWin = False
        
        #Tạo giao diện
        self.create_widgets(self.position_order)

        #Sự kiện nhấn phím R thì reset trò chơi
        self.root.bind("<r>", lambda event: self.reset())
        self.root.bind("<R>", lambda event: self.reset())

        #Sự kiện nhấn phím W thì win nhanh trò chơi
        self.root.bind("<w>", lambda event: self.quick_win())
        self.root.bind("<W>", lambda event: self.quick_win())
    
    #2. Xáo trộn ngẫu nhiên vị trí xuất hiện các con số
    def random_position(self, order):
        #Điều kiện để ko xáo trộn vị trí các số nếu user muốn thắng nhanh
        order = list(order)
        if not self.quickWin:
            random.shuffle(order)
            while(order == self.position_order):
                random.shuffle(order)
            
        #Sau khi xáo trộn, sắp xếp lần lượt các con số của order vào các vị trí trên position
        index = 0
        for i in range(self.game_size):
            row = []
            for j in range(self.game_size):
                txt = "" if order[index] == 0 else f"{order[index]}"    #Vị trí 0 thì ko có số
                pos = [order[index], f"{txt}"]
                row.append(pos)
                index += 1
            self.position.append(row)       #Cứ mỗi khi sắp xếp xong 1 dòng thì thêm dòng đó vào position
            
    #Hàm tạo giao diện
    def create_widgets(self, order):
        #Xáo trộn cấc vị trí trước khi tạo giao diện
        self.random_position(order)
        
        #Bắt đầu tạo giao diện
        for i in range(self.game_size):
            row = []
            for j in range(self.game_size):
                #Màu sắt là lightpink nếu là các con số, nếu là số 0  thì mặc định màu trắng
                color = "lightpink" if self.position[i][j][0] != 0 else "white"
                
                #Biến num tạo ra từng ô chứa các con số
                        #self.root: Tạo ô trong giao diện root
                        #width, height: kích thước lần lượt có thể chứa 8 và 4 ký tự
                        #bg: Đặt màu nền của ô
                        #command: Phát tín hiệu khi user click, lambda x = i, y = j: Đóng bắng giá trị, hỗ trợ giữ đúng tọa độ của nó
                        #self.toggle(x, y): Gọi hàm toggle khi người dùng click với tham số (x, y)
                        #text: Chữ hiển thị trên nút
                num = tk.Button(self.root, width = 8, height = 4, bg = color,       
                                command=lambda x = i, y = j: self.toggle(x, y),
                                text=self.position[i][j][1])
                
                #Đặt ô vừa tạo vào vị trí (row, column), giãn cách với các ô khác là (padx, pady)
                num.grid(row = i, column = j, padx=2, pady=2)
                row.append(num)
            
            #Mỗi khi tạo xong 1 ô thì thêm ô đó vào biến buttons chính của chương trình
            self.buttons.append(row)
            
        #Tạo nút reset, các chức năng khác tương tự như trên
        reset_btn = tk.Button(self.root, text="Reset", command=self.reset)
        reset_btn.grid(row = self.game_size, column = 0, columnspan = 2, pady=10)
        
        #Tạo nút thắng nhanh
        quick_win_btn = tk.Button(self.root, text="Quick win", command=self.quick_win)
        quick_win_btn.grid(row = self.game_size, column = 1, columnspan = 2, pady=10)
        
        #Cài đặt khi giao diện bị kéo giãn thì mọi thứ trong giao diện cũng bị kéo giãn theo
        for i in range(self.game_size):
            self.root.grid_rowconfigure(i, weight=1)        #weight=1: độ nhạy giữa các ô khi kéo giãn
            self.root.grid_columnconfigure(i, weight=1)
            
    #Hàm kích hoạt khi user click vào
    def toggle(self, x, y):
        #Tìm 4 ô xung quanh nó
        near = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for a, b in near:
            #Đặt điều kiện để giới hạn phạm vi trong lưới 3x3
            if 0 <= a < self.game_size and 0 <= b < self.game_size:
                if self.position[a][b][0] == 0:     
                    #Nếu tìm thấy ô trông (có số 0) thì hoán đổi
                    
                    #Hoán đổi vị trí trong mảng 2 chiều position
                    self.position[a][b], self.position[x][y] = self.position[x][y], self.position[a][b]

                    #Thay đổi màu sắc của 2 ô cho nhau
                    self.buttons[a][b].config(text=self.position[a][b][1], bg = "lightpink")
                    self.buttons[x][y].config(text=self.position[x][y][1], bg = "white")
        
        #Mỗi lần user click thì kiểm tra xem nước đi đó có win ko
        self.check_win()

    #Hầm kiểm tra user có win ko
    def check_win(self):
        if self.position == self.position_win:      #position: mảng 2 chiều các vị trí ngẫu nhiên
                                                    #position: mảng 2 chiều các vị trí chính xác
            messagebox.showinfo("Congratulations", "You win!")
    
    #Nút reset
    def reset(self):
        #Thay đổi biển quickwin thành False để ko xung đột với reset
        self.quickWin = False

        #Xóa toàn bộ các nút và vị trí trên màn hình
        self.position = []
        self.buttons = []
        
        #Vẽ lại các nút và vị trí lên màn hinh
        self.create_widgets(self.position_order)
    
    def quick_win(self):
        #Xóa toàn bộ các nút và vị trí trên màn hình
        self.position = []
        self.buttons = []

        #Mảng 1 chiều vị trí các con số để win nhanh
        pos_QW = [1, 2, 3, 4, 5, 6, 7, 0, 8]

        #Thay đổi biển quickwin thành True để ko xung đột với reset
        self.quickWin = True

        #Vẽ lại
        self.create_widgets(pos_QW)
        

if __name__ == "__main__":
    #1. Tạo giao diện chính
    root = tk.Tk()
    
    #2. Gọi lớp eight_puzzle để chạy các hàm trong đó
    game = eight_puzzle(root)
    
    #3. Chuẩn bị ví trí để chỉnh vị trí xuất hiện khi chạy chương trình
    root.update_idletasks()     #Cập nhật giao diện để winfo_width() và winfo_height() có thể trả về con số chinh xác
    w = root.winfo_width()      #Chiều rộng giao diện
    h = root.winfo_height()     #Chiều cao giao diện
    x = int((root.winfo_screenwidth() / 2) - (w / 2))       #Vị trí x chính giữa màn hình
    y = int((root.winfo_screenheight() / 2) - (h / 2))      #Vị trí y chính giữa màn hình

    #4. Dùng hàm geometry để căn chỉnh vị trí xuất hiện chính giữa màn hình
    root.geometry(f"{w}x{h}+{x}+{y}")
    
    #4. Bắt đầu vòng lặp chương trình
    root.mainloop()