from tabulate import tabulate
import numpy


class main():
    def __init__(self):
        self.height = None
        self.basearea = None
        self.circumference = None
        self.diameter = None
        self.radius = None
        self.volume = None
        self.getdata()
        self.transtofloat()
        self.comput()
        self.showdata()
    def getdata(self):
        self.volume = input("Volume:")
        self.radius = input("Radius:")
        if not self.radius:
            self.diameter = input("Diameter:")
            if not self.diameter:
                self.circumference = input("Circumference:")
                if not self.circumference:
                    self.basearea = input("Area of base:")
        self.height = input("height:")
    def transtofloat(self):
        try:
            if self.volume:
                self.volume = float(self.volume)

        except:
            print("Unable to turn volume into a float")
        try:
            if self.radius:
                self.radius = float(self.radius)
        except:
            print("Unable to turn radius into a float")
        try:
            if self.diameter:
                self.diameter = float(self.diameter)
        except:
            print("Unable to turn diameter into a float")
        try:
            if self.circumference:
                self.circumference = float(self.circumference)
        except:
            print("Unable to turn circumference into a float")
        try:
            if self.basearea:
                self.basearea = float(self.basearea)
        except:
            print("Unable to turn base area into a float")
        try:
            if self.height:
                self.height = float(self.height)
        except:
            print("Unable to turn base area into a float")
    def comput(self):
        if self.radius:
            if not self.volume:
                if not self.diameter:
                    self.diameter = round(self.radius* 2, 3)
                if not self.circumference:
                    self.circumference = round(2* self.radius * numpy.pi, 3)
                if not self.basearea:
                    self.basearea = round(numpy.pi * self.radius * self.radius, 3)
                if not self.volume:
                    self.volume = round(self.basearea * self.height, 3)
            if self.volume:
                if not self.diameter:
                    self.diameter = round(self.radius * 2, 3)
                if not self.circumference:
                    self.circumference = round(2 * self.radius * numpy.pi, 3)
                if not self.basearea:
                    self.basearea = round(numpy.pi * self.radius * self.radius, 3)
                if not self.height:
                    self.height = round(self.volume /self.basearea, 3 )
        if self.diameter:
            if not self.volume:
                if not self.radius:
                    self.radius = float(self.diameter / 2)
                if not self.circumference:
                    self.circumference = round(2* self.radius * numpy.pi, 3)
                if not self.basearea:
                    self.basearea = round(numpy.pi * self.radius * self.radius, 3)
                if not self.volume:
                    self.volume = round(self.basearea * self.height)

    def showdata(self):
        data = [["Volume:", self.volume], ["Base Area:", self.basearea], ["Circumference:", self.circumference], ["Radius:", self.radius], ["Diameter:", self.diameter], ["Height:", self.height]]
        print(tabulate(data, tablefmt='fancy_grid'))


main()
