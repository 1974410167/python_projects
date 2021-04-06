import turtle
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
def drawpole_3():#画出汉诺塔的底座
    t = turtle.Turtle()
    t.hideturtle()
    def drawpole_1(k):
        t.up()
        t.pensize(5)
        t.speed(75)
        t.goto(200*(k-1), 100)
        t.down()
        t.color('blue')
        t.goto(200*(k-1), -100)
        t.goto(200*(k-1)-20, -100)
        t.goto(200*(k-1)+20, -100)
    drawpole_1(0)#画出汉诺塔的A
    drawpole_1(1)#画出汉诺塔的B
    drawpole_1(2)#画出汉诺塔的C
def creat_plates(n):#制造n个盘
    plates=[turtle.Turtle() for i in range(n)]
    for i in range(n):
        plates[i].up()
        plates[i].color('green')
        plates[i].hideturtle()
        plates[i].shape("square")
        plates[i].shapesize(1,9-i)
        plates[i].goto(-200,-90+20*i)
        plates[i].showturtle()
    return plates
def pole_stack():#制造底的栈
    poles=[Stack() for i in range(3)]
    return poles
def moveDisk(plates,poles,fp,tp):
    mov=poles[fp].peek()
    plates[mov].goto((fp-1)*200,150)
    plates[mov].goto((tp-1)*200,150)
    l=poles[tp].size()
    plates[mov].goto((tp-1)*200,-90+20*l)
def moveTower(plates,poles,height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(plates,poles,height-1,fromPole,withPole,toPole)
        moveDisk(plates,poles,fromPole,toPole)
        poles[toPole].push(poles[fromPole].pop())
        moveTower(plates,poles,height-1,withPole,toPole,fromPole)
myscreen=turtle.Screen()
drawpole_3()
n=eval(input(""))
plates=creat_plates(n)
poles=pole_stack()
for i in range(n):
    poles[0].push(i)
moveTower(plates,poles,n,0,2,1)
myscreen.exitonclick()