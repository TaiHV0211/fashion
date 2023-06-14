from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from app.fashion_predict import predict
import tkinter
import cv2
import PIL.Image, PIL.ImageTk


window = Tk()
window.title("Hệ thống phân loại trang phục công sở")
window.resizable(0,0)
window.geometry("600x600")
frm = ttk.Frame(window, padding=10)
# frm.grid()


canvas = Canvas(window, width=500, height=500)
label = ttk.Label(window, text="", font=("Arial", 44))


photo = None
#open file
def select_file():
  global photo, canvas, label
  filetypes = (
    ('image', '*.jpg'),
    ('image', '*.png'),
    ('All files', '*.*')
  )

  filename = fd.askopenfilename(
    title='Open a file',
    initialdir='/',
    filetypes=filetypes)

  # print(filename)
  #Read input image
  photo = cv2.imread(filename)
  # scale_percent =  50 # percent of original size
  # # width = int(photo.shape[1] * scale_percent / 100)
  # # height = int(photo.shape[0] * scale_percent / 100)
  dim = (500, 500)
  # prediction
  result = predict(photo)
  label.configure(text=result)
  # resize image
  photo = cv2.resize(photo, dim, fx=0.5, fy=0.5)
  photo = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
  photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(photo))
  canvas.create_image(0, 0, anchor=NW, image=photo)


  # showinfo(
  #   title='Selected File',
  #   message=filename
  # )
# open button
open_button = ttk.Button(
    window,
    text='Open a File',
    command=select_file
)

open_button.pack()
canvas.pack()
label.pack()
# photo = cv2.imread(filename)

window.mainloop()