class partyAnimal:
    x=0
    def party(self):
        self.x=self.x+ 1
        print('New number',self.x)
an=partyAnimal()
print("Type",type(an))
print("Dir",dir(an))