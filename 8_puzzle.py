"""
    Họ Tên: Nguyễn Thái Bình        Họ Tên: Trương Hoài Chương      Họ Tên: Phạm Thị Kim Ngân
    MSSV:   23110080                MSSV:   2311081                 MSSV:   23110128
    
    Lớp: ARIN330585_05CLC
    Buổi: Sáng thứ 2 - thứ 6, tiết 1 - 4
"""
#Gọi thư viện tkinter
import tkinter as tk

class eight_puzzle:
    #Hàm contructor khai báo các biến sử dụng để vẽ giao diện
    #Dễ hiểu hơn, trong chương trình main, khi gọi game = eight_puzzle(root), thì lớp eight_puzzle chạy hàm __init__ 
    def __init__(self, root):
        #khai báo root(biến root sử dụng trong các hàm ở dưới) = root(tham số root được truyền ở hàm main)
        self.root = root
        #Đặt tiêu đề của giao diện
        self.root.title("8 puzzle")
        #Đặt màu background = lightgray bằng hàm config
        self.root.config(bg="lightgray")
        
        #Vị trí các ô số sẽ xuất hiện trong giao diện
        #Ví dụ với [1, '1']: Vị trí của số 1 trong ma trận position là vị trí [0][1], chữ xuất hiện trên giao diện là '1'
        self.position = [   [[4, '4'], [1, '1'], [8, '8']],
                            [[3, '3'], [0, ''], [2, '2']],
                            [[6, '6'], [5, '5'], [7, '7']]]
        #Kích thước của ma trận, trong trò 8 puzzle sẽ chỉ có 8 ô số và 1 ô trống, nên kích thước sẽ là 3x3        
        self.game_size = 3
        #Khai báo mảng buttons để chứa các nút sẽ được tạo trong hàm create_widget, khi tạo xong thì mảng buttons sẽ là ma trận 3x3
        self.buttons = []
        #Tạo giao diện
        self.create_widget()
        
    def create_widget(self):
        #2 vòng lặp lồng nhau i và j chạy trong range(self.game_size) sẽ chạy hoàn hảo các con số có sẵn trong ma trận position
        for i in range(self.game_size):
            #Tạo mảng row, để mỗi khi vòng lặp j chạy xong (tức là vừa tạo xong 3 nút, sẽ được thêm lần lượt vào row)
            row = []
            for j in range(self.game_size):
                #Đặt màu cho các con số, nếu != 0  thì màu lightpink (1 -> 8), ngược lại = 0 thì màu trắng (giống như ô trống)
                color = "white" if self.position[i][j][0] == 0 else "lightpink"
                
                #Bắt đầu tạo các ô số bằng tk.Button, để tạo và vẽ ra giao diện thì cần 2 bước:
                #B1: Khởi tạo biến button chứa nút được tạo, với cấu trúc như sau:
                    #self.root: nút được tạo sẽ nằm trong giao diện root (giao diện chính)
                    #width=8, height=4: độ rộng chứa 8 ký tự, độ cao chứa 4 ký tự, vì chiều cao của chữ cái dài gấp đôi chiều rộng, nên tạo rộng=8 và cao = 4 sẽ hoàn hảo tạo ra hình vuông
                    #bg=color: biến bg là màu background của nút tk.Button, color là màu được đặt ở câu lệnh điều kiện dòng 41
                    #text=self.position[i][j][1]: Đặt chữ xuất hiện trên giao diện là text, với chữ xuất hiện là con số tương ứng trong ma trận position (ví dụ chữ '4' bên phải tại vị trí [0][0] của ma trận position)
                button = tk.Button(self.root, width=8, height=4, bg=color,
                                   text=self.position[i][j][1])
                #B2: Bắt đầu vẽ nút lên giao diện
                    #row=i, column=j: vị trí nút được vẽ, theo như vòng lặp thì các nút sẽ lần lượt đc vẽ theo thứ tự từ trái sang phải, từ trên xuống dưới
                    #padx=2, pady=2: Giãn cách giữa các ô, nếu ko có 2 biến này thì các ô khi vẽ ra sẽ dính sát vào nhau
                button.grid(row=i, column=j, padx=2, pady=2)
                #Thêm nút button đã được tạo vào mảng row ở dòng 38, để tiện lợi thêm vào mảng buttons được khai báo ở __init__
                row.append(button)
            #Lúc này row đã có đủ 3 nút, bắt đầu thêm từng đợt 3 nút đó vào mảng buttons
            self.buttons.append(row)
        
#Giải thích chi tiết dòng if __name__ == "__main__":
#Bên trong mỗi file python đều có sẵn 1 biến đặc biệt là __name__
#Nếu ta chạy file này (8_puzzle.py) trực tiếp, thì __name__ sẽ có giá trị là "__main__"
#Ngược lại, nếu từ trong file khác mà import file này (8_puzzle.py), thì __name__ sẽ có giá trị bằng tên file đó.
#Ví dụ: Nếu từ trong file này mà bấm run code, thì __name__ sẽ bằng "__main__", lúc này sẽ thỏa mãn điều kiện và chạy các câu lệnh bên dưới
#Ngược lại, nếu ta từ file khác (ví dụ như test.py) mà import 8_puzzle.py (kiểu như để gọi lại lớp giao diện eight_puzzle), 
    #thì __name__ sẽ bằng "__test__", như vậy các câu lệnh bên dưới sẽ ko bị gọi và sẽ ko tùy tiện xuất hiện giao diện game 8 puzzle
if __name__ == "__main__":
    #Câu lệnh bắt buộc khi tạo giao diện bằng tkinter, chức năng tạo ra giao diện nền (window) trống rỗng khi chạy chương trình
    root = tk.Tk()
    #Gọi ra lớp eight_puzzle với tham số là root, tức là những gì được vẽ sẽ xuất hiện trên giao diện nền root
    #Mặc dù ở trên khi khai báo class eight_puzzle ko có tham số nhưng ở đây lại có tham số root. 
        #Lý do là tham số root sẽ được truyền thằng vào hàm __init__ chứ ko phải truyền vào lớp eight_puzzle. 
        #Như vậy khi khai báo các biến cần thiết sẽ khai báo trong hàm __init__
    game = eight_puzzle(root)
    #Dòng này gọi là vòng lặp sự kiện của tkinter
    #Giúp giữ cho cửa số window luôn được hiển thì trên màn hình
    #Giúp cửa số có thể lắng nghe các thao tác của người dùng.
    #Nếu ko có dòng này thì khi chạy, cửa số sẽ xuất hiện và lập tức đóng lại ngay trước khi người dùng có thể thấy gì
    root.mainloop()