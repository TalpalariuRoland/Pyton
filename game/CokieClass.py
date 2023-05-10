import turtle
import time
import random
from tkinter import *
import json


class CokieClass:
    Cookie=turtle.Turtle()
    score=turtle.Turtle()
    ClickPowerLabel=turtle.Turtle()
    BonusOnClickPriceTagLv1=turtle.Turtle()
    PasivePowerLabel=turtle.Turtle()
    pasivePriceTag=turtle.Turtle()

    Score=0
    BonusOnClickPriceLv1=10
    ClickPover=1
    PowLv1=0
    MaxPowerLv1=10
    BonusOnClickGrowLv1=5
    passiveGrowth=0
    passiveGrowthPrice=20
    passiveGrowthGrow=2
    passiveGrowthMaxLv1=50



    def start(self):
        screen=turtle.Screen()
        self.score.penup()
        self.score.hideturtle()
        self.score.setposition(-screen.window_width()/2+10,screen.window_height()/2-40)
        scorestring ="Cookies: %s" % self.Score
        self.score.write(scorestring, font=("Arial",24, "normal"))
        self.Cookie=turtle.Turtle()

        self.BonusOnClickPriceTagLv1.hideturtle()
        self.BonusOnClickPriceTagLv1.penup()
        self.BonusOnClickPriceTagLv1.setposition(screen.window_width()/2 -150, screen.window_height()/2 -100)
        self.BonusOnClickPriceTagLv1.write("Price:" + format(self.BonusOnClickPriceLv1) )

        self.pasivePriceTag.hideturtle()
        self.pasivePriceTag.penup()
        self.pasivePriceTag.setposition(screen.window_width()/2 -150, screen.window_height()/2 -150)
        self.pasivePriceTag.write("Price:" + format(self.passiveGrowthPrice) )

        turtle.register_shape(name="C:\\Users\\talpa\Desktop\\pyton\\game\\chocolatechip.gif",shape=None)
        self.Cookie.shape("C:\\Users\\talpa\Desktop\\pyton\\game\\chocolatechip.gif")
        self.ClickPowerLabel.hideturtle()
        self.ClickPowerLabel.penup()
        self.ClickPowerLabel.setposition(0,screen.window_height()/2-40)
        self.ClickPowerLabel.write("Click Power level:" +format(self.ClickPover))

        self.PasivePowerLabel.hideturtle()
        self.PasivePowerLabel.penup()
        self.PasivePowerLabel.setposition(0,screen.window_height()/2-80)
        self.PasivePowerLabel.write("Passive Income:" +format(self.passiveGrowth))

    def clicked(self,x,y):
        self.Score=self.Score+self.ClickPover
        scorestring ="Cookies: %s" % self.Score
        self.score.clear()
        self.score.write(scorestring, font=("Arial",24, "normal"))

    def ClickPowerUpp(self):
        if self.BonusOnClickPriceLv1 <= self.Score :
            if self.PowLv1 < self.MaxPowerLv1 :
                self.ClickPover+=1
                self.Score=self.Score-self.BonusOnClickPriceLv1
                self.BonusOnClickPriceLv1=self.BonusOnClickPriceLv1*self.BonusOnClickGrowLv1
        self.scorestring ="Cookies: %s" % self.Score
        self.score.clear()
        self.score.write(self.scorestring, font=("Arial",24, "normal"))
        self.ClickPowerLabel.clear()
        self.ClickPowerLabel.write("Click Power level:" +format(self.ClickPover))
        self.BonusOnClickPriceTagLv1.clear()
        self.BonusOnClickPriceTagLv1.write("Price:" + format(self.BonusOnClickPriceLv1))
    
    def update_score(self):
        if self.passiveGrowth>0:
            passiveGrowth = self.passiveGrowth  
            self.Score += passiveGrowth
            self.scorestring ="Cookies: %s" % self.Score
            self.score.clear()
            self.score.write(self.scorestring, font=("Arial",24, "normal"))
            turtle.ontimer(self.update_score, 1000)
    
    def addPasive(self):
        
        if self.passiveGrowth< self.passiveGrowthMaxLv1:
            if self.passiveGrowthPrice <= self.Score:
                self.passiveGrowth+=1
                self.Score=self.Score-self.passiveGrowthPrice
                self.passiveGrowthPrice=self.passiveGrowthPrice*self.passiveGrowthGrow
                
                self.scorestring ="Cookies: %s" % self.Score
                self.score.clear()
                self.score.write(self.scorestring, font=("Arial",24, "normal"))
                self.ClickPowerLabel.clear()
                self.ClickPowerLabel.write("Click Power level:" +format(self.ClickPover))
                self.BonusOnClickPriceTagLv1.clear()
                self.BonusOnClickPriceTagLv1.write("Price:" + format(self.BonusOnClickPriceLv1))

                self.PasivePowerLabel.clear()
                self.PasivePowerLabel.write("Passive Income:" +format(self.passiveGrowth))
                self.pasivePriceTag.clear()
                self.pasivePriceTag.write("Price:" + format(self.passiveGrowthPrice))
        if self.passiveGrowth==1:
            self.update_score()


    def saveData(self):
        with open('saved.json','w')as f:
            data={"Score":self.Score,
                  "BonusOnClickPriceLv1":self.BonusOnClickPriceLv1,
                  "ClickPover":self.ClickPover,
                    "PowLv1":self.PowLv1,
                    "MaxPowerLv1":self.MaxPowerLv1,
                    "BonusOnClickGrowLv1":self.BonusOnClickGrowLv1,
                    "passiveGrowth":self.passiveGrowth,
                    "passiveGrowthPrice":self.passiveGrowthPrice,
                    "passiveGrowthGrow":self.passiveGrowthGrow,
                    "passiveGrowthMaxLv1":self.passiveGrowthMaxLv1
            }
            json.dump(data,f)

    def loadData(self):
        with open('saved.json') as f:
            data = json.load(f)
            self.Score = data["Score"]
            self.BonusOnClickPriceLv1 = data["BonusOnClickPriceLv1"]
            self.ClickPover = data["ClickPover"]
            self.PowLv1 = data["PowLv1"]
            self.MaxPowerLv1 = data["MaxPowerLv1"]
            self.BonusOnClickGrowLv1 = data["BonusOnClickGrowLv1"]
            self.passiveGrowth = data["passiveGrowth"]
            self.passiveGrowthPrice = data["passiveGrowthPrice"]
            self.passiveGrowthGrow = data["passiveGrowthGrow"]
            self.passiveGrowthMaxLv1 = data["passiveGrowthMaxLv1"]
        if self.passiveGrowth>0:
            self.update_score()
        self.scorestring ="Cookies: %s" % self.Score
        self.score.clear()
        self.score.write(self.scorestring, font=("Arial",24, "normal"))
        self.ClickPowerLabel.clear()
        self.ClickPowerLabel.write("Click Power level:" +format(self.ClickPover))
        self.BonusOnClickPriceTagLv1.clear()
        self.BonusOnClickPriceTagLv1.write("Price:" + format(self.BonusOnClickPriceLv1))
        self.PasivePowerLabel.clear()
        self.PasivePowerLabel.write("Passive Income:" +format(self.passiveGrowth))
        self.pasivePriceTag.clear()
        self.pasivePriceTag.write("Price:" + format(self.passiveGrowthPrice))


