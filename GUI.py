from tkinter import *
from tkinter import messagebox
from tkinter import font
from typing import Sized
from loadTrainedModel import *

window = Tk()
window.title("Tư vấn chuyên ngành")
window.geometry("550x400")


lblTitile = Label(window, text="TƯ VẤN CHUYÊN NGÀNH", foreground='Blue', font=('Arial',15))
lblTitile.grid(column=0, row=0, columnspan=7)

lbl15 = Label(window, text="")
lbl15.grid(column=1, row=1)

lbl1 = Label(window, text="Nhập môn lập trình")
lbl1.grid(column=1, row=2)
lbl2 = Label(window, text="Lập trình hướng đối tượng")
lbl2.grid(column=1, row=3)
lbl3 = Label(window, text="Cấu trúc dữ liệu và giải thuật")
lbl3.grid(column=1, row=4)
lbl4 = Label(window, text="Lập trình Web ")
lbl4.grid(column=1, row=5)
lbl5 = Label(window, text="Hệ điều hành")
lbl5.grid(column=1, row=6)
lbl6 = Label(window, text="Mạng máy tính")
lbl6.grid(column=1, row=7)
lbl7 = Label(window, text="Thực hành mạng máy tính")
lbl7.grid(column=1, row=8)

lbl8 = Label(window, text="Cơ sở dữ liệu")
lbl8.grid(column=4, row=2)
lbl9 = Label(window, text="Thực hành cơ sở dữ liệu")
lbl9.grid(column=4, row=3)
lbl10 = Label(window, text="Hệ quản trị CSDL")
lbl10.grid(column=4, row=4)
lbl11 = Label(window, text="Trí tuệ nhân tạo")
lbl11.grid(column=4, row=5)
lbl12 = Label(window, text="Toán rời rạc")
lbl12.grid(column=4, row=6)
lbl13 = Label(window, text="Công nghệ Java")
lbl13.grid(column=4, row=7)

lbl14 = Label(window, text="Kết quả tư vấn",font=('Arial', 12, 'bold'))
lbl14.grid(column=1, row=12)

txtNMLT = Entry(window, width=15)
txtNMLT.grid(column=2, row=2)
txtLTHDT = Entry(window, width=15)
txtLTHDT.grid(column=2, row=3)
txtCTDLGT = Entry(window, width=15)
txtCTDLGT.grid(column=2, row=4)
txtLTWeb = Entry(window, width=15)
txtLTWeb.grid(column=2, row=5)
txtHDH = Entry(window, width=15)
txtHDH.grid(column=2, row=6)
txtMMT = Entry(window, width=15)
txtMMT.grid(column=2, row=7)
txtTH_MMT = Entry(window, width=15)
txtTH_MMT.grid(column=2, row=8)
txtCSDL = Entry(window, width=15)

txtCSDL.grid(column=5, row=2)
txtTH_CSDL = Entry(window, width=15)
txtTH_CSDL.grid(column=5, row=3)
txtHQTCSDL = Entry(window, width=15)
txtHQTCSDL.grid(column=5, row=4)
txtTTNT = Entry(window, width=15)
txtTTNT.grid(column=5, row=5)
txtTRR = Entry(window, width=15)
txtTRR.grid(column=5, row=6)
txtCNJava = Entry(window, width=15)
txtCNJava.grid(column=5, row=7)

lbl14 = Label(window, text="")
lbl14.grid(column=1, row=11)

lblKetQua = Label(window, width=40, text="")
lblKetQua.grid(column=1, row=13, rowspan=3, columnspan=3)

def click_btnEnter():
    try:
        X = np.array([txtNMLT.get(), txtLTHDT.get(), txtCTDLGT.get(), txtLTWeb.get(), txtHDH.get(),
                    txtMMT.get(), txtTH_MMT.get(), txtCSDL.get(), txtTH_CSDL.get(),
                    txtHQTCSDL.get(), txtTTNT.get(), txtTRR.get(), txtCNJava.get()])
        
        y = np.asarray(X, dtype=np.float64, order='C')
        loadModel()
        result = predict(y)
        if(result[0] == 1):
            lblKetQua.configure(text="Chuyên ngành Công nghệ phần mềm")
        elif(result[0] == 2):
            lblKetQua.configure(text="Chuyên ngành Hệ thống thông tin")
        elif(result[0] == 3):
            lblKetQua.configure(text="Chuyên ngành Mạng máy tính và truyền thông")
        else:
            lblKetQua.configure(text="Chuyên ngành Khoa học phân tích dữ liệu")
    except ValueError:
        messagebox.showinfo("Waning","Mời bạn nhập đủ các cột điểm!", )

        
def click_btnClear():
    txtNMLT.delete(0,END)
    txtCNJava.delete(0,END)
    txtCSDL.delete(0,END)
    txtCTDLGT.delete(0,END)
    txtHDH.delete(0,END)
    txtHQTCSDL.delete(0,END)
    txtLTHDT.delete(0,END)
    txtLTWeb.delete(0,END)
    txtMMT.delete(0,END)
    txtTH_CSDL.delete(0,END)
    txtTH_MMT.delete(0,END)
    txtTRR.delete(0,END)
    txtTTNT.delete(0,END)
    lblKetQua.configure(text="")

btnEnter = Button(window, width=15, height=2, text="Tư vấn", background='green', fg='white', font=('Arial', 12), command=click_btnEnter)
btnEnter.grid(column=3, row=12, columnspan=3,rowspan=2)

lbl16 = Label(window, text="")
lbl16.grid(column=3, row=15)

btnClear = Button(window, width=15, height=2, text="Clear all", background='Red', fg='white', font=('Arial', 12), command=click_btnClear)
btnClear.grid(column=3, row=16, columnspan=3,rowspan=2)

window.mainloop()