class partyAnimal:
    x=0
    def __init__(self):
        print("I am constructed")
        
    def party(self):
        self.x=self.x+ 1
        print('so far',self.x)
    def __del__(self):
        print('I am destructed',self.x)
an=partyAnimal()
an.party()
an.party()