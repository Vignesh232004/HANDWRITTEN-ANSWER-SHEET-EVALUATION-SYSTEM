# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:18:47 2021

@author: Admin
"""

import numpy as np
#import cosine_similarity
import tkinter
import tkinter.messagebox
from  tkinter import *
#from tkinter.ttk import *
from decimal import Decimal
import nltk
nltk.download('stopwords')

nltk.download('punkt')
nltk.download('wordnet')


myfile = open("abc.txt")
txt = myfile.read()

myfile1 = open("abc1.txt")
txt1 = myfile1.read()

#print(txt)
#print(txt1)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words('english'))
word_tokens = word_tokenize(txt)
filtered_Sentence =[]

for w in word_tokens:
    if w not in stopwords:
        filtered_Sentence.append(w)
        
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer_Sentance = [lemmatizer.lemmatize(word) for word in filtered_Sentence]

print(word_tokens)
print(filtered_Sentence)
print(lemmatizer_Sentance)

word_tokens1 = word_tokenize(txt1)
filtered_Sentence1 =[]

for w in word_tokens1:
    if w not in stopwords:
        filtered_Sentence1.append(w)

lemmatizer_Sentence1 = [lemmatizer.lemmatize(word) for word in filtered_Sentence1]

print(word_tokens1)
count = len(word_tokens1)
print(filtered_Sentence1)
print(lemmatizer_Sentence1)


import language_check
from nltk.stem import WordNetLemmatizer

# Mention the language keyword
tool = language_check.LanguageTool('en-US')
i = 0

# Path of file which needs to be checked
with open(r'abc1.txt', 'r') as fin:
			
	for line in fin:
		matches = tool.check(line)
		i = i + len(matches)	
		pass

# prints total mistakes which are found
# from the document
print("No. of mistakes found in document is ", i)
print()
	
# prints mistake one by one
for mistake in matches:
	print(mistake)
	print()

listToStr = ' '.join([str(elem) for elem in filtered_Sentence])
listToStr1 = ' '.join([str(elem) for elem in filtered_Sentence1])

keyword = len(filtered_Sentence) - len(filtered_Sentence1)
matched_word = len(filtered_Sentence1) - keyword
documents = [listToStr, listToStr1]

print(documents)

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(documents)

doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix, columns = count_vectorizer.get_feature_names(),index =['key','answer'])

print(df)

from sklearn.metrics.pairwise import cosine_similarity

print (cosine_similarity(df))

l = cosine_similarity(df)

print(l[0][1])


def grammer():
    att = Toplevel()
    att.title("Grammer mistakes")
    att.geometry('300x300')
    Label(att, text= matches, fg="black").pack()
    

def mistakes():
    att = Toplevel()
    att.title('Info')
    att.geometry('300x300')
    a = str(i)
    b = str(count)
    c = str(matched_word)
    Label(att, text= "Total number of words written:"+b , fg="black").pack()
    Label(att, text="No of words matched with keyword:"+c, fg = "black").pack()
    Label(att, text = "No of grammetical mistakes:"+a, fg = "black").pack()
    link1 = Label(att, text="click here to view", fg="blue", cursor="hand2").pack()
    button1= Button(att, text = "view", command = grammer).pack()
    
def show_marks():
    att = Toplevel()
    att.title('Results')
    att.geometry('300x300')
    Marks = Decimal(l[0][1]*100).quantize(Decimal("1.0"))
    m = str(Marks)
    a = str(i)
    print (m)
    if (Marks>=40):
        Label(att, text= m+ "\t pass", fg = "green").pack()   
    else:
        Label(att, text= m+ "\t fail", fg = "red").pack()
    
   # Label(att, text = "no of grammetical mistakes:"+a, fg = "blue").pack()
    button = Button(att, text = "info", command = mistakes).pack()
    button = Button(att, text = "exit", command = att.destroy)
    button.pack()

def main():
    root = Tk()
    root.title("AnswerSheet Evaluation App")
    root.minsize(width=300, height=300)
    root.maxsize(width=300, height=300)
    button = Button(root, text="Results", command = show_marks)
    button.pack()
    button = Button(root, text="Exit", command = root.destroy)
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
    
