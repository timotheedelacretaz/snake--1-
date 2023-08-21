import pygame
import sys
import random
import math
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

pygame.init()
font = pygame.font.SysFont('arial',40)
smallfont = pygame.font.SysFont('arial',20)
black = pygame.Color(0, 10, 0)
white = pygame.Color(255, 255, 255)
whitesnake = pygame.Color(255, 255, 255)
whitewall = pygame.Color(255, 255, 255)
grey = pygame.Color(190, 190, 190)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(250, 250, 0)
lightgreen = pygame.Color(140, 255, 140)
purple = pygame.Color(255, 100, 255)
black2 = pygame.Color(60, 70, 60)
greenmenu = pygame.Color(60,100,60)
color1 = pygame.Color(0, 100, 240)
color2 = pygame.Color(60, 60, 180)
color3 = pygame.Color(120, 0, 120)
color4 = pygame.Color(180, 60, 60)
color5 = pygame.Color(240, 100, 0)
unit = 16
modgrowth = 3
window_x = unit*68
window_y = unit*50+40
game_window = pygame.display.set_mode((window_x, window_y))
clock = pygame.time.Clock()
pygame.display.update()  
change = "null"       
running = True
x1 = 0
y1 = 0
x1c = 0
y1c = 0
dir = 0
x2 = 0
y2 = 0
x2c = 0
y2c = 0
dir2 = 0
c = 0
r = 0
w = 0
multi = 0
speed = 15
snake_list = []
snake_list2 = []
gstate = 'start'
Length_of_snake = 1
Length_of_snake2 = 1
sliderwidth = 140
sliderheight = 30
outputbox = 30
buttonwidth = 100
buttonheight = 40
wallposition=[]
modwall = 0
modaccspeed = 0
modrndspeed = 0
modborder = 0
modteleport = 0
win = 0
fruit_position = []
fruit_position2 = []
fruit_number = 1
delfruit = []
fruit_label = str(fruit_number)+" fruit"
sizelabel = 'big size' 
cha = 1
chb = 0
maxscore = 0
maxscore2 = 0
flagfunction = 0
timer = 0
stimer = 0
mtimer = 0
colorpicker = pygame.Color(0,0,0)

button = Button(game_window,window_x/2,window_y/2-buttonheight/2,buttonwidth,buttonheight,text='2 player',onClick=lambda: change(3))
button4 = Button(game_window,window_x/2-buttonwidth,window_y/2-buttonheight/2,buttonwidth,buttonheight,text='1 player',onClick=lambda: change(1))
button2 = Button(game_window,window_x/2,window_y/2-buttonheight/2,buttonwidth,buttonheight,text='restart',onClick=lambda: change(4))
button3 = Button(game_window,window_x/2-buttonwidth,window_y/2-buttonheight/2,buttonwidth,buttonheight,text='menu',onClick=lambda: change(2))
slider = Slider(game_window,int(window_x/2)-int(sliderwidth/2),int(button.getY())-60,sliderwidth,sliderheight,min=10,max=50,step=1)
output = TextBox(game_window, slider.getX()+slider.getWidth()-outputbox, slider.getY()-slider.getHeight()*2, outputbox, outputbox, fontSize=20)
button6 = Button(game_window,button.getX()+outputbox/4,button.getY()+2*buttonheight,buttonwidth,buttonheight,text='wall',onClick=lambda: change(6))
button7 = Button(game_window,button.getX()-outputbox/4-buttonwidth,button.getY()+3*buttonheight+outputbox/2,buttonwidth,buttonheight,text='acceleration',onClick=lambda: change(7))
button8 = Button(game_window,button.getX()+outputbox/4,button.getY()+3*buttonheight+outputbox/2,buttonwidth,buttonheight,text='randomspeed',onClick=lambda: change(8))
button9 = Button(game_window,button.getX()-outputbox/4-buttonwidth,button.getY()+4*buttonheight+outputbox/2+outputbox/2,buttonwidth,buttonheight,text='noborder',onClick=lambda: change(9))
button11 = Button(game_window,button.getX()-outputbox/4-buttonwidth,button.getY()+5*buttonheight+outputbox/2+outputbox,buttonwidth,buttonheight,text='teleport',onClick=lambda: change(11))
button12 = Button(game_window,window_x-buttonwidth-buttonwidth/8,buttonheight/8,buttonwidth,buttonheight,text='menu',onClick=lambda: change(2))
button13 = Button(game_window,unit,unit,buttonwidth,buttonheight,text='theme',onClick=lambda: change(12))
button14 = Button(game_window,unit,unit,buttonwidth,buttonheight,text='menu',onClick=lambda: change(2))
slider2 = Slider(game_window,int(window_x/2)-int(sliderwidth/2),int(4*window_y/6)+40,sliderwidth,sliderheight,min=0,max=255,step=1)
slider3 = Slider(game_window,int(window_x/2)-int(sliderwidth/2),slider2.getY()+sliderheight+40,sliderwidth,sliderheight,min=0,max=255,step=1)
slider4 = Slider(game_window,int(window_x/2)-int(sliderwidth/2),slider3.getY()+sliderheight+40,sliderwidth,sliderheight,min=0,max=255,step=1)


