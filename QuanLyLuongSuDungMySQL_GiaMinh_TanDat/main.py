import sys
import pandas as pd
import tkinter as tk
from tkinter import Frame, Tk, BOTH, END, ttk
from time import strftime
from tkinter import *
import  tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkcalendar import DateEntry
from datetime import date
from PIL import ImageTk, Image

#Thay đổi 4 thông số sau tùy vào từng máy
user = 'root' #Tên tài khoản MySQL WorkBench của máy
password ='Giaminh2001@' #Mật khẩu MySQL WorkBench của máy
database = 'pythontkinter' #Tên cơ sở dữ liệu của máy
host="localhost"#Tên host sử dụng

class formMoFile(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Mở file")
        self.geometry("650x550")
        self.iconbitmap("HinhAnh/icons8-align-text-left-48.ico")
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
class formNhanVien(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Nhân viên")
        self.geometry("920x420")
        self.iconbitmap("HinhAnh/icons8-employee-48_1.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def maPB():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select MaPB from phongban")
            MaPBs = cursor.fetchall()
            cursor.close()
            connection.close()
            return MaPBs
        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from nhanvien")
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                i = i + 1
            connection.close()
            tree.pack()
        def xoa():
            MaNV = tb_xoa.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("delete from nhanvien where MaNV = "+MaNV+"")
            cursor.execute("commit")
            tb_xoa.delete(0, END)
            MessageBox.showerror("Thông báo", "Xoá thành công")
            connection.close()
            xem()
        def chen():
            MaNV = tb_MaNV.get()
            Ho = tb_Ho.get()
            Ten = tb_Ten.get()
            Phai = tb_Phai.get()
            NTNS = tb_NTNS.get()
            NgayBatDau = tb_NgayBatDau.get()
            MaPB = tb_MaPB.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("insert into nhanvien(MaNV,Ho,Ten,Phai,NTNS,NgayBatDau,MaPB) values('" + MaNV + "','" + Ho + "','" + Ten + "','" + Phai + "',STR_TO_DATE('" + NTNS + "', '%d/%m/%Y'),STR_TO_DATE('" + NgayBatDau + "', '%d/%m/%Y'),'" + MaPB + "')")
            cursor.execute("commit")

            tb_Ho.delete(0, END)
            tb_Ten.delete(0, END)
            tb_Phai.delete(0, END)
            tb_NTNS.delete(0, END)
            tb_NgayBatDau.delete(0, END)
            tb_MaPB.delete(0, END)

            MessageBox.showinfo("Thông báo", "Thêm thành công")
            connection.close()
            xem()

        lb_data = tk.LabelFrame(self, padx=20, pady=15, text="Bảng nhân viên")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=16)
        tree['show'] = 'headings'
        tree["columns"] = ['MaNV', 'Ho', 'Ten', 'Phai', 'NTNS', 'NgayBatDau', 'MaPB']
        tree.column("MaNV", width=50, anchor=tk.W)
        tree.column("Ho", width=100, anchor=tk.W)
        tree.column("Ten", width=50, anchor=tk.W)
        tree.column("Phai", width=50, anchor=tk.W)
        tree.column("NTNS", width=100, anchor=tk.W)
        tree.column("NgayBatDau", width=100, anchor=tk.W)
        tree.column("MaPB", width=50, anchor=tk.W)

        tree.heading("MaNV", text="MaNV", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        tree.heading("NTNS", text="NTNS", anchor=tk.W)
        tree.heading("NgayBatDau", text="NgayBatDau", anchor=tk.W)
        tree.heading("MaPB", text="MaPB", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=570, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=570, y=50)
        tk.Label(lb_info, text="Mã nhân viên").grid(row=0, column=0, sticky='W')
        tb_MaNV = tk.Entry(lb_info)
        tb_MaNV.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Họ & tên đệm").grid(row=1, column=0, sticky='W')
        tb_Ho = tk.Entry(lb_info)
        tb_Ho.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Tên").grid(row=2, column=0, sticky='W')
        tb_Ten = tk.Entry(lb_info)
        tb_Ten.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Phái").grid(row=3, column=0, sticky='W')
        tb_Phai = tk.Spinbox(lb_info, from_ = 0, to_=1, width=5)
        tb_Phai.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Ngày sinh").grid(row=4, column=0, sticky='W')
        tb_NTNS = DateEntry(lb_info, locale='en_US', date_pattern='d/m/Y')
        tb_NTNS.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        dt=date.today()
        tb_NTNS.set_date(dt)

        tk.Label(lb_info, text="Ngày bắt đầu").grid(row=5, column=0, sticky='W')
        tb_NgayBatDau=DateEntry(lb_info, locale='en_US', date_pattern='d/m/Y')
        tb_NgayBatDau.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)
        dt=date.today()
        tb_NTNS.set_date(dt)

        tk.Label(lb_info, text="Mã phòng ban").grid(row=6, column=0, sticky='W')
        tb_MaPB = ttk.Combobox(lb_info,values=maPB(), width=5)
        tb_MaPB.grid(row=6, column=1, sticky=tk.W, padx=6, pady=5)

        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=570, y=315)

        tk.Label(lb_control, text="Xóa nhân viên có mã").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Thêm nhân viên:").grid(row=1, column=0, sticky='W')

        btn_chen = tk.Button(lb_control, text="Thêm", width=8, height=1, command=chen)
        btn_chen.grid(row=1, column=2, padx=7)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)
