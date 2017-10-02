# this is my latest version of my game which has somehow better parts from its last versions which was crreated by me
#isme mene input block dikhaya h jab bhi high score toote ga to vo box aajaega 
#in this version ,we have open anorther service which will save the name of the person who score highest
from tkinter import *
import random
import time
pausevalue=False#version3
pointheight=0#version5
pointwidth=0
root=Tk()#version7.1
tk = Tk()
equa=""#version7.1
tk. title("Bounce!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0)
canvas.pack() 
tk.update()
#hit=0#version2  version5.5
bonus=-1#version5.5
class Ball:
    def __init__(self, canvas,paddle,point,color ):#version5
        global pointheight,pointwidth
        self.canvas = canvas # comment no 1
        self.paddle=paddle
        self.point=point#veersion5
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id,245,100)
        start00 = [-2,-1,0,1,2]#version6.1
        random.shuffle(start00)
        self.x=start00[0]# to move in any direction in horizontal
        self.y=-1.5#version6.1#version 7.1
        self.canvas_height = self.canvas.winfo_height()
        pointheight=self.canvas_height#version5
        self.canvas_width = self.canvas.winfo_width()
        pointwidth=self.canvas_width #version
        self.hit_bottom = False
        self.hit_point1=False
        self.hit_pointcheck=True
    def draw(self):
        global hit,bonus
        self.canvas.move(self.id,self.x ,self.y)# we are using 'self.canvas.move()' instead of 'canvas.move()' bcoz we hv to use it as parameter we have to initialize if u see the comment no.1 sentence because of this ,
        #whenever v use canvas v hv to use like self.canvas
        pos = self.canvas.coords(self.id) #will return x1,y1x2,y2 of ball

        if pos[1] <= 0:  #here in above codes elif use isliye ni kiya may be (x,y) coordinate dono(-x,-y) me chle jaenge to problm hogi isliye use all statements as if if if 
            self.y = 3#version6.1
        if pos[3] >= self.canvas_height:
           
           self.hit_bottom = True
           canvas.create_text(245,100,text="Game Over",font=5)
           canvas.create_text(245,130,text=" YOUR SCORE IS "+ str(bonus),font=5)#version5.5
           #version6.1 strts
           fo=open("test.txt","r")
           temp=fo.read()
           high_score=int(temp)
           fo.close()
           if bonus > high_score: 
               fo=open("test.txt","w+")
               fo.write(str(bonus))
               fo.close() 

               #version7.1 begins
               equation=StringVar()
               #root.wm_attributes("-topmost", 1)# agar me is koline 81 pe rkh dunga to ek problm saari h ki tk krke koi box khul ra h 
               root.geometry("400x400")
               king=Label(root,textvariable=equation)
               equation.set("enter your name:")
               king.grid(columnspan=4)
               king.place(x=100,y=60)
               def btnpress(num):
                   global equa 
                   equa=equa+ num
                   equation.set(equa)
               def okf():
                   fo=open("name.txt","w+")
                   fo.write(equa)
                   fo.close()
                   fo=open("name.txt","r")
                   namep=fo.read()
                   fo.close()                   
                   canvas.create_text(245,160,text="COGRATS "+ str(namep),font=5)
                   canvas.create_text(245,145,text="COGRATS NEW HIGH SCORE  IS "+ str(bonus),font=5)                
                   tk.deiconify()#window will maximize
                   root.iconify()
                   messagebox.showinfo("HIGH SCORE","NewKing is "+namep)
               bq=Button(root,text="q",command= lambda:btnpress("q"),bd=5,relief=RAISED,bg="red")
               bq.place(x=50,y=80)
               bw=Button(root,text="w",command= lambda:btnpress("w"),bd=5,relief=RAISED,bg="red")
               bw.place(x=75,y=80)
               be=Button(root,text="e",command= lambda:btnpress("e"),bd=5,relief=RAISED,bg="red")
               be.place(x=100,y=80)
               br=Button(root,text="r",command= lambda:btnpress("r"),bd=5,relief=RAISED,bg="red")
               br.place(x=125,y=80)
               bt=Button(root,text="t",command= lambda:btnpress("t"),bd=5,relief=RAISED,bg="red")
               bt.place(x=150,y=80)
               by=Button(root,text="y",command= lambda:btnpress("y"),bd=5,relief=RAISED,bg="red")
               by.place(x=175,y=80)
               bu=Button(root,text="u",command= lambda:btnpress("u"),bd=5,relief=RAISED,bg="red")
               bu.place(x=200,y=80)
               bi=Button(root,text="i",command= lambda:btnpress("i"),bd=5,relief=RAISED,bg="red")
               bi.place(x=225,y=80)
               bo=Button(root,text="o",command= lambda:btnpress("o"),bd=5,relief=RAISED,bg="red")
               bo.place(x=250,y=80)
               bp=Button(root,text="p",command= lambda:btnpress("p"),bd=5,relief=RAISED,bg="red")
               bp.place(x=275,y=80)
               ba=Button(root,text="a",command= lambda:btnpress("a"),bd=5,relief=RAISED,bg="red")
               ba.place(x=60,y=110)
               bs=Button(root,text="s",command= lambda:btnpress("s"),bd=5,relief=RAISED,bg="red")
               bs.place(x=85,y=110)
               bd=Button(root,text="d",command= lambda:btnpress("d"),bd=5,relief=RAISED,bg="red")
               bd.place(x=110,y=110)
               bf=Button(root,text="f",command= lambda:btnpress("f"),bd=5,relief=RAISED,bg="red")
               bf.place(x=135,y=110)
               bg=Button(root,text="g",command= lambda:btnpress("g"),bd=5,relief=RAISED,bg="red")
               bg.place(x=160,y=110)
               bh=Button(root,text="h",command= lambda:btnpress("h"),bd=5,relief=RAISED,bg="red")
               bh.place(x=185,y=110)
               bj=Button(root,text="j",command= lambda:btnpress("j"),bd=5,relief=RAISED,bg="red")
               bj.place(x=210,y=110)
               bk=Button(root,text="k",command= lambda:btnpress("k"),bd=5,relief=RAISED,bg="red")
               bk.place(x=235,y=110)
               bl=Button(root,text="l",command= lambda:btnpress("l"),bd=5,relief=RAISED,bg="red")
               bl.place(x=260,y=110)
               bz=Button(root,text="z",command= lambda:btnpress("z"),bd=5,relief=RAISED,bg="red")
               bz.place(x=70,y=140)
               bx=Button(root,text="x",command= lambda:btnpress("x"),bd=5,relief=RAISED,bg="red")
               bx.place(x=95,y=140)
               bc=Button(root,text="c",command= lambda:btnpress("c"),bd=5,relief=RAISED,bg="red")
               bc.place(x=120,y=140)
               bv=Button(root,text="v",command= lambda:btnpress("v"),bd=5,relief=RAISED,bg="red")
               bv.place(x=145,y=140)
               bb=Button(root,text="b",command= lambda:btnpress("b"),bd=5,relief=RAISED,bg="red")
               bb.place(x=170,y=140)
               bn=Button(root,text="n",command= lambda:btnpress("n"),bd=5,relief=RAISED,bg="red")
               bn.place(x=195,y=140)
               bm=Button(root,text="m",command= lambda:btnpress("m"),bd=5,relief=RAISED,bg="red")
               bm.place(x=220,y=140)
               ok=Button(root,text="ok",command=okf,bd=5,relief=RAISED,bg="red")
               
               ok.place(x=125,y=200)
               tk.iconify()# minimization of screen

               #version7.1 ends
               
           #canvas.create_text(245,115,text="score is "+ str(hit),font=5)#version2 this will give u score how many time u hit the blue stick
        if pos[0]<=0:
            self.x=3#version 6.1#version7.1
        if pos[2] >= self.canvas_width:
            self.x = -3#version6.1#version7.1
        if self.hit_paddle(pos) == True:
            self.y = -3#version6.1#version7.1
            #hit=hit+1#version2#version5.5 
        if self.hit_point(pos)== True:
                sta=[1,2,3]#version 5.3 #version6.1#verson7.1
                random.shuffle(sta)#version 5.3
                self.y=sta[0]#version5.3
                staaa=[1,-1]#version 5.3 #version6.1#version7.1
                random.shuffle(staaa)#version 5.3
                self.x=staaa[0]
                self.hit_point1=True#version5ends
                self.hit_pointcheck=False
                bonus=bonus+1#version5.5

    def hit_paddle(self,pos):# now coming equation wll tell whether ball get hit to paddle by measurng the point where the ball hit the paddle
