class Stationery(object):
    title = ''

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):

    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        super().draw()
        print(f'Title: {self.title}')

class Pencil(Stationery):

    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        super().draw()
        print(f'Title: {self.title}')

class Handle(Stationery):
    
    def __init__(self):
        self.title = 'Handle'
    
    def draw(self):
        super().draw()
        print(f'Title: {self.title}')

Pen().draw()
print('---------------------')
Pencil().draw()
print('---------------------')
Handle().draw()