import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    
    def showdisk(self):
        t.seth(0)
        t.fd(self.dwidth/2)
        t.lt(90)
        t.fd(self.dheight)
        t.lt(90)
        t.fd(self.dwidth)
        t.lt(90)
        t.fd(self.dheight)
        t.lt(90)
        t.fd(self.dwidth/2)
        t.seth(0)

        t.pu()
        t.goto(self.dxpos, self.dypos)
        t.pd()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

        t.pu()
        t.goto(self.dxpos, self.dypos)
        t.pd()

    def cleardisk(self):
        t.seth(0)
        t.clear()
        t.seth(0)

d = Disk()
d.showdisk()
d.cleardisk()

t.done()