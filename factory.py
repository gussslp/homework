class Toys:
    def __init__(self,name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def show(self):
        print(self.name,self.color,self.type)

class Animals(Toys):
    def __init__(self,name, color, type):
        Toys.__init__(self,name, color, type)
class Disney(Toys):
    def __init__(self,name, color, type):
        Toys.__init__(self,name, color, type)

def create():
    print("buy faux fur, fabric and printed material, material stitching, paint material")

toyss = [
Animals("paddington","brown","animal"),
Disney("Mickey mouse", "black","Disney")
]
for toy in toyss:
    create()
    toy.show()