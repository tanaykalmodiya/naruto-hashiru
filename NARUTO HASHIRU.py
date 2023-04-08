import pygame
from sys import exit
from random import randint

WIDTH=800
HEIGHT=500
FPS=60
BROWN=(51,25,0)
BG_POSITION=(0,0)

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()

        self.GRAVITY=0

        self.check_shift=False
        self.check_index=0

        self.naruto_still_list=[]
        self.naruto_still_steps=6
        self.naruto_still_index=0

        self.naruto_jump_list=[]
        self.naruto_jump_steps=3
        self.naruto_jump_index=0

        self.naruto_shift_list=[]
        self.naruto_shift_steps=3
        self.naruto_shift_index=0

        self.load_sprite()
        self.image=self.naruto_still_list[0]
        self.rect=self.image.get_rect(topleft=(12,185))

        self.jump_music=pygame.mixer.Sound("graphics/jump.mp3")
        self.jump_music.set_volume(0.25)

    def input(self):

        self.keys=pygame.key.get_pressed()

        if self.keys[pygame.K_SPACE] and self.rect.bottom>=435:
            self.jump_music.play()
            self.GRAVITY=-20

        if self.keys[pygame.K_RSHIFT] and self.rect.bottom>=435:
            self.check_shift=True

    def gravity(self):

        self.GRAVITY+=1
        self.rect.bottom+=self.GRAVITY

        if self.rect.bottom>=435:
            self.rect.bottom=435

    def jump(self,x):

        self.sprite_njump=pygame.image.load("graphics/narutojump.png").convert_alpha()
        self.naruto2=pygame.Surface((56,80))
        self.naruto2.blit(self.sprite_njump,(0,0),(((x*56)-3),0,56,80))
        self.NARUTO2=pygame.transform.scale(self.naruto2,(170,250))
        self.NARUTO2.set_colorkey((0,0,0))

        return self.NARUTO2

    def attack(self,x):

        self.sprite_nattack=pygame.image.load("graphics/nrasengan.png").convert_alpha()
        self.naruto3=pygame.Surface((70,61))
        self.naruto3.blit(self.sprite_nattack,(0,0),(((x*70)-8),0,70,61))
        self.NARUTO3=pygame.transform.scale(self.naruto3,(170,240))
        self.NARUTO3.set_colorkey((0,0,0))

        return self.NARUTO3

    def naruto7(self,x):

        self.sprite_nstill=pygame.image.load("graphics/nb.png").convert_alpha()
        self.naruto1=pygame.Surface((45,79))
        self.naruto1.blit(self.sprite_nstill,(0,0),(((x*44)+2),0,45,79))
        self.NARUTO1=pygame.transform.scale(self.naruto1,(150,250))
        self.NARUTO1.set_colorkey((0,0,0))
        
        return self.NARUTO1

    def load_sprite(self):

        for x in range(self.naruto_still_steps):
            self.naruto_still_list.append(self.naruto7(x))

        for x in range(self.naruto_jump_steps):
            self.naruto_jump_list.append(self.jump(x))

        for x in range(self.naruto_shift_steps):
            self.naruto_shift_list.append(self.attack(x))

    def naruto_animation(self):

        if self.rect.bottom<435:

            self.naruto_jump_index+=0.09

            if self.naruto_jump_index>len(self.naruto_jump_list):
                self.naruto_jump_index=0
            self.image=self.naruto_jump_list[int(self.naruto_jump_index)]

        else:

            self.naruto_still_index+=0.09

            if self.naruto_still_index>len(self.naruto_still_list):
                self.naruto_still_index=0

            self.image=self.naruto_still_list[int(self.naruto_still_index)]

        if self.check_shift and self.rect.bottom==435:

            self.naruto_shift_index+=0.1

            if self.naruto_shift_index>len(self.naruto_shift_list):
                self.naruto_shift_index=0

            self.image=self.naruto_shift_list[int(self.naruto_shift_index)]
            self.check_index+=0.3

            if self.check_index>=10:
                self.check_shift=False
                self.check_index=0

    def update(self):

        self.input()
        self.gravity()
        self.naruto_animation()