class formPhongBan(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Phòng ban")
        self.geometry("660x250")
        self.iconbitmap("HinhAnh/icons8-employee-48_1.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)
        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from phongban")
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1]))
                i=i+1
            connection.close()
            tree.pack()
        def xoa():

            MaPB = tb_xoa.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("delete from phongban where MaPB = '"+MaPB+"'")
            cursor.execute("commit")
            MessageBox.showerror("Thông báo", "Xoá thành công")
            connection.close()
            xem()


        def chen():
            MaPB = tb_MaPB.get()
            TenPB = tb_TenPB.get()

            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("insert into phongban(MaPB,TenPB) values('"+ MaPB +"','"+ TenPB +"')")
            cursor.execute("commit")

            tb_MaPB.delete(0, END)
            tb_TenPB.delete(0, END)

            MessageBox.showinfo("Thông báo", "Thêm thành công")
            connection.close()
            xem()


        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng phòng ban")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data,height=8)
        tree['show'] = 'headings'
        tree["columns"] = ['MaPB', 'TenPB']
        tree.column("MaPB", width=50, anchor=tk.W)
        tree.column("TenPB", width=200, anchor=tk.W)

        tree.heading("MaPB", text="MaPB", anchor=tk.W)
        tree.heading("TenPB", text="TenPB", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=300, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=300, y=50)

        tk.Label(lb_info, text="Mã phòng ban").grid(row=0, column=0, sticky='W')
        tb_MaPB = tk.Entry(lb_info)
        tb_MaPB.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Tên phòng ban").grid(row=1, column=0, sticky='W')
        tb_TenPB = tk.Entry(lb_info)
        tb_TenPB.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=300, y=170)

        tk.Label(lb_control, text="Xóa phòng ban có mã").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Thêm phòng ban:").grid(row=1, column=0, sticky='W')


        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)

        btn_chen = tk.Button(lb_control, text="Thêm", width=8, height=1, command=chen)
        btn_chen.grid(row=1, column=2, padx=7)
