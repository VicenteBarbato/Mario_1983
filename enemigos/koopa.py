import pyxel
from enemigos.enemigos import Enemigos


class Koopa(Enemigos):

    def __init__(self, x: int, y: int, w: int, h: int, dir: str) -> None:
        super().__init__(x, y, w, h, dir)

    def draw(self):
        if not self.stop_moving:
            if self.count_molest == 0:
                self.draw_0()
            elif self.count_molest == 1:
                self.draw_1()
            elif self.count_molest == 2:
                self.draw_2()

        elif self.stop_moving:
            if self.count_molest == 0:
                self.draw_s_0()
            elif self.count_molest == 1:
                self.draw_s_1()
            elif self.count_molest == 2:
                self.draw_s_2()

    def draw_0(self):
        if self.dir == "left":
            pyxel.blt(self.x, self.y, 0, 191, 0, 16, 15)
        elif self.dir == "right":
            pyxel.blt(self.x, self.y, 0, 5, 0, 16, 15)

    def draw_1(self):
        if self.dir == "left":
            pyxel.blt(self.x, self.y, 0, 192, 24, 16, 15)
        elif self.dir == "right":
            pyxel.blt(self.x, self.y, 0, 5, 24, 16, 15)

    def draw_2(self):
        if self.dir == "left":
            pyxel.blt(self.x, self.y, 0, 191, 42, 16, 15)
        elif self.dir == "right":
            pyxel.blt(self.x, self.y, 0, 5, 42, 16, 15)

    def draw_s_0(self):
        pyxel.blt(self.x, self.y + 7, 1, 2, 155, 10, 9)

    def draw_s_1(self):
        pyxel.blt(self.x, self.y + 7, 1, 2, 178, 10, 9)

    def draw_s_2(self):
        pyxel.blt(self.x, self.y + 7, 1, 2, 197, 10, 9)

    def volteado(self):
        if self.num_veces_golpeado == 3 or self.golpear_all == True:
            self.stop_moving = True
            self.count_back_to_live += 1
        if self.num_veces_golpeado > 3 or self.count_back_to_live == 130:
            self.stop_moving = False
            self.golpear_all = False
            self.num_veces_golpeado = 0
            self.count_back_to_live = 0
            if self.count_molest < 2:
                self.speed += 0.5
                self.count_molest += 1

    def muerte_enemigo(self, mario, lista_enemigos):
        if ((self.x >= mario.x and self.x <= mario.x + 16) and (mario.y <= self.y + 24 or self.y >= mario.y + 22) \
                and mario.nivel == self.nivel - 1 and not self.suma) or (self.golpear_all == True \
                and (self.x >= mario.x and self.x <= mario.x + 16) and (mario.y <= self.y + 24 or self.y >= mario.y + 22) \
                and mario.nivel == self.nivel - 1 and not self.suma):
            self.num_veces_golpeado += 3
            mario.puntuacion += 10
            self.suma = True
        if (mario.x + 16 >= self.x and mario.x <= self.x + 16) and mario.nivel == self.nivel and self.stop_moving:
            mario.puntuacion += 800
            self.suma = True
            lista_enemigos.remove(self)