class Rasengan(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.RASENGAN=pygame.image.load("graphics/rasengan.png").convert_alpha()
        self.rasengan=pygame.transform.scale(self.RASENGAN,(60,70))
        self.rasengan.set_colorkey((0,0,0))

        self.check_shift=False
        self.check_index=0
        self.rasen_x=140


        if self.rasen_x>200:
            self.rasen_x=-500

        self.image=self.rasengan
        self.rect=self.image.get_rect(topleft=(self.rasen_x,240))

    def obstacle_movement(self):

        self.rect.left+=15

    def input(self):

        self.keys=pygame.key.get_pressed()

        if self.keys[pygame.K_RSHIFT]:
            self.check_shift=True

    def animation(self):

        if self.check_shift:

            self.image=self.rasengan
            self.check_index+=0.3

            if self.check_index>=10:
                self.check_shift=False
                self.check_index=0

    def update(self):

        self.input()
        self.animation()
        self.obstacle_movement()


class Obstacle(pygame.sprite.Sprite):

    def __init__(self,type):

        super().__init__()

        self.enemy_list=[]
        self.enemy_steps=3
        self.enemy_index=0
        self.type=type

        if type==0 or type ==2:

            self.ROCK=pygame.image.load("graphics/rock.png").convert_alpha()
            self.rock=pygame.transform.scale(self.ROCK,(125,80))
            self.rock.set_colorkey((0,0,0))
            self.obstacle_y=357
            self.frames=self.rock

        else:

            self.load_sprite()
            self.enemy=self.enemy_list[0]
            self.frames=self.enemy
            self.obstacle_y=180

        self.image=self.frames
        self.rect=self.image.get_rect(topleft=(randint(900,1500),self.obstacle_y))

    def enemy7(self,x):

        self.sprite_enemy=pygame.image.load("graphics/enemy.png").convert_alpha()
        self.enemy1=pygame.transform.scale(self.sprite_enemy,(700,260))
        self.ENEMY1=pygame.Surface((240,260))
        self.ENEMY1.blit(self.enemy1,(0,0),((x*225)+15,0,240,260))
        self.ENEMY1.set_colorkey((0,0,0))

        return self.ENEMY1 

    def load_sprite(self):

        for x in range(self.enemy_steps):
            self.enemy_list.append(self.enemy7(x))

    def enemy_animation(self):

        if self.type==1:
            self.enemy_index+=0.1
            if self.enemy_index>len(self.enemy_list):
                self.enemy_index=0

            self.image=self.enemy_list[int(self.enemy_index)]
    
    def obstacle_movement(self):

        if self.type==0 or self.type ==2:
            self.rect.left-=14
        else:
            self.rect.left-=17

    def destroy(self):

        if self.rect.left<-15:
            self.kill()

    def update(self):

        self.enemy_animation()
        self.obstacle_movement()
        self.destroy()

class Game():

    def __init__ (self):

        pygame.init()

        self.DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("NARUTO HASHIRU")

        self.FONT= pygame.font.Font(None,25)

        self.ICON=pygame.image.load('graphics/n2.png').convert_alpha()
        pygame.display.set_icon(self.ICON)

        self.CLOCK=pygame.time.Clock()

        self.BG=pygame.image.load("graphics/bg1.jpg").convert_alpha()

        self.rasen=pygame.sprite.GroupSingle()
        self.rasen.add((Rasengan()))

        self.player=pygame.sprite.GroupSingle()
        self.player.add((Player()))

        self.obstacle=pygame.sprite.Group()

        self.TREE=pygame.image.load("graphics/tree.png").convert_alpha()
        self.tree=pygame.transform.scale(self.TREE,(400,500))

        self.H1=pygame.image.load("graphics/h1.png").convert_alpha()
        self.h1=pygame.transform.scale(self.H1,(160,60))
        self.h1.set_colorkey((0,0,0))

        self.H2=pygame.image.load("graphics/h2.png").convert_alpha()
        self.h2=pygame.transform.scale(self.H2,(160,65))
        self.h2.set_colorkey((0,0,0))

        self.H3=pygame.image.load("graphics/h3.png").convert_alpha()
        self.h3=pygame.transform.scale(self.H3,(160,65))
        self.h3.set_colorkey((0,0,0))

        self.CLOUD=pygame.image.load("graphics/cloud.png").convert_alpha()
        self.cloud=pygame.transform.scale(self.CLOUD,(130,130))
        self.cloudx1=600
        self.cloudx2=650
        self.cloudx3=2
        self.cloudx4=80
        self.cloudx5=300
        self.bird5=400

        self.DEATH_COUNT=0

        self.check_menu=0

        self.check_attack=False

        self.OBSTACLE_RECT_LIST=[]
        self.obstacle_timer=pygame.USEREVENT+1
        pygame.time.set_timer(self.obstacle_timer,900)

        self.enemy_animation_timer=pygame.USEREVENT+2
        pygame.time.set_timer(self.enemy_animation_timer,800)

        self.bird_list=[]
        self.bird_steps=3
        self.bird_index=0

        self.load_sprite()

        self.bird=self.bird_list[0]
        self.bird_rect=self.bird.get_rect(topleft=(-100,30))

        self.bg_music=pygame.mixer.Sound("graphics/bgm.mp3")
        self.bg_music.set_volume(0.15)
        self.bg_music.play(loops=-1)

        self.end_music=pygame.mixer.Sound("graphics/end.mp3")
        self.end_music.set_volume(0.5)

        self.hit_music=pygame.mixer.Sound("graphics/hit.mp3")
        self.hit_music.set_volume(0.5)

    def bird7(self,x):

        self.sprite_bird=pygame.image.load("graphics/bird.png").convert_alpha()
        self.bird1=pygame.Surface((90,79))
        self.bird1.blit(self.sprite_bird,(0,0),(((x*90)),0,90,79))
        self.BIRD1=pygame.transform.scale(self.bird1,(150,130))
        self.BIRD1.set_colorkey((0,0,0))

        return self.BIRD1
        
    def load_sprite(self):

        for x in range(self.bird_steps):
            self.bird_list.append(self.bird7(x))

    def bird_animation(self):

        self.bird_index+=0.06
        if self.bird_index>len(self.bird_list):
                self.bird_index=0
        self.bird=self.bird_list[int(self.bird_index)]

    def basic_menu(self):

        self.DISPLAY.fill((BROWN))
        self.DISPLAY.blit(self.BG,BG_POSITION)
        self.DISPLAY.blit(self.tree,(500,-50))
        self.backgroung()
        self.DISPLAY.blit(self.icon,(300,15))

        self.player.draw(self.DISPLAY)
        self.player.update()

        self.DISPLAY.blit(self.CREDIT,(570,470))

    def menu(self):

        self.OBSTACLE_RECT_LIST.clear()
        self.NLOGO=pygame.image.load("graphics/nlogo.png").convert_alpha()
        self.nlogo=pygame.transform.scale(self.NLOGO,(310,140))
        self.nlogo.set_colorkey((0,0,0))
        self.icon=pygame.transform.scale(self.ICON,(135,135))
        self.icon.set_colorkey((0,0,0))
        self.CREDIT= self.FONT.render("Made By-Tanay Kalmodiya",True,(255,255,255))
        self.GG=pygame.image.load("graphics/gg.png").convert_alpha()
        self.gg=pygame.transform.scale(self.GG,(310,300))
        self.gg.set_colorkey((0,0,0))

        while True:

            self.CLOCK.tick(FPS)

            if self.check_menu==0:

                self.basic_menu()
                self.DISPLAY.blit(self.nlogo,(230,170))

            if self.check_menu==1:

                self.basic_menu()
                self.DISPLAY.blit(self.gg,(210,80))
                self.DISPLAY.blit(self.icon,(300,15))


            for event in pygame.event.get():

                if event.type==pygame.QUIT:

                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:

                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

                    if event.key==pygame.K_SPACE:
                        self.run()

            pygame.display.update()
    
    def backgroung(self):
        
        self.cloudx1+=0.5
        if self.cloudx1>=850:
            self.cloudx1=-100
        self.DISPLAY.blit(self.cloud,(self.cloudx1,-15))

        self.cloudx2+=0.5
        if self.cloudx2>=850:
            self.cloudx2=-100
        self.DISPLAY.blit(self.cloud,(self.cloudx2,10))

        self.cloudx3+=0.5
        if self.cloudx3>=850:
            self.cloudx3=-100
        self.DISPLAY.blit(self.cloud,(self.cloudx3,-60))

        self.cloudx4+=0.5
        if self.cloudx4>=850:
            self.cloudx4=-100
        self.DISPLAY.blit(self.cloud,(self.cloudx4,-40))

        self.cloudx5+=0.5
        if self.cloudx5>=850:
            self.cloudx5=-100
        self.DISPLAY.blit(self.cloud,(self.cloudx5,50))

        self.bird_rect.right+=2
        if self.bird_rect.right>850:
            self.bird_rect.right=-100
        self.bird_animation()
        self.DISPLAY.blit(self.bird,self.bird_rect)

        self.bird5+=2
        if self.bird5>850:
            self.bird5=-100
        self.bird_animation()
        self.DISPLAY.blit(self.bird,(self.bird5,-50))

    def draw(self):

        self.DISPLAY.fill((BROWN))

        self.DISPLAY.blit(self.BG,BG_POSITION)
        self.DISPLAY.blit(self.tree,(500,-50))

        self.backgroung()

        if self.DEATH_COUNT==0:
            self.DISPLAY.blit(self.h3,(600,10))

        if self.DEATH_COUNT==1:
            self.DISPLAY.blit(self.h2,(600,10))

        if self.DEATH_COUNT==2:
            self.DISPLAY.blit(self.h1,(600,10))

        self.rasen.draw(self.DISPLAY)
        self.rasen.update()

        self.player.draw(self.DISPLAY)
        self.player.update()

        self.obstacle.draw(self.DISPLAY)
        self.obstacle.update() 

        self.collision_sprite()

        pygame.display.update()

    def collision_sprite(self):

        if pygame.sprite.spritecollide(self.player.sprite,self.obstacle,True):

            self.hit_music.play()
            self.DEATH_COUNT+=1

            if self.DEATH_COUNT>=3:

                self.end_music.play()
                pygame.time.delay(1000)
                self.check_menu=1
                self.menu()
        
        if pygame.sprite.spritecollide(self.rasen.sprite,self.obstacle,True):
            None

    def run(self):

        self.DEATH_COUNT=0
        self.check_menu=0
        self.check_attack=False

        while True:

            self.CLOCK.tick(FPS)

            for event in pygame.event.get():

                if event.type==self.obstacle_timer:
                    self.obstacle.add((Obstacle(randint(0,2))))

                if event.type==pygame.KEYDOWN:

                    if event.key==pygame.K_RSHIFT:
                        self.rasen.add((Rasengan()))

                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.draw()

            pygame.display.update()

if __name__=='__main__':

    game= Game()
    game.menu()