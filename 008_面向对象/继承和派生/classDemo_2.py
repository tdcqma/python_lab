class Hero:

    def __init__(self,nickname,aggressivity,life_value):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value

    def move_forward(self):
        print('%s move forward ' % self.nickname)

    def move_backward(self):
        print('%s move backward ' % self.nickname)

    def move_left(self):
        print('%s move left' % self.nickname)

    def move_right(self):
        print('%s move right' % self.nickname)

    def attack(self,enemy):
        enemy.life_value -= self.aggressivity

class Garen(Hero):
    pass

class Riven(Hero):
    pass