class formLuong(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Lương nhân viên")
        self.geometry("900x490")
        self.iconbitmap("HinhAnh/icons8-cash-in-hand-48.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def maPB():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select MaPB from phongban")
            MaPBs = cursor.fetchall()
            cursor.close()
            connection.close()
            return MaPBs

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV")
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                i = i + 1
            connection.close()
            tree.pack()
        def tinhLuong():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query="select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV order by nv.MaPB"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor, columns=['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB'])
            f = open("Luong/TinhLuong.txt", "w+")
            print(DF_Luong, file=f)
            f.close()

            cursor.execute(query)
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                i=i+1
            connection.close()
            tree.pack()


        def luongCaoNhat():
            tree.delete(*tree.get_children())
            top = sb_top.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query="select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV order by Luong desc limit "+top+""
            cursor.execute(query)

            DF_Luong = pd.DataFrame.from_records(cursor, columns=['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB'])
            f = open("Luong/LuongCaoNhat.txt", "w+")
            print(DF_Luong, file=f)
            f.close()

            cursor.execute(query)
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                i=i+1
            connection.close()
            tree.pack()

        def luongCaoNhatTungPhongBan():
            tree.delete(*tree.get_children())
            MaPB = cb_MaPB.get()
            connection = mysql.connect(host = host, user=user, password=password,database=database)
            cursor = connection.cursor()
            query = "select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+MaPB+"' and ct.HSLuong = (select max(ct.HSLuong) from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+MaPB+"')"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor,columns=['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB'])
            f = open("Luong/LuongCaoNhatTheoPhongBan"+MaPB+".txt", "w+")
            print(DF_Luong, file=f)
            f.close()
            cursor.execute(query)
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                i = i + 1
            connection.close()
            tree.pack()

        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng phòng ban")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=20)
        tree['show'] = 'headings'
        tree["columns"] = ['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB']
        tree.column("MaNV", width=50, anchor=tk.W)
        tree.column("Ho", width=100, anchor=tk.W)
        tree.column("Ten", width=50, anchor=tk.W)
        tree.column("Phai", width=50, anchor=tk.W)
        tree.column("ChucVu", width=50, anchor=tk.W)
        tree.column("Luong", width=100, anchor=tk.W)
        tree.column("MaPB", width=50, anchor=tk.W)

        tree.heading("MaNV", text="MaNV", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        tree.heading("ChucVu", text="ChucVu", anchor=tk.W)
        tree.heading("Luong", text="Luong", anchor=tk.W)
        tree.heading("MaPB", text="MaPB", anchor=tk.W)
        xem()
        tree.pack()

        #Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=500, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=15, text="Chức năng")
        lb_control.place(x=500, y=60)

        tk.Label(lb_control, text="Tính lương nhân viên").grid(row=0, column=0, sticky='W')
        tk.Label(lb_control, text="Top nhân viên có lương cao").grid(row=1, column=0, sticky='W')
        sb_top = Spinbox(lb_control, from_ = 1, to_ = sys.maxsize,width=5)
        sb_top.grid(row=1, column=1, sticky=tk.W, padx=6, pady=5)

        tk.Label(lb_control, text="Nhân viên có lương cao nhất của phòng").grid(row=2, column=0, sticky='W')
        cb_MaPB = ttk.Combobox(lb_control, values=maPB(), width=5)
        cb_MaPB.grid(row=2, column=1, sticky=tk.W, padx=6, pady=5)

        btn_Luong = tk.Button(lb_control, text="Tính", command=tinhLuong, width=8, height=1, background="green",foreground="white")
        btn_Luong.grid(row=0, column=1, pady=2, padx=2)

        btn_LuongCaoNhat = tk.Button(lb_control, text="Xem", command=luongCaoNhat, width=8, height=1, background="green",foreground="white")
        btn_LuongCaoNhat.grid(row=1, column=2, pady=2, padx=2)

        btn_LuongCaoNhatPhongBan = tk.Button(lb_control, text="Xem", command=luongCaoNhatTungPhongBan, width=8, height=1,background="green", foreground="white")
        btn_LuongCaoNhatPhongBan.grid(row=2, column=2, pady=2, padx=2)
class formThongKe(tk.Toplevel):
    def __init__(self,parent):
        tk.Toplevel.__init__(self,parent)
        self.title("Thống kê")
        self.geometry("610x300")
        self.iconbitmap("HinhAnh/icons8-total-sales-48.ico")
        self.configure(bg='#ffff8d')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def ThongKe():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query = "select pb.TenPB, nam.SoNam, nu.SoNu, (nam.SoNam+nu.SoNu) as TongSo from phongban pb, (select MaPB, count(*) as SoNam from nhanvien where Phai = '0' group by MaPB ) nam, (select MaPB, count(*) as SoNu from nhanvien where Phai = '1' group by MaPB) nu where pb.MaPB = nam.MaPB and pb.MaPB=nu.MaPB group by pb.MaPB;"
            cursor.execute(query)
            DF_ThongKe = pd.DataFrame.from_records(cursor,columns=['TenPB', 'SoNam', 'SoNu', 'TongSo'])
            f = open("ThongKe/ThongKe.txt", "w+")
            print(DF_ThongKe, file=f)
            f.close()

            cursor.execute(query)
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3]))
                i = i + 1
            connection.close()
            tree.pack()

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=350, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=60, pady=15, text="Chức năng")
        lb_control.place(x=350, y=60)
        tk.Label(lb_control, text="Thống kê").grid(row=0, column=0, sticky='W')

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng Thống Kê")
        label_data.place(x=10, y=10)

        tree = ttk.Treeview(label_data, height=10)
        tree['show'] = 'headings'
        tree["columns"] = ['TenPB', 'SoNam', 'SoNu', 'TongSo']
        tree.column("TenPB", width=150, anchor=tk.W)
        tree.column("SoNam", width=50, anchor=tk.W)
        tree.column("SoNu", width=50, anchor=tk.W)
        tree.column("TongSo", width=50, anchor=tk.W)

        tree.heading("TenPB", text="TenPB", anchor=tk.W)
        tree.heading("SoNam", text="SoNam", anchor=tk.W)
        tree.heading("SoNu", text="SoNu", anchor=tk.W)
        tree.heading("TongSo", text="TongSo", anchor=tk.W)
        # xem()
        tree.pack()

        btn_ThongKe = tk.Button(lb_control, text="Thống kê", command=ThongKe, width=8, height=1, background="green",
                               foreground="white")
        btn_ThongKe.grid(row=0, column=1, pady=2, padx=2)
class formChiTiet(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("ChiTiet")
        self.geometry("700x420")
        self.iconbitmap("HinhAnh/icons8-brief-48.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)
    
        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from chitiet")
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3]))
                i = i + 1
            connection.close()
            tree.pack()
        
        def xoa():
            MaNV = tb_xoa.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("delete from chitiet where MaNV = "+MaNV+"")
            cursor.execute("commit")
            tb_xoa.delete(0, END)
            MessageBox.showerror("Thông báo", "Xoá thành công")
            connection.close()
            xem()
        def chen():
            MaNV = tb_MaNV.get()
            ChucVu=tb_CV.get()
            HSLuong=tb_HSLuong.get()
            MucDoCV=tb_MucDoCV.get()
            #Vitri = tb_chenTruoc()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("insert into chitiet(MaNV,ChucVu,HSLuong,MucDoCV) values('" + MaNV + "','" + ChucVu + "','" + HSLuong + "','" + MucDoCV + "')")
            cursor.execute("commit")

            tb_MaNV.delete(0, END)
            tb_CV.delete(0, END)
            tb_HSLuong.delete(0, END)
            tb_MucDoCV.delete(0, END)
            MessageBox.showinfo("Thông báo", "Thêm thành công")
            connection.close()
            xem()
        def chuVu():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select ChucVu from hschucvu")
            ChucVu = cursor.fetchall()
            cursor.close()
            connection.close()
            return ChucVu

        lb_data = tk.LabelFrame(self, padx=30, pady=15, text="Bảng chi tiết")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=16)
        tree['show'] = 'headings'
        tree["columns"] = ['MaNV', 'ChucVu', 'HSLuong', 'MucDoCV']
        tree.column("MaNV", width=80, anchor=tk.W)
        tree.column("ChucVu", width=80, anchor=tk.W)
        tree.column("HSLuong", width=80, anchor=tk.W)
        tree.column("MucDoCV", width=80, anchor=tk.W)
        

        tree.heading("MaNV", text="MaNV", anchor=tk.W)
        tree.heading("ChucVu", text="ChucVu", anchor=tk.W)
        tree.heading("HSLuong", text="HSLuong", anchor=tk.W)
        tree.heading("MucDoCV", text="MucDoCV", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=400, y=10)
        clock()

            # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=400, y=50)
        tk.Label(lb_info, text="Mã nhân viên").grid(row=0, column=0, sticky='W')
        tb_MaNV = tk.Entry(lb_info)
        tb_MaNV.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Chức Vụ").grid(row=1, column=0, sticky='W')
        tb_CV = ttk.Combobox(lb_info, value= chuVu(),width=17)
        tb_CV.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Hệ số lương").grid(row=2, column=0, sticky='W')
        tb_HSLuong = tk.Entry(lb_info)
        tb_HSLuong.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Mức độ công việc").grid(row=3, column=0, sticky='W')
        tb_MucDoCV = tk.Entry(lb_info)
        tb_MucDoCV.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

            # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=400, y=215)

        tk.Label(lb_control, text="Xóa chi tiết có mã").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Thêm nhân viên:").grid(row=1, column=0, sticky='W')

        btn_chen = tk.Button(lb_control, text="Thêm", width=8, height=1, command=chen)
        btn_chen.grid(row=1, column=2, padx=7)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)
