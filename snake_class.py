class Snake(object):
    body = []

    def __init__(self, color, pos):
        self.color = color
        self.head = pos
        self.body.append(self.head)

    def sound(self):
        print("hissss")

    def draw(self, surface):
        # for i,c in enumerate(self.body):
        #     if i == 0:
