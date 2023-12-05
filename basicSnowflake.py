import turtle
import random


turtle.bgcolor("black")


t = turtle.Turtle()

t.speed("fastest")
t.hideturtle()
t.pencolor("white")

def subBranchLength():
    arrSubBranchLength = []
    for x in range (6):
        
        arrSubBranchLength.append(random.randrange(15,100))
    return arrSubBranchLength

def createHashValue(text:str):
    hash=0
    for ch in text:
        hash = ( hash*281  ^ ord(ch)*997) & 0xFFFFFFFF
    return hash

def createSubBranchs():
    arrSubBranchLength = []

    hash = createHashValue("Josh")
    digits = [int(x) for x in str(hash)]
    print(digits)

    for number in digits:
        
        arrSubBranchLength.append(number*20)
    
    return arrSubBranchLength

def drawName():
    name = "Josh"
    t.penup()
    t.goto(0,250)
    t.pendown()
    style = ('Helvetica Neue', 30)
    t.write(name,align='center',font=style)

    turtle.done()

def drawingSnowflake():
    arrLength = createSubBranchs()
    # arrLength = subBranchLength()
    for mainBranch in range(6):
        

        for subBranch in range (6):
            t.forward(20)
            t.left(45)
            t.forward(arrLength[subBranch])
            t.back(arrLength[subBranch])
            t.right(90)
            t.forward(arrLength[subBranch])
            t.back(arrLength[subBranch])
            t.left(45)
        
        t.forward(30)
        t.back(150)
        t.right(60)


    



drawingSnowflake()
drawName()