class formHSChucVu(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("HeSoChucVu")
        self.geometry("580x250")
        self.iconbitmap("HinhAnh/icons8-brief-48.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)
        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def chucVu():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from hschucvu")
            ChucVus = cursor.fetchall()
            cursor.close()
            connection.close()
            return ChucVus

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from hschucvu")
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1]))
                i=i+1
            connection.close()
            tree.pack()

        def xoa():

            ChucVu = tb_xoa.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("delete from hschucvu where ChucVu = '"+ChucVu+"'")
            cursor.execute("commit")


            MessageBox.showerror("Thông báo", "Xoá thành công")

            cursor.execute("select * from hschucvu")
            connection.close()
            xem()
            return chucVu()

        def chen():
            ChucVu = tb_ChucVu.get()
            HSCV = tb_HSCV.get()

            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("insert into hschucvu(ChucVu,HSCV) values('"+ ChucVu +"','"+ HSCV +"')")
            cursor.execute("commit")

            tb_ChucVu.delete(0, END)
            tb_HSCV.delete(0, END)

            MessageBox.showinfo("Thông báo", "Thêm thành công")
            connection.close()
            xem()

        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng hệ số chức vụ")
        lb_data.place(x=10, y=10)    

        tree = ttk.Treeview(lb_data,height=8)
        tree['show'] = 'headings'
        tree["columns"] = ['ChucVu', 'HSCV']
        tree.column("ChucVu", width=150, anchor=tk.W)
        tree.column("HSCV", width=100, anchor=tk.W)

        tree.heading("ChucVu", text="ChucVu", anchor=tk.W)
        tree.heading("HSCV", text="HSCV", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=300, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=300, y=50)

        tk.Label(lb_info, text="Chức Vụ").grid(row=0, column=0, sticky='W')
        tb_ChucVu = tk.Entry(lb_info)
        tb_ChucVu.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Hệ số chức vụ").grid(row=1, column=0, sticky='W')
        tb_HSCV = tk.Entry(lb_info)
        tb_HSCV.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=300, y=170)

        tk.Label(lb_control, text="Xóa chức vụ ").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)

        btn_chen = tk.Button(lb_control, text="Thêm", width=8, height=1, command=chen)
        btn_chen.grid(row=1, column=2, padx=7)
