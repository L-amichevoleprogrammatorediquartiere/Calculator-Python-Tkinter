from tkinter import *
class Calculator:
     def Labelgest(self,x):
          if x=='del':
               self.testo=self.testo[:-1]
               self.testo2=self.testo2[:-1]
          elif x=='canc':
               self.testo=''
               self.testo2=''
          else:
               self.testo+=x
               if x=='=':
                    try:
                         ris=eval(self.testo2)
                         self.ris2=str(ris)
                         self.testo+=self.ris2
                         self.testo2=self.ris2
                    except:
                         self.testo=''
                         self.testo2='Syntax Error   '
               else:
                    if self.ris2!='0':
                         self.testo=self.ris2
                    self.testo2+=x
          self.cron= Label(self.area,text=self.testo,width=29,anchor='e',font='Arial 12',fg='gray')
          self.cron.pack()
          self.cron.place(x=8,y=20)
          self.scritto= Label(self.area,text=self.testo2,width=14,anchor='e',font='Arial 25')
          self.scritto.pack()
          self.scritto.place(x=4,y=47)
     def number(self,y):
          for i in ['1','2','4','5','6','7','8','9','0','.','+','-','*','/','=','del','canc']:
               if y==i:
                    self.Labelgest(i)
     def __init__ (self,root):
          self.area = Frame(root, width=280, height=100, highlightbackground="green",
                            highlightthickness="1.5")
          self.area.pack()
          self.area.place(x=10, y=30)
          self.root=root
          root.configure(bg='gray')
          self.testo=''
          self.testo2=''
          self.ris2='0'
          x=-68   #+74
          y=190
          px=24
          nomebutton=['on','tw','th','fo','fi','si','se','ei','ni','ze','pu']
          for num in range(11):
               n=nomebutton[num]
               num+=1
               if x<=80:
                    x +=74
               else :
                    x=6
                    y+=43
               if num==10:
                    num=0
                    px=61
               elif num==11:
                    x +=74
                    num='.'
                    px=26
               self.n=Button(root, text=str(num), padx=px, pady=4, font='Arial 12', command=lambda num=num:self.number(str(num)))
               self.n.pack()
               self.n.place(x=x,y=y)
          self.ugu = Button(root, text='=', padx=22, pady=4, font='Arial 11 bold', command=lambda num=num:self.number('='), fg='green')
          self.ugu.pack()
          self.ugu.place(x=228, y=319)
          self.più = Button(root, text='+', padx=22, pady=4, font='Arial 11 bold', command=lambda num=num:self.number('+'), fg='blue')
          self.più.pack()
          self.più.place(x=228, y=276)
          self.men = Button(root, text='-', padx=24, pady=4, font='Arial 11 bold', command=lambda num=num:self.number('-'), fg='blue')
          self.men.pack()
          self.men.place(x=228, y=233)
          self.per = Button(root, text='*', padx=23, pady=4, font='Arial 11 bold', command=lambda num=num:self.number('*'), fg='blue')
          self.per.pack()
          self.per.place(x=228, y=190)
          self.div = Button(root, text='/', padx=23, pady=3, font='Arial 13 bold', command=lambda num=num:self.number('/'), fg='blue', )
          self.div.pack()
          self.div.place(x=228, y=147)
          self.can = Button(root, text='Canc', padx=10, pady=4, font='Arial 11 bold', command=lambda num=num:self.number('canc'), fg='blue')
          self.can.pack()
          self.can.place(x=154, y=147)
          self.el = Button(root, text='Del', padx=16, pady=4, font='Arial 12 bold', command=lambda num=num:self.number('del'), fg='blue')
          self.el.pack()
          self.el.place(x=80, y=147)
          self.menubar= Menu(root, tearoff=0)
          self.optionmenu= Menu(self.menubar, tearoff=0)
          self.colormenu= Menu(self.optionmenu,tearoff=0)
          colori=['White','Cornflower blue','Blue','Sky blue','Cyan','Dark green','Yellow','Gold','Red','Deep pink',
                       'Violet','Black']
          for i in range(12):
               c=colori[i]
               if c=='Black':
                    self.colormenu.add_command(label=c, background=c,foreground='White',command=lambda c=c: self.root.configure(bg=c))
               else:
                    self.colormenu.add_command(label=c,background=c, command=lambda c=c: self.root.configure(bg=c))
          self.optionmenu.add_cascade(label='Change color',menu=self.colormenu)
          self.menubar.add_cascade(label='Options',menu=self.optionmenu)
          root.config(menu=self.menubar)
def main():
     root=Tk()
     root.title('Calcolatrice')
     root.geometry('300x360')
     Calc=Calculator(root)
     root.mainloop()
main()
