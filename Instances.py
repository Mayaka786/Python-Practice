class partyAnimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print(self.name,"constructed")
    def party(self):
        self.x=self.x +1
        print(self.name,"party count",self.x)
s=partyAnimal("Gabriel")
s.party()
j=partyAnimal("Vee")
j.party()
s.party()