class grandfather():

    def __init__(self,name):
        self.name=name

    def skill_fight(self):
        print(f"{self.name} can fight")

class Father(grandfather):
    def skills_drive(self):
        print(f" {self.name}Driving")

class Mother:
    def skills_cok(self):
        print(f"{self.name}Cooking")

class Child(Father, Mother):
    pass

class daughter(Mother):
    pass

child=Child("NEMO")
child.skills_cok()
        

        