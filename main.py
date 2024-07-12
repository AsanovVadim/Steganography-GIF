import os  # Взаимодействия с ос
from tkinter import *  # Интерфейса
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog as fd
from PIL import Image, ImageTk  # Вставка иконок в кнопки
from encrypt import *
from decrypt import *


filepath = ''
filename = ''


def load():
    global filepath, filename

    filepath = fd.askopenfilename()
    filename = filepath.split('/')[-1]
    btnNameMus.config(text=filename)


def save():
    saving_file = open("./Result/newimage.gif", "rb").read()
    f = asksaveasfile(initialfile='Steg_'+filename,
                      defaultextension=".gif", filetypes=[("All Files", "*.*"), ("GIF-image", "*.gif")])
    with open(f.name, "wb") as file:
        file.write(saving_file)
        file.close()


def decode():
    txtfile = open(os.path.dirname(os.path.abspath(__file__)) + '\\Result\\keys.txt', 'r')
    output = stega_decrypt(txtfile)
    txt1.delete(1.0, END)
    txt1.insert(1.0, output)


def encode():
    text_file = txt.get(1.0, END)
    # os.remove('./Result/newimage.gif') # Удаление для перезаписи файла
    stega_encrypt(filepath, text_file)


# Объявление Tk
root = Tk()
root.title('Victory')
root.geometry('1024x500')
root.configure(background='#6AA2FF')
bg = PhotoImage(file='./bg.png')
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# ----------------------------------------------------
# Загрузка картинок
img = Image.open(os.path.dirname(os.path.abspath(__file__)) + '\hbutton_3.png')
image = img.resize((300, 50), Image.LANCZOS)
img1But = ImageTk.PhotoImage(image)

img = Image.open(os.path.dirname(os.path.abspath(__file__)) + '\hbutton_2.png')
image = img.resize((300, 50), Image.LANCZOS)
img2But = ImageTk.PhotoImage(image)

img = Image.open(os.path.dirname(os.path.abspath(__file__)) + '\hbutton_1.png')
image = img.resize((180, 35), Image.LANCZOS)
imgBtnShifr = ImageTk.PhotoImage(image)

img = Image.open(os.path.dirname(os.path.abspath(__file__)) + '\hbutton.png')
image = img.resize((180, 35), Image.LANCZOS)
imgBtnRasshifr = ImageTk.PhotoImage(image)


# ----------------------------------------------------
# Кнопки загрузки и сохранения композиций
btn = Button(root, width=300, height=40,
             image=img1But, bd=0, highlightthickness=0,
             background='#161616', activeforeground='#161616',
             activebackground='#161616', command=load).place(x=20, y=20,)


btn1 = Button(root, width=300, height=40,
              image=img2But, bd=0, highlightthickness=0,
              background='#161616', activeforeground='#161616',
              activebackground='#161616', command=save).place(x=700, y=20,)


# ----------------------------------------------------
# Кнопки расшифровки и зашифровки
btnShifr = Button(root, width=180, height=35, image=imgBtnShifr, bd=0, highlightthickness=0,
                  background='#161616', activeforeground='#161616',
                  activebackground='#161616', command=encode).place(x=420, y=160,)

btnRasshifr = Button(root, width=180, height=35, image=imgBtnRasshifr, bd=0, highlightthickness=0,
                     background='#161616', activeforeground='#161616',
                     activebackground='#161616', command=decode).place(x=420, y=240,)


# ----------------------------------------------------
# Вывод файла
btnNameMus = Button(root, width=45, height=2, text=' ', state=["disabled"])
btnNameMus.place(x=350, y=20,)

btnNameMus1 = Button(root, width=45, height=2, text='newimage.gif', state=["disabled"])
btnNameMus1.place(x=350, y=350,)


# ----------------------------------------------------
# Текстовые поля
txt = Text(root, width=40, height=10, wrap=WORD)
txt.place(x=20, y=140, )
txt.insert(1.0, 'Enter your message')

txt1 = Text(root, width=40, height=10, wrap=WORD)
txt1.place(x=680, y=140, )
txt1.insert(1.0, 'Здесь будет текст расшифрованного сообщения')


root.mainloop()