import pygame
import random

# to initialize pygame
pygame.init()

#create screen
screen=pygame.display.set_mode((800,600))

#colours
blue=(0, 255, 242)
red=(255, 15, 0)
white=(255, 255, 255)
yellow=(248, 255, 0)

#Title
pygame.display.set_caption("Tic Tac Toe")

#to open the screen or game loop
running =True

font=pygame.font.Font("freesansbold.ttf",32)
#entery AngryChalk PWSchoolScript
def enter(c):
    if c%2==0:
        score=font.render(" Player vs Player",True,yellow)
        screen.blit(score,(250,258))
        score=font.render(" Player vs Computer",True,white)
        screen.blit(score,(225,310))    
    elif c%2==1:
        score=font.render(" Player vs Player",True,white)
        screen.blit(score,(250,258))
        score=font.render(" Player vs Computer",True,yellow)
        screen.blit(score,(225,310))

#table
def table():
    pygame.draw.line(screen, white, (100,200),(700,200), 4)
    pygame.draw.line(screen, white, (100,400),(700,400), 4)
    pygame.draw.line(screen, white, (300,0),(300,600), 4)
    pygame.draw.line(screen, white, (500,0),(500,600), 4)

#Box
box_x=100
box_y=0
def box(x,y,p):
    if p%2==0:
        pygame.draw.rect(screen, red, [x, y, 200, 200], 8)
    elif p%2==1:
        pygame.draw.rect(screen, blue, [x, y, 200, 200], 8)

#creating Symbol
symbol=pygame.font.Font("freesansbold.ttf",128)
def smb(x,y,p):
    if p%2==0:
        score=symbol.render("X",True,red)
        screen.blit(score,(x+55,y+38))
    elif p%2==1:
        score=symbol.render("O",True,blue)
        screen.blit(score,(x+52,y+38))    

#win
def check(p,cc):
    if a[0][0]==a[1][0]==a[2][0]==p%2:
        return 1
    elif a[0][1]==a[1][1]==a[2][1]==p%2:
        return 2
    elif a[0][2]==a[1][2]==a[2][2]==p%2:
        return 3
    elif a[0][0]==a[0][1]==a[0][2]==p%2:
        return 4
    elif a[1][0]==a[1][1]==a[1][2]==p%2:
        return 5
    elif a[2][0]==a[2][1]==a[2][2]==p%2:
        return 6
    elif a[0][0]==a[1][1]==a[2][2]==p%2:
        return 7
    elif a[0][2]==a[1][1]==a[2][0]==p%2:
        return 8
    elif cc==9:
        return 9
    else:
        return 0

#reset
def reset():
    global a,px,py,pl,cc,status,box_y,box_x,dl
    dl=[(100,0),(100,200),(100,400),(300,0),(300,200),(300,400),(500,0),(500,200),(500,400)]
    a=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    px=[]
    py=[]
    pl=[]
    cc=0
    status="ready"
    box_x=100
    box_y=0
# draw line
def drawline(x):
    if x==4:
        pygame.draw.line(screen, yellow, (200,0),(200,600), 10)
    elif x==5:
        pygame.draw.line(screen, yellow, (400,0),(400,600), 10)
    elif x==6:
        pygame.draw.line(screen, yellow, (600,0),(600,600), 10)
    elif x==1:
        pygame.draw.line(screen, yellow, (100,100),(700,100), 10)
    elif x==2:
        pygame.draw.line(screen, yellow, (100,300),(700,300), 10)
    elif x==3:
        pygame.draw.line(screen, yellow, (100,500),(700,500), 10)
    elif x==7:
        pygame.draw.line(screen, yellow, (100,0),(700,600), 10)
    elif x==8:
        pygame.draw.line(screen, yellow, (700,0),(100,600), 10)

#part 3
def stat(x,p):    
    if x=="win":
        if p%2==0:
            score=symbol.render("X WIN",True,red)
            screen.blit(score,(225,50))
        if p%2==1:
            score=symbol.render("O WIN",True,blue)
            screen.blit(score,(225,50))
    else:
        score=symbol.render("DRAW",True,white)
        screen.blit(score,(200,50))
    score=font.render("Do you want to play again ?",True,yellow)
    screen.blit(score,(190,175))