class formLuongTheoPhong(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Lương nhân viên")
        self.geometry("970x490")
        self.iconbitmap("HinhAnh/icons8-cash-in-hand-48.ico")
        self.configure(bg='#ffff8d')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def maPB():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select MaPB from phongban")
            MaPBs = cursor.fetchall()
            cursor.close()
            connection.close()
            return MaPBs
        def tinhLuong():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query="select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV order by nv.MaPB"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor, columns=['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB'])
            f = open("Luong/TinhLuong.txt", "w+")
            print(DF_Luong, file=f)
            f.close()

            cursor.execute(query)
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                i=i+1
            connection.close()
            tree.pack()
        def ThongKe(MaPB):
            tree_thongke.delete(*tree_thongke.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor_thongke = connection.cursor()
            query = "select tong.MaPB, tong.TenPB, tong.SoNam, tong.SoNu, (tong.SoNam+tong.SoNu) as TongSo , sum(ct.HSLuong*250000) as TongLuong from nhanvien nv, chitiet ct,(select pb.MaPB, pb.TenPB, nam.SoNam, nu.SoNu, (nam.SoNam+nu.SoNu) as TongSo from phongban pb, (select MaPB, count(*) as SoNam from nhanvien where Phai = '0' group by MaPB ) nam, (select MaPB, count(*) as SoNu from nhanvien where Phai = '1' group by MaPB) nu where pb.MaPB = nam.MaPB and pb.MaPB=nu.MaPB and pb.MaPB ='"+MaPB+"' group by pb.MaPB) as tong where nv.MaNV = ct.MaNV and tong.MaPB=nv.MaPB order by nv.MaPB;"
            cursor_thongke.execute(query)
            DF_ThongKe = pd.DataFrame.from_records(cursor_thongke,columns=['MaPB','TenPB', 'SoNam', 'SoNu', 'TongSo','TongLuong'])
            f = open("Luong/TongKetLuongTheoPhongBan"+MaPB+".txt", "w+")
            print(DF_ThongKe, file=f)
            f.close()
            cursor_thongke.execute(query)
            i = 0
            for row in cursor_thongke:
                tree_thongke.insert('', i, values=(row[0], row[1], row[2], row[3],row[4], row[5]))
                i = i + 1
            connection.close()
            tree_thongke.pack()
        
        def luongTheoPhongBan():
            tree.delete(*tree.get_children())
            MaPB = cb_MaPB.get()
            connection = mysql.connect(host = host, user=user, password=password,database=database)
            cursor = connection.cursor()
            query = "select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+MaPB+"'"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor,columns=['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB'])
            
            f = open("Luong/LuongTheoPhongBan"+MaPB+".txt", "w+")
            print(DF_Luong, file=f)
            f.close()
            cursor.execute(query)
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                i = i + 1
            connection.close()
            tree.pack()
            ThongKe(MaPB)
            

        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng phòng ban")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=20)
        tree['show'] = 'headings'
        tree["columns"] = ['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB']
        tree.column("MaNV", width=50, anchor=tk.W)
        tree.column("Ho", width=100, anchor=tk.W)
        tree.column("Ten", width=50, anchor=tk.W)
        tree.column("Phai", width=50, anchor=tk.W)
        tree.column("ChucVu", width=50, anchor=tk.W)
        tree.column("Luong", width=75, anchor=tk.W)
        tree.column("MaPB", width=50, anchor=tk.W)

        tree.heading("MaNV", text="MaNV", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        tree.heading("ChucVu", text="ChucVu", anchor=tk.W)
        tree.heading("Luong", text="Luong", anchor=tk.W)
        tree.heading("MaPB", text="MaPB", anchor=tk.W)
        tinhLuong()
        tree.pack()

        lb_data_thongke = tk.LabelFrame(self, padx=20, pady=5, text="Bảng thống kê")
        lb_data_thongke.place(x=480, y=175)

        tree_thongke=ttk.Treeview(lb_data_thongke, height=10)
        tree_thongke['show'] = 'headings'
        tree_thongke["columns"] = ['MaPB', 'TenPB', 'SoNam', 'SoNu', 'TongSo', 'TongLuong']
        tree_thongke.column("MaPB", width=40, anchor=tk.W)
        tree_thongke.column("TenPB", width=150, anchor=tk.W)
        tree_thongke.column("SoNam", width=50, anchor=tk.W)
        tree_thongke.column("SoNu", width=45, anchor=tk.W)
        tree_thongke.column("TongSo", width=50, anchor=tk.W)
        tree_thongke.column("TongLuong", width=70, anchor=tk.W)

        tree_thongke.heading("MaPB", text="MaPB", anchor=tk.W)
        tree_thongke.heading("TenPB", text="TenPB", anchor=tk.W)
        tree_thongke.heading("SoNam", text="SoNam", anchor=tk.W)
        tree_thongke.heading("SoNu", text="SoNu", anchor=tk.W)
        tree_thongke.heading("TongSo", text="TongSo", anchor=tk.W)
        tree_thongke.heading("TongLuong", text="TongLuong", anchor=tk.W)
        # tree_thongke.pack()


        #Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#ffff8d", foreground='black')
        lb_clock.place(x=480, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=5, text="Chức năng")
        lb_control.place(x=480, y=60)

        tk.Label(lb_control, text="Lương nhân viên theo phòng").grid(row=2, column=0, sticky='W')
        cb_MaPB = ttk.Combobox(lb_control, values=maPB(), width=5)
        cb_MaPB.grid(row=2, column=1, sticky=tk.W, padx=6, pady=5)

        btn_LuongCaoNhatPhongBan = tk.Button(lb_control, text="Xem", command=luongTheoPhongBan, width=8, height=1,background="green", foreground="white")
        btn_LuongCaoNhatPhongBan.grid(row=0, column=1, pady=2, padx=2)

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
    def HSChucVu(self):
        chucvu = formHSChucVu(self)
        chucvu.grab_set()
    def luongTheoPhong(self):
        luongtheophong =formLuongTheoPhong(self)
        luongtheophong.grab_set()

    def taoForm(self):
        self.other.title("Quản lý nhân viên")
        self.other.geometry("700x720")
        self.other.iconbitmap("HinhAnh/icons8-us-dollar-48.ico")
        self.configure(bg='#ffff8d')
        self.pack(fill=BOTH, expand=1)

        lb_truong = tk.Label(self, text="TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT\n KHOA ĐÀO TẠO CHẤT LƯỢNG CAO", font=("",13), background="#ffff8d")
        lb_truong.pack(pady=10)

        self.img1 = ImageTk.PhotoImage(Image.open("HinhAnh/fhq.png"))
        panel1 = tk.Label(self, image = self.img1, background="#ffff8d")
        panel1.place(x=200, y = 80)
        self.img2 = ImageTk.PhotoImage(Image.open("HinhAnh/ute.png"))
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
        lb_control = tk.LabelFrame(self, padx=10, pady=30, text="Chức năng",font=("", 13))
        lb_control.place(x=120, y = 440)

        tk.Label(lb_control, text="Mở 4 file ", font=("", 13)).grid(row=0, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang nhân viên ",font=("", 13)).grid(row=1, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang chi tiết ",font=("", 13)).grid(row=2, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang chức vụ ",font=("", 13)).grid(row=3, column=0, sticky='W', ipady = 10)
        # tk.Label(lb_control, text="        ").grid(row=3, column=3)
        tk.Label(lb_control, text="Mở trang phòng ban" ,font=("", 13)).grid(row=0, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang lương nhân viên ",font=("", 13)).grid(row=1, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang thống kê ",font=("", 13)).grid(row=2, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở Lương theo phòng ban ",font=("", 13)).grid(row=3, column=4, sticky='W', ipady = 10)
        # tk.Label(lb_control, text="Mở trang tổng kết ",font=("", 13)).grid(row=3, column=4, sticky='W', ipady = 10)

        Button(lb_control,text=" Mở ", command=self.moFile).grid(row=0, column=1)
        Button(lb_control, text=" Mở ",  command=self.nhanVien).grid(row=1, column=1)
        Button(lb_control,text=" Mở ", command=self.chiTiet).grid(row=2, column=1)
        Button(lb_control,text=" Mở ", command=self.HSChucVu).grid(row=3, column=1)
        Button(lb_control,text=" Mở ", command=self.phongBan).grid(row=0, column=5)
        Button(lb_control, text=" Mở ",  command=self.luong).grid(row=1, column=5)
        Button(lb_control,text=" Mở ", command=self.thongKe).grid(row=2, column=5)
        Button(lb_control,text=" Mở ", command=self.luongTheoPhong).grid(row=3, column=5)

root = Tk()
root.resizable(False, False)
formTrangChu(root)
root.mainloop()