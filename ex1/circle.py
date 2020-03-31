from math import pi

class circle(object):
    def __init__(self,radius):
        self.radius = radius
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
    
    def compute_area(self):
        area = pi * self.radius * self.radius
        return area

    
    def compute_perimeter(self):
        perimeter = 2 * pi * self.radius
        return perimeter

    def __repr__(self):
        return "Radius : {}\nArea : {}\nPerimeter : {}".format(self.radius,self.area,self.perimeter)



    