def enterp(c):
    if c%2==0:
        score=font.render("Yes",True,yellow)
        screen.blit(score,(365,258))
        score=font.render("No",True,white)
        screen.blit(score,(365,310))    
    elif c%2==1:
        score=font.render("Yes",True,white)
        screen.blit(score,(365,258))
        score=font.render("No",True,yellow)
        screen.blit(score,(365,310))

#computer
dl=[(100,0),(100,200),(100,400),(300,0),(300,200),(300,400),(500,0),(500,200),(500,400)]
def comp(x,y):
    global cc,dl,a,px,py,pl,player,part,status,cstatus
    cc+=1
    player+=1
    dl.remove((x,y))
    cxy=random.choice(dl)
    dl.remove(cxy)
    a[((cxy[0]-100)%6)//2][(cxy[1]%6)//2]=player%2
    px.append(cxy[0])
    py.append(cxy[1])
    pl.append(player)
    if check(player,cc)<9 and check(player,cc)>0:
        cstatus=status="win"
        drawline(check(player,cc))
        part+=1
                                
    elif check(player,cc)==9:
        cstatus=status="draw"
        part+=1

#varaiables
part=0
c=0
player=0
a=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
px=[]
py=[]
pl=[]
cc=0
status="ready"
cstatus="ready"
cp=0
while running:
    #screen of background
    screen.fill((1,1,1)) 

    for event in pygame.event.get():
        #if close button is presed
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                if part%3==0:
                    screen.fill((1,1,1))
                    c+=1
                    enter(c)
                elif part%3==1:
                    box_y=(box_y-200)%600
                    box(box_x,box_y,player)
                elif part%3==2:
                    cp+=1
                    enter(cp)    
            if event.key ==pygame.K_DOWN:  
                if part%3==0:
                    c+=1
                    enter(c)
                elif part%3==1:
                    box_y=(box_y+200)%600
                    box(box_x,box_y,player)
                elif part%3==2:
                    cp+=1
                    enter(cp)
            if event.key ==pygame.K_LEFT:  
                if part%3==1:
                    box_x=((box_x-300)%600)+100
                    box(box_x,box_y,player)
                
            if event.key ==pygame.K_RIGHT:  
                if part%3==1:
                    box_x=((box_x+100)%600)+100
                    box(box_x,box_y,player)
            if event.key ==pygame.K_SPACE:  
                if part%3==0:
                    part+=1
                    screen.fill((1,1,1))
                elif part%3==1:
                    if c%2==0:
                        if a[((box_x-100)%6)//2][(box_y%6)//2]==-1:
                            cc+=1
                            a[((box_x-100)%6)//2][(box_y%6)//2]=player%2
                            px.append(box_x)
                            py.append(box_y)
                            pl.append(player)
                            
                            if check(player,cc)<9 and check(player,cc)>0:
                                cstatus=status="win"
                                drawline(check(player,cc))
                                part+=1
                                
                            elif check(player,cc)==9:
                                cstatus=status="draw"
                                part+=1
                            
                            player+=1
                    elif c%2==1:
                        if a[((box_x-100)%6)//2][(box_y%6)//2]==-1:
                            cc+=1
                            a[((box_x-100)%6)//2][(box_y%6)//2]=player%2
                            px.append(box_x)
                            py.append(box_y)
                            pl.append(player)
                            if check(player,cc)<9 and check(player,cc)>0:
                                cstatus=status="win"
                                drawline(check(player,cc))
                                part+=1
                                
                            elif check(player,cc)==9:
                                cstatus=status="draw"
                                part+=1
                            else:
                                comp(box_x,box_y)    
                            player+=1
                elif part%3==2:
                    if cp%2==0:
                        part+=2
                        player=0
                    else:
                        part+=1
                        player=0
                        cp+=1
                        if c%2==1:
                            c=0

    #creating symbol
    for i in range(len(px)):
        smb(px[i],py[i],pl[i])
    if status=="win":
        table()
        pygame.display.update()
        pygame.time.delay(1000)   
        reset() 
    if status=="draw":
        reset()
    #calling part
    if part%3==0:
        enter(c)
    elif part%3==1:
        if c%2==0:
            table()
            box(box_x,box_y,player)
        else:
            table()
            box(box_x,box_y,player)
    elif part%3==2:
        stat(cstatus,player-1)
        enterp(cp)
    pygame.display.update()
        