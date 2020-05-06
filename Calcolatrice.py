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

     def unoPress(self):
          self.Labelgest('1')     
     def duePress(self):
          self.Labelgest('2')
     def trePress(self):
          self.Labelgest('3')
     def quaPress(self):
          self.Labelgest('4')
     def cinPress(self):
          self.Labelgest('5')
     def seiPress(self):
          self.Labelgest('6')
     def setPress(self):
          self.Labelgest('7')
     def ottPress(self):
          self.Labelgest('8')
     def novPress(self):
          self.Labelgest('9')
     def zerPress(self):
          self.Labelgest('0')
     def punPress(self):
          self.Labelgest('.')
     def piùPress(self):
          self.Labelgest('+')
     def menPress(self):
          self.Labelgest('-')
     def perPress(self):
          self.Labelgest('*')
     def divPress(self):
          self.Labelgest('/')
     def uguPress(self):
          self.Labelgest('=')
     def elPress(self):
          self.Labelgest('del')
     def canPress(self):
          self.Labelgest('canc')
     def whi(self):
          self.root.configure(bg='white')
     def cor(self):
          self.root.configure(bg='cornflower blue')
     def blu(self):
          self.root.configure(bg='blue')
     def sky(self):
          self.root.configure(bg='sky blue')
     def cya(self):
          self.root.configure(bg='cyan')
     def dgr(self):
          self.root.configure(bg='dark green')
     def yel(self):
          self.root.configure(bg='yellow')
     def gol(self):
          self.root.configure(bg='gold')
     def red(self):
          self.root.configure(bg='red')
     def pin(self):
          self.root.configure(bg='deep pink')
     def vio(self):
          self.root.configure(bg='violet')
     def bla(self):
          self.root.configure(bg='black')
     def __init__(self,root): #A root gli viene passato root=Tk()
          self.root=root
          root.configure(bg='gray')
          self.testo=''
          self.testo2=''
          self.ris2='0'
          ##-----------------------------------------------------------##
          self.uno=Button(root,text='1',padx=24,pady=4,font='Arial 12',command=self.unoPress)
          self.uno.pack()
          self.uno.place(x=6,y=190)
          ##-----------------------------------------------------------##
          self.due=Button(root,text='2',padx=24,pady=4,font='Arial 12',command=self.duePress)
          self.due.pack()
          self.due.place(x=80,y=190)
          ##-----------------------------------------------------------##
          self.tre=Button(root,text='3',padx=24,pady=4,font='Arial 12',command=self.trePress)
          self.tre.pack()
          self.tre.place(x=154,y=190)
          ##-----------------------------------------------------------##
          self.qua=Button(root,text='4',padx=24,pady=4,font='Arial 12',command=self.quaPress)
          self.qua.pack()
          self.qua.place(x=6,y=233)
          ##-----------------------------------------------------------##
          self.cin=Button(root,text='5',padx=24,pady=4,font='Arial 12',command=self.cinPress)
          self.cin.pack()
          self.cin.place(x=80,y=233)
          ##-----------------------------------------------------------##
          self.sei=Button(root,text='6',padx=24,pady=4,font='Arial 12',command=self.seiPress)
          self.sei.pack()
          self.sei.place(x=154,y=233)
          ##-----------------------------------------------------------##
          self.set=Button(root,text='7',padx=24,pady=4,font='Arial 12',command=self.setPress)
          self.set.pack()
          self.set.place(x=6,y=276)
          ##-----------------------------------------------------------##
          self.ott=Button(root,text='8',padx=24,pady=4,font='Arial 12',command=self.ottPress)
          self.ott.pack()
          self.ott.place(x=80,y=276)
          ##-----------------------------------------------------------##
          self.nov=Button(root,text='9',padx=24,pady=4,font='Arial 12',command=self.novPress)
          self.nov.pack()
          self.nov.place(x=154,y=276)
          ##-----------------------------------------------------------##
          self.zer=Button(root,text='0',padx=61,pady=4,font='Arial 12',command=self.zerPress)
          self.zer.pack()
          self.zer.place(x=6,y=319)
          ##-----------------------------------------------------------##
          self.ugu=Button(root,text='=',padx=22,pady=4,font='Arial 11 bold'
                          ,command=self.uguPress,fg='green')
          self.ugu.pack()
          self.ugu.place(x=228,y=319)
          ##-----------------------------------------------------------##
          self.pun=Button(root,text='.',padx=26,pady=4,font='Arial 12',command=self.punPress)
          self.pun.pack()
          self.pun.place(x=154,y=319)
          ##-----------------------------------------------------------##
          self.div=Button(root,text='/',padx=23,pady=3,font='Arial 13 bold',command=self.divPress
                          ,fg='blue',)
          self.div.pack()
          self.div.place(x=228,y=147)
          ##-----------------------------------------------------------##
          self.per=Button(root,text='*',padx=23,pady=4,font='Arial 11 bold',command=self.perPress
                          ,fg='blue')
          self.per.pack()
          self.per.place(x=228,y=190)
          ##-----------------------------------------------------------##
          self.men=Button(root,text='-',padx=24,pady=4,font='Arial 11 bold',command=self.menPress
                          ,fg='blue')
          self.men.pack()
          self.men.place(x=228,y=233)
          ##-----------------------------------------------------------##
          self.più=Button(root,text='+',padx=22,pady=4,font='Arial 11 bold',command=self.piùPress
                          ,fg='blue')
          self.più.pack()
          self.più.place(x=228,y=276)
          ##-----------------------------------------------------------##
          self.el=Button(root,text='Del',padx=16,pady=4,font='Arial 12 bold',command=self.elPress
                         ,fg='blue')
          self.el.pack()
          self.el.place(x=80,y=147)
          ##-----------------------------------------------------------##
          self.can=Button(root,text='Canc',padx=10,pady=4,font='Arial 11 bold',command=self.canPress
                          ,fg='blue')
          self.can.pack()
          self.can.place(x=154,y=147)
          ##-----------------------------------------------------------##
          self.area=Frame(root,width=280,height=100,highlightbackground="green",
                          highlightthickness="1.5")
          self.area.pack()
          self.area.place(x=10,y=30)
          ##-----------------------------------------------------------##
          self.menubar= Menu(root, tearoff=0)
          self.optionmenu= Menu(self.menubar, tearoff=0)
          self.colormenu= Menu(self.optionmenu,tearoff=0)
          self.colormenu.add_command(label='White',
                                     background='white',command=self.whi)
          self.colormenu.add_command(label='Cornflower blue',
                                     background='cornflower blue',command=self.cor)
          self.colormenu.add_command(label='Blue',
                                     background='blue',command=self.blu)
          self.colormenu.add_command(label='Sky blue',
                                     background='sky blue',command=self.sky)
          self.colormenu.add_command(label='Cyan',
                                     background='cyan',command=self.cya)
          self.colormenu.add_command(label='Dark green',
                                     background='dark green',command=self.dgr)
          self.colormenu.add_command(label='Yellow',
                                     background='yellow',command=self.yel)
          self.colormenu.add_command(label='Gold',
                                     background='gold',command=self.gol)
          self.colormenu.add_command(label='Red',
                                     background='red',command=self.red)
          self.colormenu.add_command(label='Deep pink',
                                     background='deep pink',command=self.pin)
          self.colormenu.add_command(label='Violet',
                                     background='violet',command=self.vio)
          self.colormenu.add_command(label='Black',
                                     background='black',
                                     foreground='white',command=self.bla)
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
