import turtle as t
from disk import Disk

class Pole(object):
    def __init__(self, name="", xpos = 0, ypos = 0, thick = 10, length = 100) :
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        t.fd(self.pthick / 2)
        t.lt(90)
        t.fd(self.plength)
        t.lt(90)
        t.fd(self.pthick)
        t.lt(90)
        t.fd(self.plength)
        t.lt(90)
        t.fd(self.pthick / 2)
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.done()

    def pushdisk(self, disk):
        self.stack.append(disk)

    def popdisk(self):
        d = self.stack.pop()
        d.dxpos = self.toppos 
        d.dypos = self.toppos
        return d
    
def main():
    t.speed(50)

    pole2 = Pole("Pole 2", 0, -50)

    pole2.showpole()


if __name__ == "__main__":
    main()