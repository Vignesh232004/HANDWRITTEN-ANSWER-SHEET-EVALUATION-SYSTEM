import pytesseract
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from PIL import ImageTk,Image
from PIL import Image

root = Tk()
root.title('Answer key input')
root.geometry('1100x1100')
#v = Scrollbar(root, orient='vertical')
#v.config(command=root.yview)

def open12():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/Admin/Desktop/handwriting_recognition-master/handwritten images", title="Select A File",filetypes=(("PNG files","*.PNG"),("all files","*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_image = Image.open(root.filename)
    my_image1= my_image.resize((100,50), Image.Resampling.LANCZOS)
    my_image2= ImageTk.PhotoImage(my_image1)
    my_image_label = Label(root,image=my_image2).pack()
    
    img = Image.open(root.filename)
    
    pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    result = pytesseract.image_to_string(img)
    print(result)
    Label(root,text=result).pack()
# write text in a text file and save it to source path    
    with open('abc.txt',mode='a') as file:      
      
                 file.write(result) 
                 print(result) 
    



#print(img)
open('abc.txt', mode='w')   
                 
my_btn = Button(root,text="Open File", command=open12)
my_btn.pack()

root.mainloop()
