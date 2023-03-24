# 訓練營
from .Adventurer import Archer, Warrior

class AbsInterfaceCamps:
    def __init__(self, classname=None):
        self.career = classname
    def training(self):
        self.career().training()

create_an_archer = AbsInterfaceCamps()
create_an_archer.career = Archer
create_an_archer.training() 