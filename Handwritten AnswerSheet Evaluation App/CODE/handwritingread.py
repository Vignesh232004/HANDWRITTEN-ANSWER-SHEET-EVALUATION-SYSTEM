import tkinter
import tkinter.messagebox
from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfilename 
from PIL import ImageTk,Image

from google.cloud import vision
import io
import os

root = Tk() 
root.title("Answer sheet input")
root.geometry('1000x1000')
root.resizable(width = True, height = True)
path=r"C:\Users\Admin\Desktop\handwriting_recognition-master\handwritten images\images1.jpg"


def open1():
    global my_image
    root.filename = askopenfilename(initialdir="C:/Users/Admin/Desktop/handwriting_recognition-master/handwritten images", title="Select A File",filetypes=(("PNG files","*.PNG"),("all files","*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    #my_image_label = Label(image=my_image).pack()
    
   
    #credential_path =r"C:\Users\Admin\.spyder-py3\VisionAPIDEMO\handwritten-project-82cff1ea3561.json"
    credential_path =r"C:\Users\vignesh\Downloads\helical-study-414314-e8ddfdd543bf.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    client = vision.ImageAnnotatorClient()

    with io.open(root.filename, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    text=[]
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
           # print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
               # print('Paragraph confidence: {}'.format(
                  #  paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    #print('Word text: {} (confidence: {})'.format(
                      #  word_text, word.confidence))
                    #print(word_text,end=" ")
                    #Label(root,text=word_text).pack()
                    text.append(word_text)
                    #for symbol in word.symbols:
                       # print('\tSymbol: {} (confidence: {})'.format(
                           # symbol.text, symbol.confidence))
    listToStr = ' '.join([str(elem) for elem in text])
    Label(root, text = listToStr).pack()
    with open('abc1.txt',mode='a') as file:      
            file.write(listToStr) 
            print(listToStr) 
    

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
        
    
                
"""Detects document features in an image."""

 

open('abc1.txt', mode ='w')                 
my_btn = Button(root,text="Open File", command=open1)
my_btn.pack()       
root.mainloop()  