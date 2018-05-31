class People:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)

egon = People('egon',1.80,75)
egon.height = 1.82
print(egon.bmi)