def our_snake(snake_list):
    pygame.draw.rect(game_window,lightgreen, [snake_list[0][0], snake_list[0][1], unit*modgrowth, unit*modgrowth])
    pygame.draw.rect(game_window,green, [snake_list[-1][0], snake_list[-1][1], unit*modgrowth, unit*modgrowth])
    for x in snake_list[1:len(snake_list)-1]:
        pygame.draw.rect(game_window,whitesnake, [x[0], x[1], unit*modgrowth, unit*modgrowth])

        

def our_snake2(snake_list2):
    pygame.draw.rect(game_window,purple, [snake_list2[0][0], snake_list2[0][1], unit*modgrowth, unit*modgrowth])
    pygame.draw.rect(game_window,yellow, [snake_list2[-1][0], snake_list2[-1][1], unit*modgrowth, unit*modgrowth])
    for x in snake_list2[1:len(snake_list2)-1]:
        pygame.draw.rect(game_window,grey, [x[0], x[1], unit*modgrowth, unit*modgrowth])


def change(x):
    global gstate,r,multi,modgrowth,modwall,x1,y1,x2,y2,x1c,y1c,x2c,y2c,dir,dir2,c,w,snake_list,snake_list2,Length_of_snake,Length_of_snake2,fruit_position,wallposition,modwall,win,speed,modrndspeed,modaccspeed,modaccspeed,modrndspeed,modborder,fruit_label,fruit_number,cha,flagfunction,fruit_position2,modteleport
    x1 = 0
    y1 = 0
    x1c = 0
    y1c = 0
    dir = 0
    x2 = 0
    y2 = 0
    x2c = 0
    y2c = 0
    dir2 = 0
    c = 0
    r = 0
    w = 0
    snake_list=[]
    Length_of_snake=1
    snake_list2=[]
    Length_of_snake2=1
    fruit_position=[]
    fruit_position2=[]
    r = 0
    win = 0
    wallposition = []
    if x==1:
        game_window.fill((0,10,0))
        gstate = 'run'
        multi = 0
        speed = slider.getValue()
        flagfunction = 1
    if x==2:
        game_window.fill((0,0,0))
        gstate = 'start'
    if x==3:
        game_window.fill((0,10,0))
        gstate = 'run'
        multi = 1
        speed = slider.getValue()
        flagfunction = 1
    if x==4:
        game_window.fill((0,10,0))
        gstate = 'run'
        speed = slider.getValue()
    if x==5:
        if modgrowth == 1:
            modgrowth = 3
        elif modgrowth == 2:
            modgrowth = 1
        elif modgrowth == 3:
            modgrowth = 2
        cha = 1
        flagfunction = 1
    if x == 6:
        if modwall == 0:
            modwall = 1
        elif modwall == 1:
            modwall = 0
        flagfunction = 1
    if x == 7:
        if modaccspeed == 0:
            modaccspeed = 1
        elif modaccspeed == 1:
            modaccspeed = 0
        flagfunction = 1
    if x == 8:
        if modrndspeed == 0:
            modrndspeed= 1
        elif modrndspeed == 1:
            modrndspeed= 0
        flagfunction = 1
    if x == 9:
        if modborder == 0:
            modborder= 1
        elif modborder == 1:
            modborder= 0
        flagfunction = 1
    if x == 10:
        if fruit_number==5:
            fruit_number=0
        fruit_number+=1
        fruit_label = str(fruit_number)+" fruit"
        cha = 1
    if x == 11:
        if modteleport == 0:
            modteleport= 1
        elif modteleport == 1:
            modteleport= 0
        flagfunction = 1
    if x==12:
        game_window.fill((0,0,0))
        gstate = 'theme'



