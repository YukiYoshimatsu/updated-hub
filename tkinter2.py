from Tkinter import *


window = Tk()


def your_hub(wind):
  wind.withdraw()
  hub = Tk()
  hub.title("Central Hub")
  hub.geometry('300x300')
  lbl = Label(hub, text="Please select a lesson to learn")
  lbl.grid(column=0, row=3)

  btn = Button(hub, text="1", bg="green", fg="blue", command=lambda: next_widget(hub))
  btn.grid(column=0, row=8)
  btn2 = Button(hub, text="2", bg="red", fg="green", command=lambda: flash(hub, root))
  btn2.grid(column=0, row=12)
  btn3 = Button(hub, text="3", bg="blue", fg="red", command=lambda: final(hub, root))
  btn3.grid(column=0, row=16)
  root = Tk()
  T = Text(root, height=5, width=80)
  T.pack()
  T.insert(END,
           "Much like in english, spanish words also have a plural form. Of course, this plural form also comes with it's own gender assignment\nThe masculine form for plural is [los] the feminine form for plural is [las]. Here's some examples\n")
  mainloop()
  hub.mainloop()


def flash(now, txt):
  now.withdraw()
  txt.withdraw()
  fc = Tk()
  fc.title("Flashcards")
  fc.geometry('300x300')
  labs = Label(fc, text="Here are some flashcards with Spanish to English words")
  labs.grid(column=0, row=4)
  start = Button(fc, text="Start", bg="blue", fg="green", command=lambda: cards(fc))
  start.grid(column=0, row=6)
  fc.mainloop()


def cards():
  flashcard = Tk()
  flashcard.geometry('100x100')
  flashcard.title("First")
  lbl = Label("Ayudar")
  lbl.grid(column=2,row=2)
  btn = Button(flashcard, text="English", command=lambda: cards)
  btn.grid(column=2,row=4)
  flashcard.mainloop()


def next_widget(win):
  win.withdraw()
  page = Tk()
  page.title("Welcome to LikeGeeks app")
  page.geometry('300x350')

  lbl = Label(page, text="el  chico")
  lbl.grid(column=1, row=6)
  lbl2 = Label(page, text="la  chica")
  lbl2.grid(column=1, row=7)
  lbl = Label(page, text="el  juego")
  lbl.grid(column=1, row=8)
  lbl2 = Label(page, text="la  doctora")
  lbl2.grid(column=1, row=9)
  lbl = Label(page, text="el  dia")
  lbl.grid(column=1, row=10)
  lbl2 = Label(page, text="la  mano")
  lbl2.grid(column=1, row=11)

  btn = Button(page, text="Keep Going", bg="red", fg="green", command=lambda: newPage(page, root))
  btn.grid(column=0, row=12)
  root = Tk()
  T = Text(root, height=5, width=80)
  T.pack()
  T.insert(END,
           "Welcome to <insertname>, here you will learn about gender assingnment of Spanish nouns.\nMasculine words have the word [el] assigned to them, and are usually used on words ending in e,o,u. Feminine words have the word [la] assigned to them and typically en in a or i.\nOf course there are exceptions, such as words like 'dia' or 'mano'. Please exit this window when finished with this lesson.\n")
  mainloop()
  page.mainloop()


def newPage(p, t):
  p.withdraw()
  t.withdraw()
  widge = Tk()
  widge.title("Welcome to LikeGeeks app")
  widge.geometry('300x350')

  lbl = Label(widge, text="chico")
  lbl.grid(column=1, row=6)
  lbl2 = Label(widge, text="chica")
  lbl2.grid(column=1, row=7)

  txt = Entry(widge, width=10)
  txt.grid(column=0, row=6)
  txt2 = Entry(widge, width=10)
  txt2.grid(column=0, row=7)

  lbl = Label(widge, text="juego")
  lbl.grid(column=1, row=8)
  lbl2 = Label(widge, text="doctora")
  lbl2.grid(column=1, row=9)

  txt = Entry(widge, width=10)
  txt.grid(column=0, row=8)
  txt2 = Entry(widge, width=10)
  txt2.grid(column=0, row=9)
  btn = Button(widge, text="Next", bg="green", fg="blue", command=lambda: last(widge, root))
  btn.grid(column=0, row=12)

  root = Tk()
  T = Text(root, height=5, width=80)
  T.pack()
  T.insert(END,
           "Now that you're familiar with some of the words we'll quiz you. Here are a list of words, it's your job to place the proper gender assignment, good luck!\n\n")
  mainloop()

  widge.mainloop()


