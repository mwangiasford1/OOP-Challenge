class Pet:
    def __init__(self, name):
        self.name = "billy"
        self.hunger = 10
        self.energy = 10
        self.happiness = 10
        self.tricks = ["rollover", "fetch", "sit", "stand", "shake"]
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 10)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        energy_status = "full" if self.energy > 5 else "tired"
        print(f"{self.name}'s Status: Hunger: {self.hunger}, Energy: {self.energy} ({energy_status}), Happiness: {self.happiness}")    

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!") 

    def show_tricks(self):
        print(f"{self.name}'s learned tricks: {', '.join(self.tricks) if self.tricks else 'No tricks yet!'}")

# Example usage
my_pet = Pet("billy")
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.train("Roll over")
my_pet.show_tricks()
my_pet.get_status()
