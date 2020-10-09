#ADDING BUTTO
from tkinter import*
from tkinter.messagebox import *
import math as m
from audio import PlayAudio
import threading
font=('Verdana',22)
ob= PlayAudio(voice='female')

def clear():
       ex=textField.get()
       ex=ex[0:len(ex)-2]
       textField.delete(0,END)
       textField.insert(0, ex)


def all_clear():
    textField.delete(0,END)


#important function
def click_btn_function(event):
    print("btn clicked")
    B=event.widget
    text=B['text']
    print(text)
    ob.speak(text)
    t= threading.Thread(target=ob.speak,args=(text,))
    t.start()


    if text=='x':
        textField.insert(END,"*")
        return


    if text=='=':
      try:
         ex=textField.get()
         answer = eval(ex)
         textField.delete(0,END)
         textField.insert(0,answer)
      except Exception as e:
          print('error......',e)
          showerror('error',e)
      return






    textField.insert(END,text)


#creating a window
window=Tk()
window.title('My calc')
window.geometry('600x800')

#picteure label
#pic = PhotoImage(file='C:/Users/User/calc/img/pankaj.png')
#headingLabel= Label(window,image= pic)
#headingLabel.pack(side=TOP,pady=0)

#heading label
headingLabel= Label(window,text='My calculator',font=font,underline=0)
headingLabel.pack(side=TOP)
#TEXTFIELD
textField= Entry(window,font=font)
textField.pack(side=TOP,pady=10,fill=X,padx=10)
#buttons
buttonFrame=Frame(window)
buttonFrame.pack(side=TOP)

#ADDING BUTTON
temp=1
for i in range(0,3):
  for j in range(0,3):
      Btn=Button(buttonFrame,text=str(temp),font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
      Btn.grid(row=i,column=j,padx=3,pady=3)
      temp=temp+1
      Btn.bind('<Button-1>',click_btn_function)

zerobtn=Button(buttonFrame,text=0,font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
zerobtn.grid(row=3,column=0,padx=2,pady=2)

dotbtn=Button(buttonFrame,text='.',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
dotbtn.grid(row=3,column=1,padx=2,pady=2)

equalbtn=Button(buttonFrame,text='=',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
equalbtn.grid(row=3,column=2,padx=2,pady=2)

plusbtn=Button(buttonFrame,text='+',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
plusbtn.grid(row=0,column=3,padx=2,pady=2)


minusbtn=Button(buttonFrame,text='-',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
minusbtn.grid(row=1,column=3,padx=2,pady=2)


mulbtn=Button(buttonFrame,text='*',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
mulbtn.grid(row=2,column=3,padx=2,pady=2)


divbtn=Button(buttonFrame,text='/',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
divbtn.grid(row=3,column=3,padx=2,pady=2)


clearbtn=Button(buttonFrame,text='<',font=font,width=11,relief='solid',activebackground='blue',activeforeground='white',command=clear)
clearbtn.grid(row=4,column=0,padx=2,pady=2,columnspan=2)


Allclearbtn=Button(buttonFrame,text='AC',font=font,width=11,relief='solid',activebackground='blue',activeforeground='white',command=all_clear)
Allclearbtn.grid(row=4,column=2,padx=2,pady=2,columnspan=2)

#BIDING BUTTONS
zerobtn.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)
equalbtn.bind('<Button-1>',click_btn_function)
plusbtn.bind('<Button-1>',click_btn_function)
minusbtn.bind('<Button-1>',click_btn_function)
mulbtn.bind('<Button-1>',click_btn_function)
divbtn.bind('<Button-1>',click_btn_function)
clearbtn.bind('<Button-1>',click_btn_function)
####################################################################################3
#second vieddo funcationn....
scFrame=Frame(window)

sqrtbtn=Button(scFrame,text='√',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
sqrtbtn.grid(row=0,column=0,padx=2,pady=2)


powbtn=Button(scFrame,text='^',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
powbtn.grid(row=0,column=1,padx=2,pady=2)

factbtn=Button(scFrame,text='x!',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
factbtn.grid(row=0,column=2,padx=2,pady=2)

radbtn=Button(scFrame,text='toRad',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
radbtn.grid(row=0,column=3,padx=2,pady=2)

degbtn=Button(scFrame,text='toDeg',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
degbtn.grid(row=1,column=0,padx=2,pady=2)



sinbtn=Button(scFrame,text='sinθ',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
sinbtn.grid(row=1,column=1,padx=2,pady=2)


cosbtn=Button(scFrame,text='cosθ',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
cosbtn.grid(row=1,column=2,padx=2,pady=2)


tanbtn=Button(scFrame,text='tanθ',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
tanbtn.grid(row=1,column=3,padx=2,pady=2)


#aboutbtn=Button(scFrame,text='about',font=font,width=5,relief='solid',activebackground='blue',activeforeground='white')
#aboutbtn.grid(row=1,column=3,padx=3,pady=3)

normalcalc = True

def calculate_sc(event):
    print('btn..')
    btn=event.widget
    text=btn['text']
    print(text)
    ex=textField.get()
    answer=' '
    if text =='toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))

    elif text=='toRad':
        print('radian')
        answer = str(m.radians(float(ex)))

    elif text=='x!':
         print("cal factorial")
         answer= str(m.factorial(int(ex)))
    elif text=='sinθ':
        print("cal sin")
        answer=str(m.sin(m.radians(int(ex))))
    elif text=='cosθ':
        print("cal cos")
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        print("cal tan")
        answer = str(m.tan(m.radians(int(ex))))
    elif text=='√':
        print("squrt")
    elif text=='^':
        print("power")
    textField.delete(0,END)
    textField.insert(0,answer)





def sc_click():
    global normalcalc
    if normalcalc:
       buttonFrame.pack_forget()
       scFrame.pack(side=TOP,pady=20)
       buttonFrame.pack(side=TOP)
       window.geometry('510x700')
       print("show sc")
       normalcalc=False
    else:
        print("show normal")
        scFrame.pack_forget()
        window.geometry('510x550')
        normalcalc=True

#binding scintific buttons
sqrtbtn.bind("<Button-1>",calculate_sc)
powbtn.bind("<Button-1>",calculate_sc)
factbtn.bind("<Button-1>",calculate_sc)
radbtn.bind("<Button-1>",calculate_sc)
degbtn.bind("<Button-1>",calculate_sc)
sinbtn.bind("<Button-1>",calculate_sc)
cosbtn.bind("<Button-1>",calculate_sc)
tanbtn.bind("<Button-1>",calculate_sc)
#aboutbtn.bind("<Button-1>",ob.speak(text))




fontMenu = (" ", 15)
menubar=Menu(window,font=fontMenu)

mode=Menu(menubar,font=fontMenu,tearoff=0)
mode.add_checkbutton(label="Scintific Calculator",command=sc_click)
menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)







window.mainloop()
