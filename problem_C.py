class Starship ():
    def __init__(self, name, crew_list):
        self.name = name
        self.crew_list = crew_list
        self.damaged = {
            'Bridge': False,
            'Medbay': False,
            'Engine': False,
            'Lasers': False,
            'Sleep pods': False
        }
class Crew:
    def __init__(self, name):
        self.name = name
        self.status = "Active"
        self.location = "Sleep Pods"
    def move(self, location):
        if location not in ['Bridge', 'Medbay', 'Engine', 'Lasers', 'Sleep pods']:
            print("Not a valid location")
        else: 
            self.location = location
    def repair(self, ship):
        self.ship = ship
        print(f'{self.name} does not know how to do that')
    def first_aid(self, ship):
        self.ship = ship
        print(f'{self.name} does not know how to do that')
    def fire_lasers(self, ship,target_ship, target_location):
         self.ship = ship
        self.target_ship = target_ship
        self.target_location = target_location
        print(f'{self.name} does not know how to do that')
    def __repr__(self):
        return f'{self.name}: {self.status}, at {self.location}'
crew1 = Crew("Sakshi")
crew2 = Crew("Jina")
crew3 = Crew("Daniel")
space_boat = Starship('Ebon Hawk', [crew1, crew2, crew3])
if __name__ == '__main__':
    print(space_boat.name)
    print(space_boat.crew_list)
    print(space_boat.damaged)
    crew1.move('Dungeon')
    print(crew1.location)
    crew1.move('Engine')
    print(crew1.location)
    crew2.repair(space_boat)
    crew3.first_aid(space_boat)
    crew2.fire_lasers(space_boat, space_boat, "Engine")
