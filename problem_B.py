class Starship:
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
    def __repr__(self):
        return f'{self.name}: {self.status}, at {self.location}'
crew1 = Crew("Sakshi")
crew2 = Crew("Jina")
crew2 = Crew("Daniel")
spaceship = Starship('Ebon Hawk', [crew1, crew2, crew3])
if __name__ == '__main__':
    print(spaceship.name)
    print(spaceship.crew_list)
    print(spaceship.damaged)
