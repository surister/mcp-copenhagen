
class MountainGroup:
    def __init__(self, country: str):
        self.country = country
        self.mountains = []

    def mountain(self, f, *args, **kwargs):
        print(f)
        f = f(*args, **kwargs)
        self.mountains.append(f)

    def __repr__(self):
        return f'{self.__class__.__name__}(mountains={self.mountains})'

mg = MountainGroup('spain')

@mg.mountain
def mulhacen():
    return {'name': 'mulhacen', 'height': 3479}

print(mg)