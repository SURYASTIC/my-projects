from tkinter import *

score1=0
wicket1=0
B1score1=0
B2score1=0
B1BallsPl=0
B2BallsPl=0
Tballs=0
Tovers=0


class Cricket:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1270x880+0+0')
        self.root.config(bg="Black")

#Frame1 **************************************************************
        frame1=Frame(self.root)
        frame1.place(x=300,y=100,width=700,height=50)


#Team Label
        self.t_name=StringVar()
        self.t_name.set("Canada")
        self.teamlabel=Label(frame1,text="",textvariable=self.t_name,font=("",15,'bold'))
        self.teamlabel.pack(side=LEFT)

#Score Label
        self.score=StringVar()
        self.score.set("0")
        self.scorelabel=Label(frame1,text="",textvariable=self.score,font=("",15))
        self.scorelabel.pack(side=LEFT,padx=(10,0))

#Wickets Label
        self.wicket=StringVar()
        self.wicket.set(" -  0   ")
        self.wicketlabel=Label(frame1,text="",textvariable=self.wicket,font=("",15))
        self.wicketlabel.pack(side=LEFT)

#Over Label
        self.over=StringVar()
        self.over.set("")
        self.overlabel=Label(frame1,text="",textvariable=self.over,font=("",15))
        self.overlabel.pack(side=LEFT,padx=(10,0))

#Balls Label
        self.balls=StringVar()
        self.balls.set("")
        self.ballslabel=Label(frame1,text="",textvariable=self.balls,font=("",15))
        self.ballslabel.pack(side=LEFT)

#Total Over Label
        self.tover=StringVar()
        self.tover.set(" Bulgaria ")
        self.toverlabel=Label(frame1,text="",textvariable=self.tover,font=("",15))
        self.toverlabel.pack(side=LEFT)





#Frame 2 ************************************************************** 
        frame2=Frame(self.root)
        frame2.place(x=300,y=200,width=750,height=300)


#Run Buttons
        totalscorelabel=Label(frame2,text="T1 Goals",font=("",13)).place(x=0,y=5)
        
     

        score2button=Button(frame2,text="+1",font=("",15),command=self.score1)  
        score2button.place(x=40,y=40)

      

        score6button=Button(frame2,text="-1",font=("",15),command=self.score6)  
        score6button.place(x=40,y=130)


# Wickets Label and Buttons
        totalwicketslabel=Label(frame2,text="T2 Goals",font=("",13)).place(x=0,y=190)

        wicketbutton=Button(frame2,text="+1",font=("",15),command=self.wickets)
        wicketbutton.place(x=10,y=210)

        _wicketbutton=Button(frame2,text="-1",font=("",15),command=self._wickets)
        _wicketbutton.place(x=80,y=210)


# Batsman 1 Buttons
        B1scorebutton=Label(frame2,text="D square",font=("",13)).place(x=200,y=5)

        
        B1scorebutton2=Button(frame2,text="+1",font=("",15),command=self.B1score2)
        B1scorebutton2.place(x=240,y=40)

        

        B1scorebutton6=Button(frame2,text="-1",font=("",15),command=self.B1score6)
        B1scorebutton6.place(x=240,y=130)

        B1ballbutton=Label(frame2,text="T2 D square",font=("",13)).place(x=200,y=190)

        B1ballbutton=Button(frame2,text="+1",font=("",15),command=self.B1Ball)
        B1ballbutton.place(x=200,y=210)

        _B1ballbutton=Button(frame2,text="-1",font=("",15),command=self._B1Ball)
        _B1ballbutton.place(x=270,y=210)



# Total Balls Button
       


