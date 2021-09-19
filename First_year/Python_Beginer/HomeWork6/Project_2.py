class Road:
    _length = 0
    _width = 0

    def __init__(self, length_meter, width_meter):
        self._length = length_meter
        self._width = width_meter

    def define_mass(self, thickness_centimeters):
        return self._length * self._width * 25 * thickness_centimeters

road = Road(5000, 20)
print(f'{road.define_mass(5):,d}')