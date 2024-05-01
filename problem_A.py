class Crew:
    def __init__(self, name):
        self.name = name
        self.status = "Active"
        self.location = "Sleep Pods"
    def __repr__(self):
        return f'{self.name}: {self.status}, at {self.location}'
crew0 = Crew("Ava")

if __name__ == '__main__':
    print(crew0.name)
    print(crew0.status)
    print(crew0.location)
    print(crew0)