def spawn():
    global fruit_position,Length_of_snake,Length_of_snake2,w,modwall,j,k,speed,delfruit,modgrowth
    
    safezone = []
    i = []
    for x in range(0,int(math.sqrt(((10-modgrowth-1)*(10-modgrowth))+1))):
        g = [snake_list[-1][0]-unit*((int(math.sqrt(((10-modgrowth-1)*(10-modgrowth))+1))-1)/2),snake_list[-1][1]-unit*((int(math.sqrt(((10-modgrowth-1)*(10-modgrowth))+1))-1)/2)]
        b = x*unit
        for y in range(0,int(math.sqrt(((10-modgrowth-1)*(10-modgrowth))+1))):
            c = y*unit
            i.append(g[0]+b)
            i.append(g[1]+c)
            safezone.append(i)
            i = []

    u = 0
    for x in fruit_position:
        if x[2] == delfruit[2]:
            u = x
    fruit_position.remove(u)
    if modteleport==1:
        for x in fruit_position2:
            if x[2] == delfruit[2]:
                u = x
        fruit_position2.remove(u)
    s = delfruit[2]
    z=0
    while z==0:
        f1=[(random.randrange(unit,window_x-(2*unit),unit*modgrowth)),(random.randrange(unit+40,window_y-(2*unit)-40,unit*modgrowth))]
        if f1 not in snake_list:
            if f1 not in fruit_position2:
                if f1 not in fruit_position:
                    if f1 not in wallposition:
                        z=1
    fruit_position.append([f1[0],f1[1],s])
    if modteleport==1:
        z=0
        while z==0:
            f2=[(random.randrange(unit,window_x-(2*unit),unit*modgrowth)),(random.randrange(unit+40,window_y-(2*unit)-40,unit*modgrowth))]
            if f2 not in snake_list:
                if f2 not in fruit_position2:
                    if f2 not in fruit_position:
                        if f2 not in wallposition:
                            z=1
        fruit_position2.append([f2[0],f2[1],s])



    j =0 
    if modwall == 1:
        while j == 0:
            v =[(random.randrange(unit,window_x-(2*unit),unit*modgrowth)),(random.randrange(unit+40,window_y-(2*unit)-40,unit*modgrowth))]
            if v not in wallposition:
                if v not in safezone:
                    if v not in fruit_position:
                        if v not in snake_list:
                            if v not in snake_list2:
                                j = 1   
        wallposition.append(v)
    

    if modrndspeed ==1:
        speed = random.randrange(16,54)

    if modaccspeed==1:
        speed +=1*((Length_of_snake-1)+(Length_of_snake2-1))
    
    if w==1:
        Length_of_snake+=1
        w=0
    if w==2:
        Length_of_snake2+=1
        w=0


    delfruit =[]