#if the ball hitting point lie on tht paddle then will return true
        paddle_pos = self.canvas.coords(self.paddle.id)#will give the position of paddle
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                
                return True
               
            return False
    def hit_point(self,pos):#see the above comment for hit_paddle
      pos1 = self.canvas.coords(self.point.id)#will give the info of target position
      if pos[2] >= pos1[0] and pos[0] <= pos1[2]:
            if pos[3] >= pos1[1] and pos[3] <= pos1[3]:
          
               return True
      
            return False
      
    
       
        
class Paddle:
    
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)         
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

 
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 1#version5.1
        if pos[2] >= self.canvas_width:
            self.x = -1#version5.1
        
    def turn_left(self,evt):
        self.x = -4#version7.2
    def turn_right(self,evt):
        self.x = 4#version7.2
# version5 begins
class Point:
    def __init__(self,canvas,color):
        self.canvas=canvas
     
        self.id=canvas.create_rectangle(0,0,40,20,fill=color)
        self.canvas.move(self.id,250,100)
        start1=[-30,-20,-10,10,20,30,40,50]
        random.shuffle(start1)
        self.x=start1[0]
        self.y=start1[1]

    def draw(self):
        global pointheight,pointwidth
        start1=[-70,-60,-40,40,50,60,70]#version 5.3
        random.shuffle(start1)#version 5.3
        
        self.x=start1[0]#version5.3
        self.y=start1[1]#version5.3
        #version 5.4 beginss
        pos1 = self.canvas.coords(self.id)
         
        pointcheckheight=pointheight/4
       
        pointcheckwidth=pointwidth
       
        if pos1[0]+self.x <= 5:#version5.4
              self.x=100#cersion5.3
        if pos1[1] +self.y >=125:
            self.y=-100
             
        if pos1[1]+self.y <= 5:#version5.4
             self.y=100#version5.3
             
       
        if pos1[0]+self.x >=460:#version5.4 #version 6.1    
            self.x = -100#version 5.3
     
        self.canvas.move(self.id,self.x,self.y)#version5.4
        
      
point=Point(canvas,"brown")
paddle=Paddle(canvas,"blue")
ball=Ball(canvas,paddle,point,"red")



def pau():#version3
    global pausevalue#version3
    pausevalue=True#version3 
    ans=messagebox.askquestion("user","u want to continue??")# version4
    
    if ans=="yes": #version4
        pla()#version4
def pla():#version3
    global pausevalue#version3
    pausevalue=False#version3
pause=Button(tk,text="PAUSE",relief =RAISED,command=pau)#version3
pause.pack(side=LEFT)#version3
play=Button(tk,text="PLAY",command=pla,relief =RAISED)#version3
play.pack(side=LEFT)#version3

while 1:
    
    if  pausevalue== False:#version3
        if ball.hit_bottom == False:
         ball.draw()
         if ball.hit_point1 ==True:
              if ball.hit_pointcheck==False:
                  point.draw()
              ball.hit_point1=False
         paddle.draw()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
        