def last(w, t):
  w.withdraw()
  t.withdraw()
  i = Tk()
  i.title("Welcome to LikeGeeks app")
  i.geometry('300x350')

  lbl = Label(i, text="los  chicos")
  lbl.grid(column=1, row=6)
  lbl2 = Label(i, text="las  chicas")
  lbl2.grid(column=1, row=7)
  lbl = Label(i, text="los  juegos")
  lbl.grid(column=1, row=8)
  lbl2 = Label(i, text="las  doctoras")
  lbl2.grid(column=1, row=9)
  lbl = Label(i, text="los  dias")
  lbl.grid(column=1, row=10)
  lbl2 = Label(i, text="las  manos")
  lbl2.grid(column=1, row=11)

  btn = Button(i, text="Next", bg="green", fg="blue", command=lambda: final(i, root))
  btn.grid(column=0, row=12)

  root = Tk()
  T = Text(root, height=5, width=80)
  T.pack()
  T.insert(END,
           "Much like in english, spanish words also have a plural form. Of course, this plural form also comes with it's own gender assignment\nThe masculine form for plural is [los] the feminine form for plural is [las]. Here's some examples\n")
  mainloop()
  i.mainloop()

def final(w, t):
  w.withdraw()
  t.withdraw()
  x = Tk()
  x.title("Welcome to LikeGeeks app")
  x.geometry('300x350')

  lbl = Label(x, text="chicos")
  lbl.grid(column=1, row=6)
  lbl2 = Label(x, text="chicas")
  lbl2.grid(column=1, row=7)

  txt = Entry(x, width=10)
  txt.grid(column=0, row=6)
  txt2 = Entry(x, width=10)
  txt2.grid(column=0, row=7)

  lbl = Label(x, text="juegos")
  lbl.grid(column=1, row=8)
  lbl2 = Label(x, text="doctoras")
  lbl2.grid(column=1, row=9)

  txt = Entry(x, width=10)
  txt.grid(column=0, row=8)
  txt2 = Entry(x, width=10)
  txt2.grid(column=0, row=9)
  x.mainloop()

def clicked():
  messagebox.showinfo('Message title', 'Thank you for testing the prototype of Duolongo2')
  messagebox.showwarning('Message title', 'Be warned this software is still in development')  # shows warning message
  messagebox.showerror('Message title', 'Message content')  # shows error
  lbl.configure(text="Button was clicked !!")


window.title("Duolingo")
window.geometry('300x300')
lbl = Label(window, text="Basic Spanish Study")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=0, row=1)

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

lbl2 = Label(window, text="Please select your proficiency(Choose One!)")
lbl2.grid(column=0, row=3)
chk_state = BooleanVar()
chk2_state = BooleanVar()
chk3_state = BooleanVar()
chk4_state = BooleanVar()
chk_state.set(False)  # set check state
chk2_state.set(False)
chk3_state.set(False)
chk4_state.set(False)

chk = Checkbutton(window, text='I am a native Speaker', var=chk_state)
chk2 = Checkbutton(window, text='I am very good at Spanish', var=chk2_state)

chk3 = Checkbutton(window, text='I know a little Spanish', var=chk3_state)
chk4 = Checkbutton(window, text='I have no experience in Spanish', var=chk4_state)

chk.grid(column=0, row=7)
chk2.grid(column=0, row=8)
chk3.grid(column=0, row=9)
chk4.grid(column=0, row=10)

btn = Button(window, text="Let's Begin", bg="green", fg="blue", command=lambda: your_hub(window))
btn.grid(column=0, row=12)
btn2 = Button(window, text='Click here', command=clicked)
btn2.grid(column=0, row=15)

window.mainloop()