# Frame 3
        frame3=Frame(self.root)
        frame3.place(x=300,y=550,width=700,height=200)

        TotalOverlabel=Label(frame3,text="Time in Mins",font=("",13)).place(x=10,y=20)

        self.TotalOverentry=Entry(frame3,font=("",10))
        self.TotalOverentry.place(x=10,y=50)

        TotalOverbutton=Button(frame3,text="Update",font=("",12))
        TotalOverbutton.place(x=40,y=100)

        B1Namelabel=Label(frame3,text="Red card",font=("",13)).place(x=170,y=20)

        self.B1Nameentry=Entry(frame3,font=("",10))
        self.B1Nameentry.place(x=170,y=50)

        B1Namebutton=Button(frame3,text="Update",font=("",12),command=self.update_B1)
        B1Namebutton.place(x=210,y=100)

        B2Namelabel=Label(frame3,text="Add a Player",font=("",13)).place(x=330,y=20)

        self.B2Nameentry=Entry(frame3,font=("",10))
        self.B2Nameentry.place(x=330,y=50)

        B2Namebutton=Button(frame3,text="Update",font=("",12),command=self.update_B2)
        B2Namebutton.place(x=370,y=100)

        TeamNamelabel=Label(frame3,text="Team Name of the player",font=("",13)).place(x=490,y=20)

        self.TeamNameentry=Entry(frame3,font=("",10))
        self.TeamNameentry.place(x=490,y=50)

        TeamNamebutton=Button(frame3,text="Update",font=("",12),command=self.Update_TeaMName)
        TeamNamebutton.place(x=530,y=100)


#Team Score

    def score1(self):
            global score1
            score1+=1
            self.score.set(score1)

    def score2(self):
            global score1
            score1+=2
            self.score.set(score1)

    def score3(self):
            global score1
            score1+=3
            self.score.set(score1)

    def score4(self):
            global score1
            score1+=4
            self.score.set(score1)

    def score5(self):
            global score1
            score1+=6
            self.score.set(score1)

    def score6(self):
            global score1
            score1-=1
            self.score.set(score1)


#Wickets
    def wickets(self):
            global wicket1
            wicket1+=1
            w=self.wicket.set("-"+str(wicket1))
            if(wicket1==10):
                    self.wicket.set(" ")
                    wicket1=0

    def _wickets(self):
            global wicket1
            wicket1-=1
            self.wicket.set("-"+str(wicket1))

#Overs
    def update_overs(self):
            a=self.TotalOverentry.get()
            self.tover.set("/ "+a)
            self.TotalOverentry.delete(0,'end')


#Batsman 1 Stats

    def B1score1(self):
            global B1score1
            global score1
            global B1BallsPl
            global Tballs,Tovers
            Tballs+=1
            B1BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B1balls.set("(" + str(B1BallsPl) + ")")
            score1+=1
            B1score1+=1
            self.B1score.set(B1score1)
            self.score.set(score1)

    def B1score2(self):
            global B1score1
            global score1
            global B1BallsPl
            global Tballs,Tovers
            Tballs+=1
            B1BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B1balls.set("(" + str(B1BallsPl) + ")")
            score1+=2
            B1score1+=2
            self.B1score.set(B1score1)
            self.score.set(score1)

    def B1score3(self):
            global B1score1
            global score1
            global B1BallsPl
            global Tballs,Tovers
            Tballs+=1
            B1BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B1balls.set("(" + str(B1BallsPl) + ")")
            score1+=3
            B1score1+=3
            self.B1score.set(B1score1)
            self.score.set(score1)

    def B1score4(self):
            global B1score1
            global score1
            global B1BallsPl
            global Tballs,Tovers
            Tballs+=1
            B1BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B1balls.set("(" + str(B1BallsPl) + ")")
            score1+=4
            B1score1+=4
            self.B1score.set(B1score1)
            self.score.set(score1)

    def B1score5(self):
            global B1score1
            global score1
            global B1BallsPl
            global Tballs,Tovers
            Tballs+=1
            B1BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B1balls.set("(" + str(B1BallsPl) + ")")
            score1+=6
            B1score1+=6
            self.B1score.set(B1score1)
            self.score.set(score1)

    def B1score6(self):
            global B1score1
            global score1
            score1-=1
            B1score1-=1
            self.B1score.set(B1score1)
            self.score.set(score1)

    def B1Ball(self):
            global B1BallsPl
            global Tballs,Tovers
            Tballs+=1
            B1BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B1balls.set("(" + str(B1BallsPl) + ")")

    def _B1Ball(self):
            global B1BallsPl
            B1BallsPl-=1
            global Tballs,Tovers
            if(Tballs==0):
                    Tballs=5
                    self.balls.set("."+str(Tballs))
                    Tovers-=1
                    self.over.set(Tovers)
            else:
                    Tballs-=1
                    self.balls.set("."+str(Tballs))
            self.B1balls.set("(" + str(B1BallsPl) + ")")


