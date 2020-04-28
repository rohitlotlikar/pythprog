import pygame
pygame.init()
win=pygame.display.set_mode((600,338))
pygame.display.set_caption("MY FIRST GAME")

walkLeft=[ pygame.image.load('l0.png'), pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'), pygame.image.load('l4.png'),pygame.image.load('l5.png')]
walkRight=[ pygame.image.load('r0.png'), pygame.image.load('r1.png'), pygame.image.load('r2.png'), pygame.image.load('r3.png'), pygame.image.load('r4.png'),pygame.image.load('r5.png')]

bg=pygame.image.load('backg.png')
clock=pygame.time.Clock()
bulletSound=pygame.mixer.Sound('bullet.wav')
hitSound=pygame.mixer.Sound('hit.wav')
music=pygame.mixer.music.load('backmusic.mp3')
pygame.mixer.music.play(-1)
jump=pygame.mixer.Sound('jump.wav')
dead=pygame.mixer.Sound('die.wav')
score=0
class player():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=7
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=walkCount=0
        self.standing=True
        self.hitbox=(self.x+20,self.y+20,42,50)
    def draw(self,win):
        if self.walkCount+1>=18:
            self.walkCount=0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(round(self.x),round(self.y)))
                self.walkCount=self.walkCount+1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(round(self.x),round(self.y)))
                self.walkCount=self.walkCount+1
        else:
            if self.left:
                win.blit(walkLeft[0],(round(self.x),round(self.y)))
            else:
                win.blit(walkRight[0],(round(self.x),round(self.y)))
        self.hitbox=(round(self.x+20),round(self.y),42,50)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)       
    def hit(self):
        dead.play()
        self.isJump=False
        self.jumpCount=10
        self.x=0
        self.y=214
        self.walkcount=0
        font1=pygame.font.SysFont('comicsans',40)
        dead1=font1.render("SCORE -5 ",1,(200,0,0))
        win.blit(dead1,(((600/2-(dead1.get_width()/2))),(338/2-(dead1.get_height()/2))))
        pygame.display.update()
        i=0
        while i<300:
            pygame.time.delay(10)
            i=i+1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i=301
                    pygame.quit()

        
        print("dead") 

        
         

class projectile():
    def __init__(self,x,y,radius,color,facing): 
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)


class enemy():
    walkLeft=[pygame.image.load("tile000.png"),pygame.image.load("tile001.png")]
    walkRight=[pygame.image.load("tile000.png"),pygame.image.load("tile001.png")]
    hit=pygame.image.load("tile002.png")

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.walkCount=0
        self.vel=3
        self.path=[self.x,self.end]
        self.hitbox=(self.x,self.y+27,28,32)
        self.health=10
        self.visible=True

    def draw(self,win): 
        self.move()
        if self.visible:       
            if self.walkCount+1>=6:
                self.walkCount=0
            if self.vel>0:
                win.blit(self.walkRight[self.walkCount //3],(self.x,self.y))
                self.walkCount=self.walkCount+1
            else:
                win.blit(self.walkLeft[self.walkCount //3],(self.x,self.y))
                self.walkCount=self.walkCount+1
            self.hitbox=(self.x,self.y+27,28,32)
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-10,50,7))
            pygame.draw.rect(win,(0,225,0),(self.hitbox[0],self.hitbox[1]-10,50-(5*(10-self.health)),7))
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)


    def move(self):
        if self.vel>0:
            if self.x + self.vel <self.path[1]:
                self.x=self.x+self.vel
            else:
                    self.vel=self.vel*-1
                    self.walkCount=0
        else:
            if self.x-self.vel > self.path[0]:
                self.x =self.x+self.vel
            else:
                self.vel=self.vel*-1
                self.walkCount=0
    def hit(self):
        if self.health>1:
            self.health=self.health-1
        else:
            self.visible=False
        print("hit")


def redrawgameWindow():
    win.blit(bg,(0,0)) 
    text=font.render("Score: "+str(score),1,(255,0,0))
    win.blit(text,(450,10))
    mario.draw(win)  
    maren.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


run=True
mario=player(0,214,81,60)
maren=enemy(100,204,30,60,570)
bullets=[]
bulp=0
font=pygame.font.SysFont('comicsans',30,True,True)

#main loop
while run:
    if maren.visible==True:
        if mario.hitbox[0]+mario.hitbox[2]>maren.hitbox[0]and mario.hitbox[0]<maren.hitbox[0]+maren.hitbox[2]:
            if mario.hitbox[1]+mario.hitbox[3]>maren.hitbox[1]:
                mario.hit()
                score=score -5
    clock.tick(21)
    if bulp>0:
        bulp=bulp+1
        if bulp>10:
            bulp=0
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
    for bullet in bullets:
        if maren.visible:
            if bullet.y + bullet.radius>maren.hitbox[1]:
                if bullet.x+bullet.radius>maren.hitbox[0] and bullet.x<maren.hitbox[0]+maren.hitbox[2]:
                    hitSound.play()
                    maren.hit()
                    score=score+1
                    bullets.pop(bullets.index(bullet))
        if bullet.x<600 and bullet.x>0:
            bullet.x = bullet.x+2*bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and bulp==0:
        bulletSound.play()
        if mario.left:
            facing=-1
        else: 
            facing=1 
        if len(bullets)<3:
            bullets.append(projectile(round((mario.x+mario.width //2)),round((mario.y+mario.height//2)),6,(220,35,0),facing))
        bulp=1
    if keys[pygame.K_LEFT] and mario.x>0:
        mario.x=mario.x-mario.vel
        mario.left=True
        mario.right=False
        mario.standing=False

    elif keys[pygame.K_RIGHT]and mario.x<600-mario.width:
        mario.x=mario.x+mario.vel
        mario.right=True
        mario.left=False
        mario.standing=False

    else:
        mario.standing=True
        mario.walkCount=0

    if not (mario.isJump):

        if keys[pygame.K_UP]:
            jump.play()
            mario.isJump=True  
            mario.right=False
            mario.left=False
            mario.walkCount=0

    else:

        if mario.jumpCount>=-10:
            neg=1

            if mario.jumpCount<0:
                neg=-1
            mario.y -=(mario.jumpCount **2)*0.2*neg
            mario.jumpCount-=1

        else:
            mario.isJump=False
            mario.jumpCount=10
        
    redrawgameWindow()

pygame.quit()