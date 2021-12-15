import pygame as pg
from Engine import *
from Obstacles import *
from Player import *
from Terrain import *
from UI import *
from AI import *


WIDTH, HEIGHT = 800, 600
FPS = 60

BG = (45,64,89)
BLACK = (0, 0, 0)
WHITE = (255,250,250)
TEAL = (0, 128, 128)


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.enemies = []
        self.enemies_to_die = []
        self.bullets = []
        self.bullets_to_die = []
        self.coins = []
        self.coins_to_die = []
        self.UI = UI(self.screen)

        self.score = 0

        self.control_vars = {'in_menu': True, 'in_game': False, 'in_pause': False, 'end_game': False}
        #self.create_menu()

        self.lift = HEIGHT
        self.flag = False

        self.Engine = Engine(WIDTH, HEIGHT, -30)
        self.Player = Player(self.screen, pg.Vector3(WIDTH/2, self.lift, 0), 'Player_model.txt', pg.Vector3(), pg.Vector3(0, 0, 0), 20)
        self.Terrain = Terrain(self.screen, WIDTH, 550, 20, 12, HEIGHT+20, (34, 139, 34), 1)
        self.AI = AI(self.screen, self.lift, 1300)

    def run(self):
        while True:
            self.create_menu()

            while self.control_vars.get('in_menu'):
                self.clock.tick(FPS)
                self.screen.fill(BG)
                pg.display.set_caption(str(int(self.clock.get_fps())))

                self.control_vars = self.UI.update(self.control_vars)
                self.UI.draw()
                
                ''' Эта фигня работает '''
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE]:
                    exit()

                pg.display.flip()

            self.create_gameUI()

            while self.control_vars.get('in_game'):
                self.clock.tick(FPS)
                self.screen.fill(BG)
                pg.display.set_caption(str(int(self.clock.get_fps())))

                for en in self.enemies_to_die:
                    self.enemies.remove(en)
                self.enemies_to_die = []

                for b in self.bullets_to_die:
                    self.bullets.remove(b)
                self.bullets_to_die = []

                for c in self.coins_to_die:
                    self.coins.remove(c)
                self.coins_to_die = []
                
                ''' ---------------------------------------------------- '''

                self.Terrain.update()
                self.Engine.orthogonal_projection_edge(self.Terrain)
                self.Terrain.draw()

                ''' ---------------------------------------------------- '''

                self.AI.update()
                if self.AI.time_to_spawn_enemy:
                    for en in self.AI.spawn_enemies():
                        self.enemies.append(en)
                if self.AI.time_to_spawn_coin:
                    for c in self.AI.spawn_coins():
                        self.coins.append(c)

                for en in self.enemies:
                    en.update()
                    if en.collide_bullet(self.bullets):
                        self.score += 2
                    if en.time_to_die:
                        self.enemies_to_die.append(en)

                    self.Engine.orthogonal_projection_edge(en)
                    self.Engine.orthogonal_projection(en)
                    en.draw()

                ''' ---------------------------------------------------- '''

                for c in self.coins:
                    c.update()
                    if c.time_to_die:
                        self.coins_to_die.append(c)

                    c.rotate('y', 5)
                    self.Engine.orthogonal_projection_edge(c)
                    self.Engine.orthogonal_projection(c)
                    c.draw()
                
                ''' ---------------------------------------------------- '''

                for b in self.bullets:
                    b.update()
                    if b.time_to_die:
                        self.bullets_to_die.append(b)

                    self.Engine.orthogonal_projection_edge(b)
                    self.Engine.orthogonal_projection(b)
                    b.draw()

                
                self.Player.update()
                if self.Player.collide_сoin(self.coins):
                    self.score += 2.5
                if self.Player.collide_enemy(self.enemies):
                    self.control_vars = {'in_menu': False, 'in_game': False, 'in_pause': False, 'end_game': True}
                if self.Player.time_to_shoot:
                    self.bullets.append(self.Player.shoot())
                self.Engine.orthogonal_projection_edge(self.Player)
                self.Engine.orthogonal_projection(self.Player)
                self.Player.draw()

                self.control_vars = self.UI.update(self.control_vars)
                self.UI.UI_elements[0].update_phrase('Счёт:' + str(int(self.score))) # Поправить потом!
                self.UI.draw()

                if pg.event.get() != []:
                    print(pg.event.get())
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_LEFT:
                            print('lol')

                ''' Эта фигня работает '''
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE]:
                    exit()
                elif keys[pg.K_p]:
                    self.control_vars = {'in_menu': False, 'in_game': True, 'in_pause': True, 'end_game': False}
                    self.flag = True

                if self.control_vars.get('in_pause'):
                    s = pg.Surface((WIDTH, HEIGHT))
                    s.set_alpha(100)
                    s.fill((0, 0, 0))
                    self.screen.blit(s, (0,0))

                pg.display.flip()
                '''
                while self.control_vars.get('in_pause'):
                    self.clock.tick(FPS)
                    pg.display.set_caption(str(int(self.clock.get_fps())))

                    keys = pg.key.get_pressed()
                    if keys[pg.K_ESCAPE]:
                        exit()
                    elif keys[pg.K_o]:
                        print('lol')
                        self.control_vars = {'in_menu': False, 'in_game': True, 'in_pause': False}
                    
                    pg.display.flip()
                '''
            
            self.create_end_gameUI()

            while self.control_vars.get('end_game'):
                self.restore_game()
                self.clock.tick(FPS)
                self.screen.fill(BG)
                pg.display.set_caption(str(int(self.clock.get_fps())))

                self.control_vars = self.UI.update(self.control_vars)
                self.UI.draw()

                ''' Эта фигня работает '''
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE]:
                    exit()

                pg.display.flip()


    
    def create_menu(self):
        self.UI.restore()
        self.UI.add_text(self.screen, WHITE, pg.Vector2(WIDTH/2, 200), 70, "SpaceGame")
        self.UI.add_button(self.screen, TEAL, WHITE, pg.Vector2(WIDTH/2-100, 400), 200, 40, 30, "Начать", 'play')

    def create_gameUI(self):
        self.UI.restore()
        self.UI.add_text(self.screen, WHITE, pg.Vector2(38, 18), 30, 'Счёт: ' + str(self.score))

    def create_end_gameUI(self):
        self.UI.restore()
        self.UI.add_text(self.screen, WHITE, pg.Vector2(WIDTH/2, HEIGHT/2-100), 70, "Вы проиграли:(")
        self.UI.add_text(self.screen, WHITE, pg.Vector2(WIDTH/2, HEIGHT/2), 40, 'Ваш счёт: ' + str(int(self.score)))
        self.UI.add_button(self.screen, TEAL, WHITE, pg.Vector2(WIDTH/2-100, HEIGHT/2+100), 200, 40, 30, "Перезапустить", 'play')

    def restore_game(self):
        self.enemies = []
        self.enemies_to_die = []
        self.bullets = []
        self.bullets_to_die = []
        self.coins = []
        self.coins_to_die = []
        self.score = 0
        self.Player.pos_center = pg.Vector3(WIDTH/2, self.lift, 0)

if __name__ == '__main__':
    app = App()
    app.run()
                