#Batsman 2 Stats

    def B2score1(self):
            global B2score1
            global score1
            global B2BallsPl
            global Tballs,Tovers
            Tballs+=1
            B2BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B2balls.set("(" + str(B2BallsPl) + ")")
            score1+=1
            B2score1+=1
            self.B2score.set(B2score1)
            self.score.set(score1)

    def B2score2(self):
            global B2score1
            global score1
            global B2BallsPl
            global Tballs,Tovers
            Tballs+=1
            B2BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B2balls.set("(" + str(B2BallsPl) + ")")
            score1+=2
            B2score1+=2
            self.B2score.set(B2score1)
            self.score.set(score1)

    def B2score3(self):
            global B2score1
            global score1
            global B2BallsPl
            global Tballs,Tovers
            Tballs+=1
            B2BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B2balls.set("(" + str(B2BallsPl) + ")")
            score1+=3
            B2score1+=3
            self.B2score.set(B2score1)
            self.score.set(score1)

    def B2score4(self):
            global B2score1
            global score1
            global B2BallsPl
            global Tballs,Tovers
            Tballs+=1
            B2BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B2balls.set("(" + str(B2BallsPl) + ")")
            score1+=4
            B2score1+=4
            self.B2score.set(B2score1)
            self.score.set(score1)

    def B2score5(self):
            global B2score1
            global score1
            global B2BallsPl
            global Tballs,Tovers
            Tballs+=1
            B2BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B2balls.set("(" + str(B2BallsPl) + ")")
            score1+=6
            B2score1+=6
            self.B2score.set(B2score1)
            self.score.set(score1)

    def B2score6(self):
            global B2score1
            global score1
            score1-=1
            B2score1-=1
            self.B2score.set(B2score1)
            self.score.set(score1)

    def B2Ball(self):
            global B2BallsPl
            global Tballs,Tovers
            Tballs+=1
            B2BallsPl+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)
            self.B2balls.set("(" + str(B2BallsPl) + ")")

    def _B2Ball(self):
            global B2BallsPl
            B2BallsPl-=1
            global Tballs,Tovers
            if(Tballs==0):
                    Tballs=5
                    self.balls.set("."+str(Tballs))
                    Tovers-=1
                    self.over.set(Tovers)
            else:
                    Tballs-=1
                    self.balls.set("."+str(Tballs))
            self.B2balls.set("(" + str(B2BallsPl) + ")")

#Update Batsman Name 
    def update_B1(self):
            a=self.B1Nameentry.get()
            self.B1.set(a)
            B1score1 = 0
            self.B1score.set("0")
            self.B1balls.set("(0)")
            global wicket1
            wicket1+=1
            w=self.wicket.set("-"+str(wicket1))
            if(wicket1==10):
                    self.wicket.set(" ")
                    wicket1=0
            self.B1Nameentry.delete(0,'end')

    def update_B2(self):
            a=self.B2Nameentry.get()
            self.B2.set(a)
            B2score1 = 0
            self.B2score.set("0")
            self.B2balls.set("(0)")
            global wicket1
            wicket1+=1
            w=self.wicket.set("-"+str(wicket1))
            if(wicket1==10):
                    self.wicket.set(" ")
                    wicket1=0
            self.B2Nameentry.delete(0,'end')
# Update Team Name
    def Update_TeaMName(self):
            a=self.TeamNameentry.get()
            self.t_name.set(a)
            self.TeamNameentry.delete(0,'end')

#Total Balls
    def Total_Balls(self):
            global Tballs,Tovers
            Tballs+=1
            self.balls.set("."+str(Tballs))
            if(Tballs>5):
                    self.balls.set(".0")
                    Tballs=0
                    Tovers+=1
                    self.over.set(Tovers)

    def _Total_Balls(self):
            global Tballs,Tovers
            if(Tballs==0):
                    Tballs=5
                    self.balls.set("."+str(Tballs))
                    Tovers-=1
                    self.over.set(Tovers)
            else:
                    Tballs-=1
                    self.balls.set("."+str(Tballs))



if __name__=="__main__":
    root=Tk()
    app=Cricket(root)
    root.mainloop()