while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()


    if cha ==1:
        if modgrowth==1:
            sizelabel = 'big size'
        if modgrowth==2:
            sizelabel = 'medium size'
        if modgrowth==3:
            sizelabel = 'small size'
        if chb == 1:
            button10.disable()
            button10.hide()
            button5.disable()
            button5.hide()
        button5 = Button(game_window,button.getX()-outputbox/4-buttonwidth,button.getY()+2*buttonheight,buttonwidth,buttonheight,text=sizelabel,onClick=lambda: change(5))
        button10 = Button(game_window,button.getX()+outputbox/4,button.getY()+4*buttonheight+outputbox,buttonwidth,buttonheight,text=fruit_label,onClick=lambda: change(10))
        cha = 0
        chb = 1

    
    
    if gstate == 'start':
        
        button.enable()
        button.show()
        button4.enable()
        button4.show()
        button2.disable()
        button2.hide()
        button3.disable()
        button3.hide()
        output.enable()
        output.show()
        slider.enable()
        slider.show()
        button5.enable()
        button5.show()
        button6.enable()
        button6.show()
        button7.enable()
        button7.show()
        button8.enable()
        button8.show()
        button9.enable()
        button9.show()
        button10.enable()
        button10.show()
        button11.enable()
        button11.show()
        button12.disable()
        button12.hide()
        button13.enable()
        button13.show()
        button14.disable()
        button14.hide()
        slider2.disable()
        slider2.hide()
        slider3.disable()
        slider3.hide()
        slider4.disable()
        slider4.hide()
        


        pygame.draw.rect(game_window,greenmenu, [0, 0, window_x, window_y])
        if modgrowth == 2:
            pygame.draw.rect(game_window,color3, [button5.getX()-outputbox/4, button5.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        elif modgrowth ==3:
            pygame.draw.rect(game_window,color1, [button5.getX()-outputbox/4, button5.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        else:
            pygame.draw.rect(game_window,color5, [button5.getX()-outputbox/4, button5.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        if modwall == 1:
            pygame.draw.rect(game_window,red, [button6.getX()-outputbox/4, button6.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        else:
            pygame.draw.rect(game_window,black, [button6.getX()-outputbox/4, button6.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        if modaccspeed == 1:
            pygame.draw.rect(game_window,red, [button7.getX()-outputbox/4, button7.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        else:
            pygame.draw.rect(game_window,black, [button7.getX()-outputbox/4, button7.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        if modrndspeed == 1:
            pygame.draw.rect(game_window,red, [button8.getX()-outputbox/4, button8.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        else:
            pygame.draw.rect(game_window,black, [button8.getX()-outputbox/4, button8.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        if modborder == 1:
            pygame.draw.rect(game_window,red, [button9.getX()-outputbox/4, button9.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        else:
            pygame.draw.rect(game_window,black, [button9.getX()-outputbox/4, button9.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        if fruit_number == 1:
            pygame.draw.rect(game_window,color1, [button10.getX()-outputbox/4, button10.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        elif fruit_number == 2:
            pygame.draw.rect(game_window,color2, [button10.getX()-outputbox/4, button10.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        elif fruit_number == 3:
            pygame.draw.rect(game_window,color3, [button10.getX()-outputbox/4, button10.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        elif fruit_number == 4:
            pygame.draw.rect(game_window,color4, [button10.getX()-outputbox/4, button10.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        else:
            pygame.draw.rect(game_window,color5, [button10.getX()-outputbox/4, button10.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        if modteleport == 1:
            pygame.draw.rect(game_window,red, [button11.getX()-outputbox/4, button11.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])
        else:
            pygame.draw.rect(game_window,black, [button11.getX()-outputbox/4, button11.getY()-outputbox/4, buttonwidth+outputbox/2,buttonheight+outputbox/2])


        game_window.blit(smallfont.render(('speed'),True,(0,0,0)),(slider.getX(), slider.getY()-slider.getHeight()*2))

        speed=slider.getValue()
        output.setText(slider.getValue())
    
        pygame_widgets.update(events)
        pygame.display.update()
    
    elif gstate == 'theme':
        button.disable()
        button.hide()
        button4.disable()
        button4.hide()
        button2.disable()
        button2.hide()   
        button3.disable()
        button3.hide()
        output.disable()
        output.hide()
        slider.disable()
        slider.hide()
        button5.disable()
        button5.hide()
        button6.disable()
        button6.hide()
        button7.disable()
        button7.hide()
        button8.disable()
        button8.hide()
        button9.disable()
        button9.hide()
        button10.disable()
        button10.hide()
        button11.disable()
        button11.hide()
        button12.disable()
        button12.hide()
        button13.disable()
        button13.hide()
        button14.enable()
        button14.show()
        slider2.enable()
        slider2.show()
        slider3.enable()
        slider3.show()
        slider4.enable()
        slider4.show()

        pygame.draw.rect(game_window,greenmenu, [0, 0, window_x, window_y]) 

        r = slider2.getValue()
        g = slider3.getValue()
        b = slider4.getValue()
        colorpicker=pygame.Color(r,g,b)
        pygame.draw.rect(game_window,black, [window_x/4-8, window_y/14-8, window_x/2+28,2*unit+16])
        pygame.draw.rect(game_window,white, [window_x/4-4, window_y/14-4, window_x/2+20,2*unit+8])
        pygame.draw.rect(game_window,colorpicker, [window_x/4, window_y/14, window_x/2+12,2*unit])
        k = 0
        for x in range(0,10):
            for y in range(0,9):
                if k == 1:
                    a = window_x/4-unit*2+20
                else:
                    a = window_x/4+20
                b = window_y/8+20
                a += y*unit*2*2
                b += x*unit*2
                pygame.draw.rect(game_window, black, pygame.Rect(a, b, unit*2,unit*2))
            if k == 0:
                k = 1
            else:
                k = 0
        for x in range(0,10):
            for y in range(0,9):
                if k == 1:
                    a = window_x/4+20
                else:
                    a = window_x/4-unit*2+20
                b = window_y/8+20
                a += y*unit*2*2
                b += x*unit*2
                pygame.draw.rect(game_window, black2, pygame.Rect(a, b, unit*2,unit*2))
            if k == 0:
                k = 1
            else:
                k = 0
        cbuttonwall = pygame.draw.rect(game_window,whitewall, [window_x/2+4, window_y/2-7-2*unit, 2*unit,2*unit])
        cbuttonwall2 = pygame.draw.rect(game_window,whitewall, [window_x/2+4-6*2*unit, window_y/2-7-4*2*unit, 2*unit,2*unit])
        cbuttonp1 = pygame.draw.rect(game_window,green, [window_x/2+4-3*2*unit, window_y/2-7-3*2*unit, 2*unit,2*unit])
        cbuttonp12 = pygame.draw.rect(game_window,whitesnake, [window_x/2+4-3*2*unit, window_y/2-7-4*2*unit, 2*unit,2*unit])
        cbuttonp13 = pygame.draw.rect(game_window,whitesnake, [window_x/2+4-3*2*unit, window_y/2-7-5*2*unit, 2*unit,2*unit])
        cbuttonp14 = pygame.draw.rect(game_window,lightgreen, [window_x/2+4-3*2*unit, window_y/2-7-6*2*unit, 2*unit,2*unit])
        cbuttonp2 = pygame.draw.rect(game_window,yellow, [window_x/2+4+5*2*unit, window_y/2-7-3*2*unit, 2*unit,2*unit])
        cbuttonp22 = pygame.draw.rect(game_window,grey, [window_x/2+4+5*2*unit, window_y/2-7-4*2*unit, 2*unit,2*unit])
        cbuttonp23 = pygame.draw.rect(game_window,grey, [window_x/2+4+5*2*unit, window_y/2-7-5*2*unit, 2*unit,2*unit])
        cbuttonp24 = pygame.draw.rect(game_window,purple, [window_x/2+4+5*2*unit, window_y/2-7-6*2*unit, 2*unit,2*unit])
        for ev in pygame.event.get():
            if ev.type==pygame.MOUSEBUTTONDOWN:
                if mouse[0]>cbuttonwall.x and mouse[0]<cbuttonwall.x+2*unit and mouse[1]>cbuttonwall.y and mouse[1]<cbuttonwall.y+2*unit:
                    whitewall = colorpicker
                if mouse[0]>cbuttonwall2.x and mouse[0]<cbuttonwall2.x+2*unit and mouse[1]>cbuttonwall2.y and mouse[1]<cbuttonwall2.y+2*unit:
                    whitewall = colorpicker
                if mouse[0]>cbuttonp1.x and mouse[0]<cbuttonp1.x+2*unit and mouse[1]>cbuttonp1.y and mouse[1]<cbuttonp1.y+2*unit:
                    green = colorpicker
                if mouse[0]>cbuttonp12.x and mouse[0]<cbuttonp12.x+2*unit and mouse[1]>cbuttonp12.y and mouse[1]<cbuttonp12.y+2*unit:
                    whitesnake = colorpicker
                if mouse[0]>cbuttonp13.x and mouse[0]<cbuttonp13.x+2*unit and mouse[1]>cbuttonp13.y and mouse[1]<cbuttonp13.y+2*unit:
                    whitesnake = colorpicker
                if mouse[0]>cbuttonp14.x and mouse[0]<cbuttonp14.x+2*unit and mouse[1]>cbuttonp14.y and mouse[1]<cbuttonp14.y+2*unit:
                    lightgreen = colorpicker
                if mouse[0]>cbuttonp2.x and mouse[0]<cbuttonp2.x+2*unit and mouse[1]>cbuttonp2.y and mouse[1]<cbuttonp2.y+2*unit:
                    yellow = colorpicker
                if mouse[0]>cbuttonp22.x and mouse[0]<cbuttonp22.x+2*unit and mouse[1]>cbuttonp22.y and mouse[1]<cbuttonp22.y+2*unit:
                    grey = colorpicker
                if mouse[0]>cbuttonp23.x and mouse[0]<cbuttonp23.x+2*unit and mouse[1]>cbuttonp23.y and mouse[1]<cbuttonp23.y+2*unit:
                    grey = colorpicker
                if mouse[0]>cbuttonp24.x and mouse[0]<cbuttonp24.x+2*unit and mouse[1]>cbuttonp24.y and mouse[1]<cbuttonp24.y+2*unit:
                    purple = colorpicker
        pygame_widgets.update(events)
        pygame.display.update()


    elif gstate == 'run': 
        
        button.disable()
        button.hide()
        button4.disable()
        button4.hide()
        button2.disable()
        button2.hide()   
        button3.disable()
        button3.hide()
        output.disable()
        output.hide()
        slider.disable()
        slider.hide()
        button5.disable()
        button5.hide()
        button6.disable()
        button6.hide()
        button7.disable()
        button7.hide()
        button8.disable()
        button8.hide()
        button9.disable()
        button9.hide()
        button10.disable()
        button10.hide()
        button11.disable()
        button11.hide()
        button12.enable()
        button12.show()
        button13.disable()
        button13.hide()
        button14.disable()
        button14.hide()
        slider2.disable()
        slider2.hide()
        slider3.disable()
        slider3.hide()
        slider4.disable()
        slider4.hide()

        if flagfunction ==1:
            maxscore=0
            maxscore2=0
            flagfunction = 0
        
        if Length_of_snake == 1 and c == 0:
            if multi == 0:
                x1 = unit*(37-modgrowth)
                y1 = unit*25+40
            if multi == 1:
                x1 = unit*(25-modgrowth)
                y1 = unit*(19-modgrowth)+40
                x2 = unit*(37+modgrowth)
                y2 = unit*(25+modgrowth)+40
            game_window.fill((0,10,0))



            for x in range(0,fruit_number):
                if fruit_position==[]:
                    s = 1
                else:
                    s= fruit_position[-1][2]
                    if s==5:
                        s=0
                    s+=1
                fruit_position.append([(random.randrange(unit,window_x-(2*unit),unit*modgrowth)),(random.randrange(unit+40,window_y-(2*unit)-40,unit*modgrowth)),s])
                if modteleport==1:
                    fruit_position2.append([(random.randrange(unit,window_x-(2*unit),unit*modgrowth)),(random.randrange(unit+40,window_y-(2*unit)-40,unit*modgrowth)),s])
            c =1  

        if dir==0 and Length_of_snake==1 and snake_list!=[unit*(37-modgrowth),unit*25+40]:
            timer=0
        if multi==1:
            if dir==0 and Length_of_snake==1 and snake_list!=[unit*(25-modgrowth),unit*(19-modgrowth)+40] and snake_list2!=[unit*(37+modgrowth),unit*(25+modgrowth)+40]:
                timer=0


        for x in fruit_position:
            pygame.draw.rect(game_window, black, pygame.Rect(x[0], x[1], unit*modgrowth, unit*modgrowth))
        if modteleport==1:
            for x in fruit_position2:
                pygame.draw.rect(game_window, black, pygame.Rect(x[0], x[1], unit*modgrowth, unit*modgrowth))

        for pos in snake_list:
            pygame.draw.rect(game_window, black,pygame.Rect(pos[0], pos[1], unit*modgrowth, unit*modgrowth))
        for pos in snake_list2:
            pygame.draw.rect(game_window, black,pygame.Rect(pos[0], pos[1], unit*modgrowth, unit*modgrowth))

        k = 0
        for x in range(0,int((window_y-40)/unit/modgrowth)):
            for y in range(0,int(window_x/unit/2/modgrowth+1)):
                if k == 1:
                    a = -unit*(modgrowth-1)
                else:
                    a = unit
                b = 40+unit
                a += y*unit*2*modgrowth
                b += x*unit*modgrowth
                pygame.draw.rect(game_window, black2, pygame.Rect(a, b, unit*modgrowth,unit*modgrowth ))
            if k == 0:
                k = 1
            else:
                k = 0


        for x in wallposition:
            pygame.draw.rect(game_window, whitewall, pygame.Rect(x[0], x[1], unit*modgrowth, unit*modgrowth))



        if keys[pygame.K_w] and not dir == 1:
            x1c = 0
            y1c = -unit*modgrowth
            dir = 2
        elif keys[pygame.K_s] and not dir == 2:
            x1c = 0
            y1c = +unit*modgrowth
            dir = 1
        elif keys[pygame.K_a] and not dir == 3:
            x1c = -unit*modgrowth
            y1c = 0
            dir = 4
        elif keys[pygame.K_d] and not dir == 4:
            x1c = +unit*modgrowth
            y1c = 0
            dir = 3
        if keys[pygame.K_UP] and not dir2 == 1:
            x2c = 0
            y2c = -unit*modgrowth
            dir2 = 2
        elif keys[pygame.K_DOWN] and not dir2 == 2:
            x2c = 0
            y2c = +unit*modgrowth
            dir2 = 1
        elif keys[pygame.K_LEFT] and not dir2 == 3:
            x2c = -unit*modgrowth
            y2c = 0
            dir2 = 4
        elif keys[pygame.K_RIGHT] and not dir2 == 4:
            x2c = +unit*modgrowth
            y2c = 0
            dir2 = 3


        
        x1 += x1c
        y1 += y1c
        x2 += x2c
        y2 += y2c

        if modborder==1:
            if x1 <= 0:
                x1 = window_x-((modgrowth+1)*unit)
            if x1 >= window_x-unit:
                x1 = unit
            if y1 < +unit+40:
                y1 = window_y-(modgrowth+1)*unit
            if y1 > window_y-(modgrowth+1)*unit:
                y1=+40+unit
            if multi==1:
                if x2 < unit:
                    x2 = window_x-unit
                elif x2 > window_x-unit:
                    x2 = -unit*(modgrowth-1)
                elif y2 < +unit+40:
                    y2 = window_y-unit
                elif y2 > window_y-unit:
                    y2=+40+(unit*(modgrowth-1))

        if modteleport==1:
            for x in fruit_position:
                if (x1 == x[0]and y1 == x[1]):
                    delfruit = [x1,y1,x[2]]
                    w = 1
                    for y in fruit_position2:
                        if y[2]==x[2]:
                            x1=y[0]
                            y1=y[1]
                    dir=0
                    spawn()
                if (x2 == x[0]and y2 == x[1]):
                    delfruit = [x2,y2,x[2]]
                    w = 2
                    for y in fruit_position2:
                        if y[2]==x[2]:
                            x2=y[0]
                            y2=y[1]
                    dir=0
                    spawn()
                    
            for x in fruit_position2:
                if (x1 == x[0]and y1 == x[1]):
                    delfruit = [x1,y1,x[2]]
                    w = 1
                    for y in fruit_position:
                        if y[2]==x[2]:
                            x1=y[0]
                            y1=y[1]
                    dir2=0
                    spawn()
                if (x2 == x[0]and y2 == x[1]):
                    delfruit = [x2,y2,x[2]]
                    w = 2
                    for y in fruit_position:
                        if y[2]==x[2]:
                            x2=y[0]
                            y2=y[1]
                    dir2=0
                    spawn()

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]
        our_snake(snake_list)

        if multi == 1:
            snake_Head2 = []
            snake_Head2.append(x2)
            snake_Head2.append(y2)
            snake_list2.append(snake_Head2)
            if len(snake_list2) > Length_of_snake2:
                del snake_list2[0]
            our_snake2(snake_list2)

        if modteleport==0:
            for x in fruit_position:
                if (x1 == x[0]and y1 == x[1]):
                    delfruit = [x1,y1,x[2]]
                    w = 1
                    spawn()
                if (x2 == x[0]and y2 == x[1]):
                    delfruit = [x2,y2,x[2]]
                    w = 2
                    spawn()
                    
            for x in fruit_position2:
                if (x1 == x[0]and y1 == x[1]):
                    delfruit = [x1,y1,x[2]]
                    w = 1
                    spawn()
                if (x2 == x[0]and y2 == x[1]):
                    delfruit = [x2,y2,x[2]]
                    w = 2
                    spawn()


        for x in wallposition:
            if (x1 == x[0]and y1 == x[1]):
                if multi == 1:
                    win = 2
                gstate = 'gameover'

        if modborder==0:        
            if x1 < +unit or x1 >= window_x-unit:
                if multi == 1:
                    win = 2
                gstate = 'gameover'
            if y1 < +unit+40 or y1 >= window_y-unit:
                if multi == 1:
                    win = 2
                gstate = 'gameover'
        for x in snake_list[:len(snake_list)-1]:
            if snake_list[-1][0] == x[0] and snake_list[-1][1] == x[1]:
                if multi == 1:
                    win = 2
                gstate = 'gameover'

        if multi == 1:
            for x in wallposition:
                if (x2 == x[0]and y2 == x[1]):
                    win = 1
                    gstate = 'gameover'
            for x in wallposition:
                if (x1 == x[0]and y1 == x[1]):
                    win = 1
                    gstate = 'gameover'
            else:
                if x2 < +unit or x2 > window_x-(2*unit):
                    win = 1
                    gstate = 'gameover'
                if y2 < +unit+40 or y2 > window_y-(2*unit):
                    win = 1
                    gstate = 'gameover'
            for x in snake_list2[:len(snake_list2)-1]:
                if snake_list2[-1][0] == x[0] and snake_list2[-1][1] == x[1]:
                    win = 1
                    gstate = 'gameover'
            for x in snake_list2[:len(snake_list2)-1]:
                if snake_list[-1][0] == x[0] and snake_list[-1][1] == x[1]:
                    win = 2
                    gstate = 'gameover'
            for x in snake_list[:len(snake_list)-1]:
                if snake_list2[-1][0] == x[0] and snake_list2[-1][1] == x[1]:
                    win = 1
                    gstate = 'gameover'
            if snake_list[0][0] == snake_list2[0][0] and snake_list[0][1] == snake_list2[0][1]:
                gstate = 'gameover'

                
        pygame.draw.rect(game_window, greenmenu, pygame.Rect(0, 0, unit, window_y))
        pygame.draw.rect(game_window, greenmenu, pygame.Rect(0, window_y-unit, window_x, unit))
        pygame.draw.rect(game_window, greenmenu, pygame.Rect(window_x-unit, 0, unit, window_y))
        pygame.draw.rect(game_window, greenmenu, pygame.Rect(0, 0, window_x, unit+40))
        f = 0
        for x in fruit_position:
            f+=1
            colorfruit = 'color'+str(x[2])
            pygame.draw.rect(game_window, locals()[colorfruit], pygame.Rect(x[0], x[1], unit*modgrowth, unit*modgrowth))
        for x in fruit_position2:
            f+=1
            colorfruit = 'color'+str(x[2])
            pygame.draw.rect(game_window, locals()[colorfruit], pygame.Rect(x[0], x[1], unit*modgrowth, unit*modgrowth))
        game_window.blit(smallfont.render(('Score P1'+" "+str(Length_of_snake-1)),True,(0,0,0)),(unit,0))
        game_window.blit(smallfont.render(('Score P1'+" "+str(Length_of_snake-1)),True,(255,255,255)),(unit,0))
        if multi == 1:
            game_window.blit(smallfont.render(('Score P2'+" "+str(Length_of_snake2-1)),True,(0,0,0)),(10*unit,0))
            game_window.blit(smallfont.render(('Score P2'+" "+str(Length_of_snake2-1)),True,(255,255,255)),(10*unit,0))
        
        timer +=clock.get_time()
        stimer = int(timer/1000)
        mtimer = int(stimer/60)
        stimer-=mtimer*60
        strtimer = str(mtimer)+" m "+str(stimer)+" s"
        game_window.blit(smallfont.render((strtimer),True,(255,255,255)),(window_x/2-36,0))   

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(speed/modgrowth) 



    elif gstate == 'gameover':
        button2.enable()
        button2.show()
        button3.enable()
        button3.show()
        button12.disable()
        button12.hide()
        if maxscore<(Length_of_snake-1):
            maxscore = Length_of_snake-1
        if multi==1:
            if maxscore2<(Length_of_snake2-1):
                maxscore2 = Length_of_snake2-1

        game_window.fill((0,0,0))
        pygame.draw.rect(game_window,greenmenu, [0, 0, window_x, window_y])
        game_window.blit(font.render('Game Over',True,(0,0,0)),(window_x/2-104,button3.getY()-120))

        if win == 1:
            game_window.blit(font.render('P1 Win',True,(0,0,0)),(window_x/2-104,button3.getY()-60))
        elif win == 2:
            game_window.blit(font.render('P2 Win',True,(0,0,0)),(window_x/2-104,button3.getY()-60)) 

        if multi ==1:
            game_window.blit(smallfont.render(('Score P1'+" "+str(Length_of_snake-1)),True,(255,255,255)),(window_x/4+52,button3.getY()-180))   
            game_window.blit(smallfont.render(('Score P2'+" "+str(Length_of_snake2-1)),True,(255,255,255)),(3*window_x/4-156,button3.getY()-180))
            game_window.blit(smallfont.render(('max Score P2'+" "+str(maxscore2)),True,(255,255,255)),(3*window_x/4-176,button3.getY()-240))
            game_window.blit(smallfont.render(('max Score P1'+" "+str(maxscore)),True,(255,255,255)),(window_x/4+32,button3.getY()-240))
        else:
            game_window.blit(smallfont.render(('Score P1'+" "+str(Length_of_snake-1)),True,(255,255,255)),(window_x/2-52,button3.getY()-180))
            game_window.blit(smallfont.render(('max Score P1'+" "+str(maxscore)),True,(255,255,255)),(window_x/2-72,button3.getY()-240))   
    
        if keys[pygame.K_SPACE]:
            change(4)


        pygame_widgets.update(events)        
        pygame.display.update()    
           