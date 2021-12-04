import sys
import tkinter as tk
from time import strftime
from tkinter import *
from tkinter import BOTH, END, Frame, Tk

import numpy as np
import pandas as pd
from PIL import Image, ImageTk
pd.set_option('display.max_rows', None)


class formMoFile(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Mở file")
        self.geometry("650x550")
        self.iconbitmap("image/icons8-align-text-left-48.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False, False)

        def open_NV():
            my_text.delete('1.0', END)
            text_file = open("Nhanvien.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def open_CT():
            my_text.delete('1.0', END)
            text_file = open("ChiTiet.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def open_CV():
            my_text.delete('1.0', END)
            text_file = open("HSChucVu.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def open_PB():
            my_text.delete('1.0', END)
            text_file = open("PhongBan.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def clear_text():
            my_text.delete('1.0', END)

        my_text = Text(self, width=70, height=30)
        my_text.pack()

        openNV_btn = Button(self, text="Nhanvien.txt", activebackground="#42a5f5", width=12, height=1, command=open_NV)
        openNV_btn.place(x=40, y=500)
        openCT_btn = Button(self, text="ChiTiet.txt", activebackground="#42a5f5", width=12, height=1, command=open_CT)
        openCT_btn.place(x=160, y=500)
        openCV_btn = Button(self, text="HSChuVu.txt", activebackground="#42a5f5", width=12, height=1, command=open_CV)
        openCV_btn.place(x=280, y=500)
        openPB_btn = Button(self, text="PhongBan.txt", activebackground="#42a5f5", width=12, height=1, command=open_PB)
        openPB_btn.place(x=390, y=500)
        openPB_btn = Button(self, text="Clear", activebackground="#42a5f5", width=12, height=1, command=clear_text)
        openPB_btn.place(x=510, y=500)

List_NhanVien = [('001', 'Lai Van', 'Sam', 0, '01/01/1966', '30/04/1990', 'VP'),
                 ('002', 'Tran Van', 'Minh', 0, '23/02/1965', '10/05/1990', 'VP'),
                 ('003', 'Tong Canh', 'Son', 0, '12/04/1963', '24/10/1996', 'TK'),
                 ('004', 'Ngo Viet', 'Hung', 0, '11/02/1977', '04/06/1997', 'TK'),
                 ('005', 'Mai Tho', 'Loan', 1, '23/05/1970', '08/03/1989', 'TK'),
                 ('006', 'Mac Xuan', 'Tien', 0, '12/04/1963', '28/03/1992', 'TK'),
                 ('007', 'Vu Hoai', 'Anh', 0, '15/06/1968', '09/03/1993', 'KH'),
                 ('008', 'Tran Thanh', 'Khanh', 0, '15/07/1942', '11/10/1985', 'KH'),
                 ('009', 'Nguyen Hong', 'Hanh', 1, '13/01/1962', '06/06/1987', 'KT'),
                 ('010', 'Le Thi', 'Huong', 1, '23/05/1962', '06/06/1988', 'KT'),
                 ('011', 'Lam Quoc', 'Khanh', 0, '21/06/1963', '27/09/1991', 'KT'),
                 ('012', 'Nguyen Hong', 'Van', 1, '11/05/1976', '05/05/1995', 'TK'),
                 ('013', 'Nguyen Minh', 'Quang', 0, '13/06/1951', '05/05/1978', 'VP'),
                 ('014', 'Trang Phi', 'Hung', 0, '23/03/1953', '07/07/1996', 'VP'),
                 ('015', 'Tran Nguyet', 'Minh', 1, '19/09/1963', '10/10/1995', 'VP'),
                 ('016', 'Nguyen Ngoc', 'Hien', 1, '14/03/1961', '08/04/1990', 'VP'),
                 ('017', 'Do Anh', 'Hang', 0, '11/01/1960', '05/05/1979', 'VP'),
                 ('018', 'Dinh Thi', 'Tam', 1, '04/03/1962', '05/05/1995', 'TC'),
                 ('019', 'Nguyen Kim', 'Toan', 1, '01/09/1960', '31/07/1990', 'TC'),
                 ('020', 'Nguyen Bich', 'Lien', 1, '03/03/1969', '16/12/1996', 'TC'),
                 ('021', 'Huynh Bach', 'Tuyet', 1, '07/03/1968', '23/05/1994', 'KH'),
                 ('022', 'Le Phuong', 'Thanh', 1, '12/02/1957', '05/05/1981', 'KH'),
                 ('023', 'Ta The', 'Khanh', 0, '23/05/1969', '15/09/1993', 'KH'),
                 ('024', 'Bui Son', 'Hai', 0, '14/03/1951', '08/05/1990', 'TC'),
                 ('025', 'Luu Vu', 'Cam', 0, '17/06/1970', '22/08/1995', 'TK'),
                 ('026', 'Doan Thi', 'Chi', 0, '12/05/1960', '30/10/1994', 'TC'),
                 ('027', 'Tran Quang', 'Thanh', 0, '14/09/1963', '05/05/1992', 'TK'),
                 ('028', 'Truong Le', 'Xuan', 1, '13/04/1968', '23/05/1994', 'KT'),
                 ('029', 'Nguyen Van', 'Thanh', 0, '02/09/1969', '08/02/1996', 'TC'),
                 ('030', 'Dang Van', 'Thuy', 0, '01/01/1968', '23/08/1992', 'TK'),
                 ('031', 'Nguyen Van', 'Thanh', 0, '02/02/1979', '23/05/1994', 'KH'),
                 ('032', 'Lam Van', 'Tuan', 0, '12/02/1969', '09/09/1993', 'TK'),
                 ('033', 'Hoang Ngoc', 'Thanh', 0, '13/05/1944', '09/03/1978', 'VP'),
                 ('034', 'Nguyen Van', 'Nuoi', 0, '23/04/1970', '02/10/1990', 'TK'),
                 ('035', 'Do Dinh', 'Viet', 0, '12/04/1945', '31/07/1985', 'TC'),
                 ('036', 'Le Trung', 'Binh', 0, '13/04/1977', '30/05/1997', 'TK'),
                 ('037', 'Tran The', 'Duyet', 0, '14/04/1970', '26/04/1996', 'KH'),
                 ('038', 'Le Bich', 'Phuong', 1, '13/03/1974', '04/08/1995', 'KH'),
                 ('039', 'Mai Van', 'Duoc', 0, '14/04/1960', '04/10/1993', 'TC'),
                 ('040', 'Truong Xuan', 'Hong', 0, '15/05/1940', '28/04/1979', 'TC'),
                 ('041', 'Huynh Ngoc', 'Quanh', 0, '23/05/1964', '30/05/1990', 'TK'),
                 ('042', 'Dao Thanh', 'Huong', 1, '12/03/1969', '08/08/1993', 'TK'),
                 ('043', 'Pham Hoai', 'Nam', 1, '15/06/1978', '28/07/1992', 'VP'),
                 ('044', 'Le Thi My', 'Linh', 1, '19/09/1971', '30/05/1995', 'TK'),
                 ('045', 'Pham The', 'Dung', 0, '23/05/1980', '30/12/1997', 'TK'),
                 ('046', 'Hoang Thanh', 'Trang', 1, '12/03/1970', '03/03/1997', 'KT'),
                 ('047', 'Nguyen Van', 'Hien', 0, '15/06/1960', '05/05/1988', 'TK'),
                 ('048', 'Tran Nguyet', 'Nga', 1, '12/07/1965', '26/04/1993', 'TK'),
                 ('049', 'Mai Thi Hong', 'Xuan', 1, '02/06/1962', '09/09/1995', 'VP'),
                 ('050', 'Nguyen Thi', 'Nam', 1, '06/07/1960', '06/06/1987', 'KT'),
                 ('051', 'Ton Thi Thanh', 'Nhan', 1, '14/06/1965', '04/10/1993', 'TC'),
                 ('052', 'Nguyen To', 'Uyen', 1, '05/06/1963', '07/10/1990', 'TK'),
                 ('053', 'Luong Anh', 'Tuyen', 1, '23/01/1975', '02/10/1997', 'KT'),
                 ('054', 'Doan Van', 'Thanh', 0, '24/03/1971', '06/06/1993', 'VP'),
                 ('055', 'Luong Van', 'Chanh', 0, '20/05/1963', '12/01/1997', 'TK'),
                 ('056', 'Truong Tuong', 'Nhat', 0, '25/12/1972', '23/05/1994', 'KH'),
                 ('057', 'Nguyen Xuan', 'Phuong', 0, '14/04/1960', '05/01/1986', 'TK'),
                 ('058', 'Vo Ngoc', 'Quang', 0, '12/02/1960', '07/10/1990', 'TK'),
                 ('059', 'Nguyen Thanh', 'Thuy', 1, '19/05/1960', '07/07/1996', 'TK'),
                 ('060', 'Nguyen Trong', 'Son', 0, '20/05/1941', '22/07/1989', 'KT')]

DF_NhanVien = pd.DataFrame.from_records(List_NhanVien, columns=['MaNV', 'Ho', 'Ten', 'Phai', 'NTNS', 'NgayBatDau', 'MaPB'])
f = open("nhanvien/NhanVien_data.txt", "w")
print(DF_NhanVien, file=f)
f.close()

# <--------------Giao diện nhân viên-------------->
class formNhanVien(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Nhân viên")
        self.geometry("1010x500")
        self.iconbitmap("image/icons8-employee-48_1.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xoa():
            global DF_NhanVien
            my_text.delete("1.0", END)
            DF_NhanVien.drop(DF_NhanVien.index[[int(tb_xoa.get())]], inplace=True)
            DF_NhanVien.reset_index(inplace=True, drop=True)

            f = open("nhanvien/NhanVien_xoa.txt", "w+")
            print(DF_NhanVien, file=f)
            f.close()

            text_file = open("nhanvien/NhanVien_xoa.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_xoa.delete(0, END)

        # https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value):
            # Starting value of upper half
            start_upper = 0
            # End value of upper half
            end_upper = row_number
            # Start value of lower half
            start_lower = row_number
            # End value of lower half
            end_lower = df.shape[0]
            # Create a list of upper_half index
            upper_half = [*range(start_upper, end_upper, 1)]
            # Create a list of lower_half index
            lower_half = [*range(start_lower, end_lower, 1)]
            # Increment the value of lower half by 1
            lower_half = [x.__add__(1) for x in lower_half]
            # Combine the two lists
            index_ = upper_half + lower_half
            # Update the index of the dataframe
            df.index = index_
            # Insert a row at the end
            df.loc[row_number] = row_value
            # Sort the index labels
            df = df.sort_index()
            # return the dataframe
            return df

        def chenTruoc():
            global DF_NhanVien
            my_text.delete("1.0", END)
            id = tb_maNV.get()
            hoTenDem = tb_hoTenDem.get()
            ten = tb_ten.get()
            phai = tb_phai.get()
            ngaySinh = tb_ngaySinh.get()
            ngayBatDau = tb_ngayBatDau.get()
            maPB = tb_maPB.get()
            input_data = [id, hoTenDem, ten, phai, ngaySinh, ngayBatDau, maPB]
            DF_NhanVien = Insert_row(int(tb_chenTruoc.get()), DF_NhanVien, input_data)
            DF_NhanVien.reset_index(inplace=True, drop=True)

            f = open("nhanvien/NhanVien_chenTruoc.txt", "w+")
            print(DF_NhanVien, file=f)
            f.close()

            text_file = open("nhanvien/NhanVien_chenTruoc.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_maNV.delete(0, END)
            tb_hoTenDem.delete(0, END)
            tb_ten.delete(0, END)
            tb_phai.delete(0, END)
            tb_ngaySinh.delete(0, END)
            tb_ngayBatDau.delete(0, END)
            tb_maPB.delete(0, END)
            tb_chenTruoc.delete(0, END)

        def chenSau():
            global DF_NhanVien
            my_text.delete("1.0", END)
            id = tb_maNV.get()
            hoTenDem = tb_hoTenDem.get()
            ten = tb_ten.get()
            phai = tb_phai.get()
            ngaySinh = tb_ngaySinh.get()
            ngayBatDau = tb_ngayBatDau.get()
            maPB = tb_maPB.get()
            input_data = [id, hoTenDem, ten, phai, ngaySinh, ngayBatDau, maPB]
            DF_NhanVien = Insert_row(int(tb_chenSau.get()) + 1, DF_NhanVien, input_data)
            DF_NhanVien.reset_index(inplace=True, drop=True)

            f = open("nhanvien/NhanVien_chenSau.txt", "w+")
            print(DF_NhanVien, file=f)
            f.close()

            text_file = open("nhanvien/NhanVien_chenSau.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_maNV.delete(0, END)
            tb_hoTenDem.delete(0, END)
            tb_ten.delete(0, END)
            tb_phai.delete(0, END)
            tb_ngaySinh.delete(0, END)
            tb_ngayBatDau.delete(0, END)
            tb_maPB.delete(0, END)
            tb_chenTruoc.delete(0, END)


        # Lable data
        lb_data = tk.LabelFrame(self, padx=20, pady=15, text="Bảng nhân viên")
        lb_data.place(x=10, y=10)

        my_text = tk.Text(lb_data, width=68)
        my_text.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        text_file = open("nhanvien/NhanVien_data.txt", "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #Lable clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=650, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=650, y=50)

        tk.Label(lb_info, text="Mã nhân viên").grid(row=0, column=0,sticky='W')
        tb_maNV = tk.Entry(lb_info)
        tb_maNV.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Họ & tên đệm").grid(row=1, column=0,sticky='W')
        tb_hoTenDem = tk.Entry(lb_info)
        tb_hoTenDem.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Tên").grid(row=2, column=0,sticky='W')
        tb_ten = tk.Entry(lb_info)
        tb_ten.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Phái").grid(row=3, column=0,sticky='W')
        tb_phai = tk.Entry(lb_info)
        tb_phai.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Ngày sinh").grid(row=4, column=0,sticky='W')
        tb_ngaySinh = tk.Entry(lb_info)
        tb_ngaySinh.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Ngày bắt đầu").grid(row=5, column=0,sticky='W')
        tb_ngayBatDau = tk.Entry(lb_info)
        tb_ngayBatDau.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Mã phòng ban").grid(row=6, column=0,sticky='W')
        tb_maPB = tk.Entry(lb_info)
        tb_maPB.grid(row=6, column=1, sticky=tk.W, padx=6, pady=5, ipadx=50)

        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=650, y=310)

        tk.Label(lb_control, text="Xóa nhân viên thứ").grid(row=0, column=0,sticky='W')
        tb_xoa = tk.Spinbox(lb_control, from_=0, to_=sys.maxsize, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Chèn trước nhân viên thứ:").grid(row=1, column=0,sticky='W')
        tb_chenTruoc = tk.Spinbox(lb_control, from_=0, to_=sys.maxsize, width=10)
        tb_chenTruoc.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Chèn sau nhân viên thứ:").grid(row=2, column=0,sticky='W')
        tb_chenSau = tk.Spinbox(lb_control, from_=0, to_=sys.maxsize, width=10)
        tb_chenSau.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)

        btn_chenTruoc = tk.Button(lb_control, text="Chèn trước", width=8, height=1, command=chenTruoc)
        btn_chenTruoc.grid(row=1, column=2, padx=7)

        btn_chenSau = tk.Button(lb_control, text="Chèn sau", width=8, height=1, command=chenSau)
        btn_chenSau.grid(row=2, column=2, padx=7)


List_HSChucVu = [('GD', 3.00),('NV', 1.00),('PGD', 2.20),('PP', 1.50),
                 ('TK', 1.20),('TL', 1.50),('TP', 2.00),('TX', 1.20)]

DF_HSChucVu = pd.DataFrame.from_records(List_HSChucVu, columns=['ChucVu', 'HSCV'])
f = open("chucvu/HSChucVu_data.txt", "w")
print(DF_HSChucVu, file=f)
f.close()

# <--------------Giao diện chức vụ-------------->
class formChucVu(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Chức vụ")
        self.geometry("655x260")
        self.iconbitmap("image/icons8-table-48.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xoa():
            global DF_HSChucVu
            my_text.delete("1.0", END)

            DF_HSChucVu.drop(DF_HSChucVu.index[int(tb_xoa.get())], inplace=True)
            DF_HSChucVu.reset_index(inplace=True, drop=True)

            f = open("chucvu/HSChucVu_xoa.txt", "w+")
            print(DF_HSChucVu, file=f)
            f.close()

            text_file = open("chucvu/HSChucVu_xoa.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_xoa.delete(0, END)

        # https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value):
            # Starting value of upper half
            start_upper = 0
            # End value of upper half
            end_upper = row_number
            # Start value of lower half
            start_lower = row_number
            # End value of lower half
            end_lower = df.shape[0]
            # Create a list of upper_half index
            upper_half = [*range(start_upper, end_upper, 1)]
            # Create a list of lower_half index
            lower_half = [*range(start_lower, end_lower, 1)]
            # Increment the value of lower half by 1
            lower_half = [x.__add__(1) for x in lower_half]
            # Combine the two lists
            index_ = upper_half + lower_half
            # Update the index of the dataframe
            df.index = index_
            # Insert a row at the end
            df.loc[row_number] = row_value
            # Sort the index labels
            df = df.sort_index()
            # return the dataframe
            return df

        def chenTruoc():
            global DF_HSChucVu
            my_text.delete("1.0", END)

            input_data = [tb_chucVu.get(), tb_hsCongViec.get()]
            DF_HSChucVu = Insert_row(int(tb_chenTruoc.get()), DF_HSChucVu, input_data)
            DF_HSChucVu.reset_index(inplace=True, drop=True)

            f = open("chucvu/HSChucVu_chenTruoc.txt", "w+")
            print(DF_HSChucVu, file=f)
            f.close()

            text_file = open("chucvu/HSChucVu_chenTruoc.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_chucVu.delete(0, END)
            tb_hsCongViec.delete(0, END)
            tb_chenTruoc.delete(0, END)

        def chenSau():
            global DF_HSChucVu
            my_text.delete("1.0", END)

            input_data = [tb_chucVu.get(), tb_hsCongViec.get()]
            DF_HSChucVu = Insert_row(int(tb_chenSau.get()) + 1, DF_HSChucVu, input_data)
            DF_HSChucVu.reset_index(inplace=True, drop=True)

            f = open("chucvu/HSChucVu_chenSau.txt", "w+")
            print(DF_HSChucVu, file=f)
            f.close()

            text_file = open("chucvu/HSChucVu_chenSau.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_chucVu.delete(0, END)
            tb_hsCongViec.delete(0, END)
            tb_chenSau.delete(0, END)

        # Label data
        lb_data = tk.LabelFrame(self, text="Chức Vụ")
        lb_data.place(x=10, y=10)

        my_text = tk.Text(lb_data, width=25, height=12)
        my_text.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        text_file = open("chucvu/HSChucVu_data.txt", "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=250, y=10)
        clock()

        #Label information
        lb_info = tk.LabelFrame(self, padx=20, pady=15, text="Thông tin")
        lb_info.place(x=250, y=50)

        tk.Label(lb_info, text="Chức Vụ").grid(row=0, column=0,sticky='W')
        tb_chucVu = tk.Entry(lb_info)
        tb_chucVu.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Hệ số công việc").grid(row=1, column=0,sticky='W')
        tb_hsCongViec = tk.Entry(lb_info)
        tb_hsCongViec.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Label control
        tk.Label(lb_info, text="Xóa mẫu tin thứ:").grid(row=2, column=0,sticky='W')
        tb_xoa = tk.Spinbox(lb_info, from_=0, to_=sys.maxsize)
        tb_xoa.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Chèn trước mẫu tin số:").grid(row=3, column=0,sticky='W')
        tb_chenTruoc = tk.Spinbox(lb_info, from_=0, to_=sys.maxsize)
        tb_chenTruoc.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Chèn sau mẫu tin số:").grid(row=4, column=0,sticky='W')
        tb_chenSau = tk.Spinbox(lb_info, from_=0, to_=sys.maxsize)
        tb_chenSau.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

        btn_xoa = tk.Button(lb_info, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=2, column=2, padx=5.5)

        btn_chenTruoc = tk.Button(lb_info, text="Chèn trước", width=8, height=1, command=chenTruoc)
        btn_chenTruoc.grid(row=3, column=2, padx=5.5)

        btn_chenSau = tk.Button(lb_info, text="Chèn sau", width=8, height=1, command=chenSau)
        btn_chenSau.grid(row=4, column=2, padx=5.5)

List_PhongBan = [('KH','Phong Kinh te Ke hoach'),
                ('KT','Phong Ke toan Tai chanh'),
                ('TC','Phong To chuc Nhan so'),
                ('TK','Phong Ky thuat Thiet ke'),
                ('VP','Van phong Xi nghiep')]
df_Phongban = pd.DataFrame.from_records(List_PhongBan, columns=['MaPB','TenPB'])
f=open("phongban/PhongBan_data.txt","w")
print(df_Phongban,file=f)
f.close()

# <----------------------Gia diện phòng ban---------------------->

class formPhongBan(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Phòng ban")
        self.geometry("750x325")
        self.iconbitmap("image/icons8-room-48_1.ico")
        self.configure(bg='#ffff8d')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=350, y=10)
        clock()

        # tạo label cho thao tác và các btn
        label_inf = tk.LabelFrame(self, padx=20, pady=15, text="Thông tin")
        label_inf.place(x=350, y=80)

        # label ma phòng ban
        tk.Label(label_inf, text="Mã phòng ban").grid(row=0, column=0)
        tb_maPB = tk.Entry(label_inf)
        tb_maPB.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        # label tên phongf ban
        tk.Label(label_inf, text="Tên phòng ban").grid(row=1, column=0)
        tb_tenPB = tk.Entry(label_inf)
        tb_tenPB.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn xoa
        tk.Label(label_inf, text="Vị trí muốn xóa").grid(row=2, column=0)
        tb_xoa = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_xoa.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn chen trc
        tk.Label(label_inf, text="Vị trí muốn thêm trước").grid(row=3, column=0)
        tb_chenTruoc = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_chenTruoc.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn chen sau
        tk.Label(label_inf, text="Vị trí muốn thêm sau").grid(row=4, column=0)
        tb_chenSau = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_chenSau.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng phòng ban")
        label_data.place(x=10, y=10)

        my_text = tk.Text(label_data, height=15, width=35)
        my_text.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
        text_file = open("phongban/PhongBan_data.txt", "r")
        stuff = text_file.read()
        my_text.delete(1.0, END)
        my_text.insert(END, stuff)
        text_file.close()

        # function xóa


        def xoa():
            global df_Phongban
            df_Phongban.drop(df_Phongban.index[[int(tb_xoa.get())]],inplace=True)
            df_Phongban.reset_index(drop=True, inplace=True)

            my_text.delete(1.0, END)
            f = open("phongban/PhongBan_xoa.txt", "w+")
            print(df_Phongban, file=f)
            f.close()

            text_file = open("phongban/PhongBan_xoa.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
            
            # Xóa giá trị trong textbox:
            tb_xoa.delete(0, END)

        # btn xóa
        btn_xoa = tk.Button(label_inf, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=6, column=0, padx=5.5)

        # function thêm
        # Hàm chèn dòng bất kỳ
        # https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value):
            # Starting value of upper half
            start_upper = 0
            # End value of upper half
            end_upper = row_number
            # Start value of lower half
            start_lower = row_number
            # End value of lower half
            end_lower = df.shape[0]
            # Create a list of upper_half index
            upper_half = [*range(start_upper, end_upper, 1)]
            # Create a list of lower_half index
            lower_half = [*range(start_lower, end_lower, 1)]
            # Increment the value of lower half by 1
            lower_half = [x.__add__(1) for x in lower_half]
            # Combine the two lists
            index_ = upper_half + lower_half
            # Update the index of the dataframe
            df.index = index_
            # Insert a row at the end
            df.loc[row_number] = row_value
            # Sort the index labels
            df = df.sort_index()
            # return the dataframe
            return df

        def chenTruoc():
            global df_Phongban
            intput_data = [tb_maPB.get(), tb_tenPB.get()]
            df_Phongban = Insert_row(int(tb_chenTruoc.get()), df_Phongban, intput_data)
            df_Phongban.reset_index(drop=True, inplace=True)

            my_text.delete("1.0", END)
            f = open("phongban/PhongBan_chenTruoc.txt", "w+")
            print(df_Phongban, file=f)
            f.close()
            # đọc lại file vào textbox
            text_file = open("phongban/PhongBan_chenTruoc.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            # xóa text field sau khi thêm thông tin
            tb_chenTruoc.delete(0, END)
            tb_maPB.delete(0, END)
            tb_tenPB.delete(0, END)

        # btn chèn trước
        btn_chenTruoc = tk.Button(label_inf, text="Chèn trước", width=8, height=1, command=chenTruoc)
        btn_chenTruoc.grid(row=6, column=1, padx=5.5)

        def chenSau():
            global df_Phongban
            intput_data = [tb_maPB.get(), tb_tenPB.get()]
            df_Phongban = Insert_row(int(tb_chenSau.get()) + 1, df_Phongban, intput_data)
            df_Phongban.reset_index(drop=True, inplace=True)

            my_text.delete("1.0", END)
            f = open("phongban/PhongBan_chenSau.txt", "w+")
            print(df_Phongban, file=f)
            f.close()
            # đọc lại file vào textbox
            text_file = open("phongban/PhongBan_chenSau.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
            # xóa text field sau khi thêm thông tin
            tb_chenSau.delete(0, END)
            tb_maPB.delete(0, END)
            tb_tenPB.delete(0, END)

        # btn chèn sau
        btn_chenSau = tk.Button(label_inf, text="Chèn Sau", width=8, height=1, command=chenSau)
        btn_chenSau.grid(row=6, column=2, padx=5.5)


List_ChiTiet = [('001', 'NV', 4, 'C1'), ('002', 'NV', 5, 'C3'), ('003', 'NV', 3, 'C2'), ('004', 'NV', 2, 'C1'),
                ('005', 'NV', 6, 'C3'),
                ('006', 'TL', 6, 'B2'), ('007', 'PP', 5, 'B2'), ('008', 'PGD', 7, 'A2'), ('009', 'PP', 7, 'B2'),
                ('010', 'NV', 6, 'C3'),
                ('011', 'NV', 5, 'C2'), ('012', 'NV', 4, 'C3'), ('013', 'NV', 7, 'C3'), ('014', 'TX', 4, 'B3'),
                ('015', 'TK', 4, 'C2'),
                ('016', 'NV', 5, 'C1'), ('017', 'PP', 8, 'B2'), ('018', 'NV', 3, 'C2'), ('019', 'PGD', 7, 'A2'),
                ('020', 'TK', 4, 'C2'),
                ('021', 'TL', 5, 'B2'), ('022', 'TP', 7, 'A3'), ('023', 'NV', 4, 'C2'), ('024', 'NV', 4, 'C3'),
                ('025', 'NV', 3, 'C3'),
                ('026', 'TL', 4, 'B2'), ('027', 'TX', 5, 'B3'), ('028', 'NV', 7, 'C3'), ('029', 'NV', 3, 'C3'),
                ('030', 'NV', 3, 'C3'),
                ('031', 'NV', 4, 'C2'), ('032', 'PP', 6, 'B3'), ('033', 'TP', 7, 'A3'), ('034', 'NV', 5, 'C3'),
                ('035', 'PP', 6, 'B3'),
                ('036', 'TK', 4, 'B1'), ('037', 'NV', 3, 'C2'), ('038', 'TK', 4, 'B1'), ('039', 'NV', 4, 'C2'),
                ('040', 'TP', 7, 'A3'),
                ('041', 'PGD', 8, 'A2'), ('042', 'NV', 5, 'C3'), ('043', 'TK', 4, 'B1'), ('044', 'NV', 4, 'C3'),
                ('045', 'NV', 3, 'C1'),
                ('046', 'NV', 2, 'C1'), ('047', 'TP', 8, 'A2'), ('048', 'NV', 5, 'C3'), ('049', 'NV', 3, 'C2'),
                ('050', 'NV', 6, 'C3'),
                ('051', 'NV', 4, 'C2'), ('052', 'PP', 7, 'B3'), ('053', 'NV', 2, 'C2'), ('054', 'NV', 4, 'C2'),
                ('055', 'NV', 3, 'C2'),
                ('056', 'NV', 4, 'C3'), ('057', 'GD', 9, 'A3'), ('058', 'NV', 4, 'C3'), ('059', 'NV', 3, 'C1'),
                ('060', 'TP', 7, 'A3')]
DF_ChiTiet = pd.DataFrame.from_records(List_ChiTiet, columns=['MaNV', 'ChucVu', 'HSLuong', 'MucDoCV'])
f = open("chitiet/Chitiet_data.txt", "w")
print(DF_ChiTiet, file=f)
f.close()

class formChiTiet(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Chi tiết")
        self.geometry("755x400")
        self.iconbitmap("image/icons8-more-details-48.ico")
        self.configure(bg='#ffff8d')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=348, y=5)
        clock()
        # tạo label cho thao tác và các btn
        label_inf = tk.LabelFrame(self, padx=20, pady=15, text="Thông tin")
        label_inf.place(x=350, y=45)

        # label mã NV
        tk.Label(label_inf, text="Mã nhân viên").grid(row=0, column=0)
        tb_maNV = tk.Entry(label_inf)
        tb_maNV.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        # label chức vụ
        tk.Label(label_inf, text="Chức vụ").grid(row=1, column=0)
        tb_CV = tk.Entry(label_inf)
        tb_CV.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        # label hệ số lương
        tk.Label(label_inf, text="Hệ số lương").grid(row=2, column=0)
        tb_HSLuong = tk.Entry(label_inf)
        tb_HSLuong.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        # label mức độ công việc
        tk.Label(label_inf, text="Mức độ CV").grid(row=3, column=0)
        tb_MucdoCV = tk.Entry(label_inf)
        tb_MucdoCV.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn xoa
        tk.Label(label_inf, text="Vị trí muốn xóa").grid(row=4, column=0)
        tb_xoa = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_xoa.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn chen trc
        tk.Label(label_inf, text="Vị trí muốn thêm trước").grid(row=5, column=0)
        tb_chenTruoc = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_chenTruoc.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn chen sau
        tk.Label(label_inf, text="Vị trí muốn thêm sau").grid(row=6, column=0)
        tb_chenSau = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_chenSau.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=20, text="Bảng chi tiết")
        label_data.place(x=10, y=10)

        my_text = tk.Text(label_data, height=15, width=35)
        my_text.grid(row=0, column=0, sticky=tk.W, pady=15, padx=10)
        text_file = open("chitiet/Chitiet_data.txt", "r")
        stuff = text_file.read()
        my_text.delete(1.0, END)
        my_text.insert(END, stuff)
        text_file.close()

        def xoa():
            global DF_ChiTiet
            DF_ChiTiet.drop(DF_ChiTiet.index[[int(tb_xoa.get())]], inplace=True)
            DF_ChiTiet.reset_index(drop=True, inplace=True)

            my_text.delete(1.0, END)
            f = open("chitiet/Chitiet_xoa.txt", "w+")
            print(DF_ChiTiet, file=f)
            f.close()

            text_file = open("chitiet/Chitiet_xoa.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
            # Xóa giá trị trong textbox:
            tb_xoa.delete(0, END)

        # btn xóa
        btn_xoa = tk.Button(label_inf, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=7, column=0, padx=5.5)

        # Hàm chèn dòng bất kỳ
        # https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value):
            # Starting value of upper half
            start_upper = 0
            # End value of upper half
            end_upper = row_number
            # Start value of lower half
            start_lower = row_number
            # End value of lower half
            end_lower = df.shape[0]
            # Create a list of upper_half index
            upper_half = [*range(start_upper, end_upper, 1)]
            # Create a list of lower_half index
            lower_half = [*range(start_lower, end_lower, 1)]
            # Increment the value of lower half by 1
            lower_half = [x.__add__(1) for x in lower_half]
            # Combine the two lists
            index_ = upper_half + lower_half
            # Update the index of the dataframe
            df.index = index_
            # Insert a row at the end
            df.loc[row_number] = row_value
            # Sort the index labels
            df = df.sort_index()
            # return the dataframe
            return df

        def chenTruoc():
            global DF_ChiTiet
            intput_data = [tb_maNV.get(), tb_CV.get(), tb_HSLuong.get(), tb_MucdoCV.get()]
            DF_ChiTiet = Insert_row(int(tb_chenTruoc.get()), DF_ChiTiet, intput_data)
            DF_ChiTiet.reset_index(drop=True,inplace=True)

            my_text.delete("1.0", END)
            f = open("chitiet/Chitiet_chenTruoc.txt", "w+")
            print(DF_ChiTiet, file=f)
            f.close()
            # đọc lại file vào textbox
            text_file = open("chitiet/Chitiet_chenTruoc.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            # xóa text field sau khi thêm thông tin
            tb_chenTruoc.delete(0, END)
            tb_maNV.delete(0, END)
            tb_CV.delete(0, END)
            tb_MucdoCV.delete(0, END)
            tb_HSLuong.delete(0, END)

        # btn chèn trước
        btn_chenTruoc = tk.Button(label_inf, text="Chèn trước", width=8, height=1, command=chenTruoc)
        btn_chenTruoc.grid(row=7, column=1, padx=5.5)

        def chenSau():
            global DF_ChiTiet
            intput_data = [tb_maNV.get(), tb_CV.get(), tb_HSLuong.get(), tb_MucdoCV.get()]
            DF_ChiTiet = Insert_row(int(tb_chenSau.get()) + 1, DF_ChiTiet, intput_data)
            DF_ChiTiet.reset_index(drop=True, inplace=True)

            my_text.delete("1.0", END)
            f = open("chitiet/Chitiet_chenSau.txt", "w+")
            print(DF_ChiTiet, file=f)
            f.close()
            # đọc lại file vào textbox
            text_file = open("chitiet/Chitiet_chenSau.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
            # xóa text field sau khi thêm thông tin
            tb_chenSau.delete(0, END)
            tb_maNV.delete(0, END)
            tb_CV.delete(0, END)
            tb_MucdoCV.delete(0, END)
            tb_HSLuong.delete(0, END)

        # btn chèn sau
        btn_chenSau = tk.Button(label_inf, text="Chèn Sau", width=8, height=1, command=chenSau)
        btn_chenSau.grid(row=7, column=2, padx=5.5)
# <----------------------Gia diện lương nhân viên---------------------->
class formLuong(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Lương nhân viên")
        self.geometry("910x480")
        self.iconbitmap("image/icons8-cash-in-hand-48.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def tinhLuong():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])

            DF_TinhLuong = DF_Fields.apply(lambda x: x*250000 if x.name == 'HSLuong' else x)
            #https://www.geeksforgeeks.org/how-to-sort-a-pandas-dataframe-by-multiple-columns-in-python/
            DF_SapXep = DF_TinhLuong.sort_values(by=["MaPB","MaNV"])

            DF_DoiTenField = DF_SapXep.rename({'HSLuong': 'Luong'},axis=1)
            f = open("luong/TinhLuong.txt", "w+")
            print(DF_DoiTenField, file=f)
            f.close()

            text_file = open("luong/TinhLuong.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def luongCaoNhat():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])

            DF_TinhLuong = DF_Fields.apply(lambda x: x*250000 if x.name == 'HSLuong' else x)
            DF_DoiTenField = DF_TinhLuong.rename({'HSLuong': 'Luong'},axis=1)
            #https://www.geeksforgeeks.org/how-to-sort-a-pandas-dataframe-by-multiple-columns-in-python/
            DF_SapXepGiam = DF_DoiTenField.sort_values(by=["Luong"], ascending=False)
            DF_LuongCaoNhat = DF_SapXepGiam.head(20)
            f = open("luong/TopLuongCaoNhat.txt", "w+")
            print(DF_LuongCaoNhat, file=f)
            f.close()

            text_file = open("luong/TopLuongCaoNhat.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def luongCaoNhatPhongBan():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])

            DF_TinhLuong = DF_Fields.apply(lambda x: x * 250000 if x.name == 'HSLuong' else x)
            DF_DoiTenField = DF_TinhLuong.rename({'HSLuong': 'Luong'}, axis=1)
            # https://www.geeksforgeeks.org/how-to-sort-a-pandas-dataframe-by-multiple-columns-in-python/
            DF_SapXepGiam = DF_DoiTenField.sort_values(by=["Luong"], ascending=False)

            #https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values
            DF_LuongPhongKH = DF_SapXepGiam.loc[DF_SapXepGiam['MaPB']=='KH']
            mucLuongCaoNhatKH = DF_LuongPhongKH["Luong"].max()
            DF_LuongCaoNhatPhongKH = DF_LuongPhongKH.loc[DF_LuongPhongKH['Luong']==mucLuongCaoNhatKH]

            DF_LuongPhongKT = DF_SapXepGiam.loc[DF_SapXepGiam['MaPB']=='KT']
            mucLuongCaoNhatKT = DF_LuongPhongKT["Luong"].max()
            DF_LuongCaoNhatPhongKT = DF_LuongPhongKT.loc[DF_LuongPhongKT['Luong']==mucLuongCaoNhatKT]

            DF_LuongPhongTC = DF_SapXepGiam.loc[DF_SapXepGiam['MaPB']=='TC']
            mucLuongCaoNhatTC = DF_LuongPhongTC["Luong"].max()
            DF_LuongCaoNhatPhongTC = DF_LuongPhongTC.loc[DF_LuongPhongTC['Luong']==mucLuongCaoNhatTC]

            DF_LuongPhongTK = DF_SapXepGiam.loc[DF_SapXepGiam['MaPB']=='TK']
            mucLuongCaoNhatTK = DF_LuongPhongTK["Luong"].max()
            DF_LuongCaoNhatPhongTK = DF_LuongPhongTK.loc[DF_LuongPhongTK['Luong']==mucLuongCaoNhatTK]

            DF_LuongPhongVP = DF_SapXepGiam.loc[DF_SapXepGiam['MaPB']=='VP']
            mucLuongCaoNhatVP = DF_LuongPhongVP["Luong"].max()
            DF_LuongCaoNhatPhongVP = DF_LuongPhongVP.loc[DF_LuongPhongVP['Luong']==mucLuongCaoNhatVP]

            DF_LuongCaoNhatTheoPhong = pd.concat([DF_LuongCaoNhatPhongKH,DF_LuongCaoNhatPhongKT,DF_LuongCaoNhatPhongTC, DF_LuongCaoNhatPhongTK, DF_LuongCaoNhatPhongVP])

            f = open("luong/LuongCaoNhatTheoPhong.txt", "w+")
            print(DF_LuongCaoNhatTheoPhong, file=f)
            f.close()

            text_file = open("luong/LuongCaoNhatTheoPhong.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        # Label data
        lb_data = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_data.place(x=10, y=10)
        my_text = tk.Text(lb_data, width=60)
        my_text.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

        DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
        fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])

        f = open("luong/Luong_data.txt", "w+")
        print(fields, file=f)
        f.close()

        text_file = open("luong/Luong_data.txt", "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=545, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=15, text="Chức năng")
        lb_control.place(x=545, y=60)

        tk.Label(lb_control, text="Tính lương nhân viên").grid(row=0, column=0,sticky='W')
        tk.Label(lb_control, text="Top 20 nhân viên có lương cao").grid(row=1, column=0,sticky='W')
        tk.Label(lb_control, text="Top nhân viên có lương cao nhất của mỗi phòng").grid(row=2, column=0,sticky='W')

        btn_Luong = tk.Button(lb_control, text="Tính", command=tinhLuong, width=8,height=1, background="green", foreground="white")
        btn_Luong.grid(row=0, column=1,pady=2, padx=2)
        btn_Luong = tk.Button(lb_control, text="Xem", command=luongCaoNhat, width=8,height=1, background="green", foreground="white")
        btn_Luong.grid(row=1, column=1,pady=2, padx=2)
        btn_Luong = tk.Button(lb_control, text="Xem", command=luongCaoNhatPhongBan, width=8,height=1, background="green", foreground="white")
        btn_Luong.grid(row=2, column=1, pady=2, padx=2)


# <----------------------Gia diện thống kê---------------------->

class formThongKe(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Thống kê")
        self.geometry("750x325")
        self.iconbitmap("image/icons8-total-sales-48.ico")
        self.configure(bg='#ffff8d')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=480, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=60, pady=15, text="Chức năng")
        lb_control.place(x=475, y=60)
        tk.Label(lb_control, text="Thống kê").grid(row=0, column=0, sticky='W')

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng Thống Kê")
        label_data.place(x=10, y=10)

        def ThongKe():
            df_NV_PB = df_Phongban.merge(DF_NhanVien)
            # KH departmant
            df_KH = df_NV_PB.loc[df_NV_PB['MaPB'] == 'KH']
            tong_KH = len(df_KH)
            KH_Nam = df_KH.loc[df_KH['Phai'] == 0]
            tong_KH_Nam = len(KH_Nam)
            tong_KH_Nu = tong_KH - tong_KH_Nam

            # KT departmant
            df_KT = df_NV_PB.loc[df_NV_PB['MaPB'] == 'KT']
            tong_KT = len(df_KT)
            KT_Nam = df_KT.loc[df_KT['Phai'] == 0]
            tong_KT_Nam = len(KT_Nam)
            tong_KT_Nu = tong_KT - tong_KT_Nam

            # TC departmant
            df_TC = df_NV_PB.loc[df_NV_PB['MaPB'] == 'TC']
            tong_TC = len(df_TC)
            TC_Nam = df_TC.loc[df_TC['Phai'] == 0]
            tong_TC_Nam = len(TC_Nam)
            tong_TC_Nu = tong_TC - tong_TC_Nam

            # TK departmant
            df_TK = df_NV_PB.loc[df_NV_PB['MaPB'] == 'TK']
            tong_TK = len(df_TK)
            TK_Nam = df_TK.loc[df_TK['Phai'] == 0]
            tong_TK_Nam = len(TK_Nam)
            tong_TK_Nu = tong_TK - tong_TK_Nam

            # VP departmant
            df_VP = df_NV_PB.loc[df_NV_PB['MaPB'] == 'VP']
            tong_VP = len(df_VP)
            VP_Nam = df_VP.loc[df_VP['Phai'] == 0]
            tong_VP_Nam = len(VP_Nam)
            tong_VP_Nu = tong_VP - tong_VP_Nam

            # tao list
            list_test = [('Phong Kinh te Ke hoach', tong_KH_Nam, tong_KH_Nu, tong_KH),
                         ('Phong Ke toan Tai chinh', tong_KT_Nam, tong_KT_Nu, tong_KT),
                         ('Phong To chuc Nhan so', tong_TC_Nam, tong_TC_Nu, tong_TC),
                         ('Phong Ky thuat Thiet ke', tong_TK_Nam, tong_TK_Nu, tong_TK),
                         ('Van phong Xi nghiep', tong_VP_Nam, tong_VP_Nu, tong_VP)]
            df_lst = pd.DataFrame.from_records(list_test, columns=['TenPB', 'sonam', 'tongnu', 'tong'])

            f = open("thongke/ThongKe.txt", "w+")
            print(df_lst, file=f)
            f.close()

            my_text.delete(1.0, END)
            text_file = open("thongke/ThongKe.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        btn_ThongKe = tk.Button(lb_control, text="Thống kê", command=ThongKe, width=8, height=1, background="green",foreground="white")
        btn_ThongKe.grid(row=0, column=1, pady=2, padx=2)

        my_text = tk.Text(label_data, height=15, width=50)
        my_text.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)


# <----------------------Gia diện tổng kết---------------------->

class formTongKet(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Tổng kết")
        self.geometry("910x600")
        self.iconbitmap("image/icons8-brief-48.ico")
        self.configure(bg='#ffff8d')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=700, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=55, pady=15, text="Chức năng")
        lb_control.place(x=633, y=60)
        tk.Label(lb_control, text="Mã phòng ban:").grid(row=0, column=0, sticky='W')

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng Tổng kết")
        label_data.place(x=20, y=15)

        def tinhLuongTongKet_KH():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])
            DF_TinhLuong = DF_Fields.apply(lambda x: x * 250000 if x.name == 'HSLuong' else x)
            DF_DoiTenField = DF_TinhLuong.rename({'HSLuong': 'Luong'}, axis=1)
            DF_DoiTenField = DF_DoiTenField.loc[DF_DoiTenField['MaPB'] == 'KH']

            tong_NV_KH = len(DF_DoiTenField)
            KH_Nam = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 0]
            tong_nam_KH = len(KH_Nam)
            KH_Nu = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 1]
            tong_nu_KH = len(KH_Nu)
            tong_KH = sum(DF_DoiTenField['Luong'])

            f = open("tongket/TinhLuongTongKet_KH.txt", "w+")
            print(DF_DoiTenField, file=f)
            print("Tong Nhan vien : ", tong_NV_KH, file=f)
            print("Tong so Nam    : ", tong_nam_KH, file=f)
            print("Tong so Nu     : ", tong_nu_KH, file=f)
            print("Tong Luong     : ", tong_KH, file=f)
            f.close()

            text_file = open("tongket/TinhLuongTongKet_KH.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def tinhLuongTongKet_KT():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])
            DF_TinhLuong = DF_Fields.apply(lambda x: x * 250000 if x.name == 'HSLuong' else x)
            DF_DoiTenField = DF_TinhLuong.rename({'HSLuong': 'Luong'}, axis=1)
            DF_DoiTenField = DF_DoiTenField.loc[DF_DoiTenField['MaPB'] == 'KT']

            tong_NV_KT = len(DF_DoiTenField)
            KT_Nam = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 0]
            tong_nam_KT = len(KT_Nam)
            KT_Nu = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 1]
            tong_nu_KT = len(KT_Nu)
            tong_KT = sum(DF_DoiTenField['Luong'])

            f = open("tongket/TinhLuongTongKet_KT.txt", "w+")
            print(DF_DoiTenField, file=f)
            print("Tong Nhan vien : ", tong_NV_KT, file=f)
            print("Tong so Nam    : ", tong_nam_KT, file=f)
            print("Tong so Nu     : ", tong_nu_KT, file=f)
            print("Tong Luong     : ", tong_KT, file=f)
            f.close()

            text_file = open("tongket/TinhLuongTongKet_KT.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def tinhLuongTongKet_TC():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])
            DF_TinhLuong = DF_Fields.apply(lambda x: x * 250000 if x.name == 'HSLuong' else x)
            DF_DoiTenField = DF_TinhLuong.rename({'HSLuong': 'Luong'}, axis=1)
            DF_DoiTenField = DF_DoiTenField.loc[DF_DoiTenField['MaPB'] == 'TC']

            tong_NV_TC = len(DF_DoiTenField)
            TC_Nam = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 0]
            tong_nam_TC = len(TC_Nam)
            TC_Nu = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 1]
            tong_nu_TC = len(TC_Nu)
            tong_TC = sum(DF_DoiTenField['Luong'])

            f = open("tongket/TinhLuongTongKet_TC.txt", "w+")
            print(DF_DoiTenField, file=f)
            print("Tong Nhan vien : ", tong_NV_TC, file=f)
            print("Tong so Nam    : ", tong_nam_TC, file=f)
            print("Tong so Nu     : ", tong_nu_TC, file=f)
            print("Tong Luong     : ", tong_TC, file=f)
            f.close()

            text_file = open("tongket/TinhLuongTongKet_TC.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def tinhLuongTongKet_TK():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])
            DF_TinhLuong = DF_Fields.apply(lambda x: x * 250000 if x.name == 'HSLuong' else x)
            DF_DoiTenField = DF_TinhLuong.rename({'HSLuong': 'Luong'}, axis=1)
            DF_DoiTenField = DF_DoiTenField.loc[DF_DoiTenField['MaPB'] == 'TK']

            tong_NV_TK = len(DF_DoiTenField)
            TK_Nam = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 0]
            tong_nam_TK = len(TK_Nam)
            TK_Nu = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 1]
            tong_nu_TK = len(TK_Nu)
            tong_TK = sum(DF_DoiTenField['Luong'])

            f = open("tongket/TinhLuongTongKet_TK.txt", "w+")
            print(DF_DoiTenField, file=f)
            print("Tong Nhan vien : ", tong_NV_TK, file=f)
            print("Tong so Nam    : ", tong_nam_TK, file=f)
            print("Tong so Nu     : ", tong_nu_TK, file=f)
            print("Tong Luong     : ", tong_TK, file=f)
            f.close()

            text_file = open("tongket/TinhLuongTongKet_TK.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def tinhLuongTongKet_VP():
            my_text.delete("1.0", END)

            DF_Luong = DF_NhanVien.merge(DF_ChiTiet)
            DF_Fields = DF_Luong.filter(["MaNV", "Ho", "Ten", "Phai", "ChucVu", "HSLuong", "MaPB"])
            DF_TinhLuong = DF_Fields.apply(lambda x: x * 250000 if x.name == 'HSLuong' else x)
            DF_DoiTenField = DF_TinhLuong.rename({'HSLuong': 'Luong'}, axis=1)
            DF_DoiTenField = DF_DoiTenField.loc[DF_DoiTenField['MaPB'] == 'VP']

            tong_NV_VP = len(DF_DoiTenField)
            VP_Nam = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 0]
            tong_nam_VP = len(VP_Nam)
            VP_Nu = DF_DoiTenField.loc[DF_DoiTenField['Phai'] == 1]
            tong_nu_VP = len(VP_Nu)
            tong_VP = sum(DF_DoiTenField['Luong'])

            f = open("tongket/TinhLuongTongKet_VP.txt", "w+")
            print(DF_DoiTenField, file=f)
            print("Tong Nhan vien : ", tong_NV_VP, file=f)
            print("Tong so Nam    : ", tong_nam_VP, file=f)
            print("Tong so Nu     : ", tong_nu_VP, file=f)
            print("Tong Luong     : ", tong_VP, file=f)
            f.close()

            text_file = open("tongket/TinhLuongTongKet_VP.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        btn_ThongKeKH = tk.Button(lb_control, text="KH", command=tinhLuongTongKet_KH, width=8, height=1,
                                  background="green", foreground="white")
        btn_ThongKeKH.grid(row=0, column=1, pady=2, padx=2)

        btn_ThongKeKT = tk.Button(lb_control, text="KT", command=tinhLuongTongKet_KT, width=8, height=1,
                                  background="green", foreground="white")
        btn_ThongKeKT.grid(row=1, column=1, pady=2, padx=2)

        btn_ThongKeKT = tk.Button(lb_control, text="TC", command=tinhLuongTongKet_TC, width=8, height=1,
                                  background="green", foreground="white")
        btn_ThongKeKT.grid(row=2, column=1, pady=2, padx=2)

        btn_ThongKeKT = tk.Button(lb_control, text="TK", command=tinhLuongTongKet_TK, width=8, height=1,
                                  background="green", foreground="white")
        btn_ThongKeKT.grid(row=3, column=1, pady=2, padx=2)

        btn_ThongKeKT = tk.Button(lb_control, text="VP", command=tinhLuongTongKet_VP, width=8, height=1,
                                  background="green", foreground="white")
        btn_ThongKeKT.grid(row=4, column=1, pady=2, padx=2)

        my_text = tk.Text(label_data, height=32, width=70)
        my_text.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)


# <----------------------Giao diện chính---------------------->
class formTrangChu(Frame):
    def __init__(self, other):
        Frame.__init__(self, other)
        self.other = other
        self.taoForm()

    def moFile(self):
        moFile = formMoFile(self)
        moFile.grab_set()
    def nhanVien(self):
        nhanVien = formNhanVien(self)
        nhanVien.grab_set()
    def chucVu(self):
        chucVu = formChucVu(self)
        chucVu.grab_set()
    def phongBan(self):
        phongBan = formPhongBan(self)
        phongBan.grab_set()
    def chiTiet(self):
        chiTiet = formChiTiet(self)
        chiTiet.grab_set()
    def luong(self):
        luong = formLuong(self)
        luong.grab_set()
    def thongKe(self):
        thongKe = formThongKe(self)
        thongKe.grab_set()
    def tongKet(self):
        tongKet = formTongKet(self)
        tongKet.grab_set()

    def taoForm(self):
        self.other.title("Quản lý nhân viên")
        self.other.geometry("700x700")
        self.other.iconbitmap("image/icons8-us-dollar-48.ico")
        self.configure(bg='#ffff8d')
        self.pack(fill=BOTH, expand=1)

        lb_truong = tk.Label(self, text="TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT\n KHOA ĐÀO TẠO CHẤT LƯỢNG CAO", font=("",13), background="#ffff8d")
        lb_truong.pack(pady=10)

        self.img1 = ImageTk.PhotoImage(Image.open("image/fhq.png"))
        panel1 = tk.Label(self, image = self.img1, background="#ffff8d")
        panel1.place(x=200, y = 80)
        self.img2 = ImageTk.PhotoImage(Image.open("image/ute.png"))
        panel2 = tk.Label(self, image = self.img2, background="#ffff8d")
        panel2.place(x=350, y = 80)
        #Label title
        lb_title = tk.Label(self, text="Quản lý lương của một cơ quan", font=("",24), background="#ffff8d")
        lb_title.place(x=120, y = 250)

        #Label information
        lb_infor = tk.LabelFrame(self, background="#ffff8d",borderwidth=0)
        lb_infor.place(x=120, y = 300)
        tk.Label(lb_infor, text="Giảng viên hướng dẫn:", font=("", 13), background="#ffff8d").grid(row=0, column=0, sticky='W', ipady = 10)
        tk.Label(lb_infor, text="Sinh viên thực hiện:", font=("", 13), background="#ffff8d").grid(row=1, column=0, sticky='W', ipady=10)
        tk.Label(lb_infor, text="GVC, ThS. Trần Tiến Đức", font=("", 13), background="#ffff8d").grid(row=0, column=1, sticky='W', ipady = 10)
        tk.Label(lb_infor, text="Nguyễn Ngọc Gia Minh", font=("", 13), background="#ffff8d").grid(row=1, column=1, sticky='W', ipady=10)
        tk.Label(lb_infor, text="Tô Lê Tấn Đạt ", font=("", 13), background="#ffff8d").grid(row=2, column=1, sticky='W', ipady=10)
        tk.Label(lb_infor, text="19110090", font=("", 13), background="#ffff8d").grid(row=1, column=2, sticky='W',ipady=10)
        tk.Label(lb_infor, text="19110030", font=("", 13), background="#ffff8d").grid(row=2, column=2, sticky='W', ipady=10)

        #Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=15, text="Chức năng",font=("", 13))
        lb_control.place(x=90, y = 440)

        tk.Label(lb_control, text="Mở 4 file ", font=("", 13)).grid(row=0, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang nhân viên ",font=("", 13)).grid(row=1, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang chi tiết ",font=("", 13)).grid(row=2, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang chức vụ ",font=("", 13)).grid(row=3, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="        ").grid(row=3, column=3)
        tk.Label(lb_control, text="Mở trang phòng ban" ,font=("", 13)).grid(row=0, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang lương nhân viên ",font=("", 13)).grid(row=1, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang thống kê ",font=("", 13)).grid(row=2, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang tổng kết ",font=("", 13)).grid(row=3, column=4, sticky='W', ipady = 10)

        Button(lb_control,text=" Mở ", command=self.moFile).grid(row=0, column=1)
        Button(lb_control, text=" Mở ",  command=self.nhanVien).grid(row=1, column=1)
        Button(lb_control,text=" Mở ", command=self.chiTiet).grid(row=2, column=1)
        Button(lb_control,text=" Mở ", command=self.chucVu).grid(row=3, column=1)
        Button(lb_control,text=" Mở ", command=self.phongBan).grid(row=0, column=5)
        Button(lb_control, text=" Mở ",  command=self.luong).grid(row=1, column=5)
        Button(lb_control,text=" Mở ", command=self.thongKe).grid(row=2, column=5)
        Button(lb_control,text=" Mở ", command=self.tongKet).grid(row=3, column=5)

root = Tk()
root.resizable(False, False)
formTrangChu(root)
root.mainloop()
