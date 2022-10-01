class Factory:
    def __init__(self,name, color, movie):
        self.name = name
        self.color = color
        self.movie = movie
    
    def buy_material(self):
        print("buy faux fur, fabric and printed material")

    def stitching(self):
        print("material stitching")
    
    def paint(self):
        print("paint material")

Factory = Factory("bear","brown","paddington bear")

Factory.paint()