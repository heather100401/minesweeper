import pygame, pygame_gui, random


pygame.init()           #INITIALIZE PYGAME


#DISPLAY SETTINGS
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
manager = pygame_gui.UIManager((display_width, display_height),'mine_themes.json')
pygame.display.set_caption('MINESWEEPER')
clock = pygame.time.Clock()

#-----------COLOR PRESETS
bg_pink = (219, 189, 189)

#-----------BOX SIZE PRESETS
box_width = 50
box_height = 50
display.fill(bg_pink)

flag = False
global numMines 

#---------------DRAWINGS-------------------------------------

def blank_boxes(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('blank'))
def draw_zero(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('zero'))
def draw_one(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('one'))
def draw_two(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('two'))
def draw_three(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('three'))
def draw_four(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('four'))
def draw_five(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('five'))
def draw_six(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('six'))
def draw_seven(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('seven'))
def draw_eight(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('eight'))
def draw_flag(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('flag'))
def draw_mine(x,y):
    return pygame_gui.elements.ui_button.UIButton(relative_rect = pygame.Rect(x,y, box_width, box_height),
                                           manager = manager,
                                           text = '',
                                           object_id = pygame_gui.core.object_id.ObjectID('mine'))
    
#------------------------------------------------------------

def mines(mineMap, numMines):
    for i in range(numMines):
        while True:
            x = random.randint(0, 8)  
            y = random.randint(0, 8)  
            if mineMap[x][y] != 1:
                mineMap[x][y] = 1
                break
    return mineMap
def draw_easy():
    grid = []                               #ARRAY OF BOXES
    numMines = 21                           #NUM OF MINES CHANGES DEPENDING ON DIFFICULTY
    mineMap = [[0 for _ in range(10)] for _ in range(10)]
    x = 170                                 #PIXEL LOCATION FOR FIRST BOX
    y = 80
    for i in range (0, 10):
        row = []
        for j in range (0, 10):
            row.append(blank_boxes(x,y))    #ADD 8 BLANK BOXES TO A ROW
            x += box_width
        x = 170
        y += box_height
        grid.append(row)                    #GRID CONTAINS 8x8 BOXES
    mineMap = mines(mineMap, numMines)
    return grid, mineMap

def minesTouching(mineMap, i, j):
    numMinesTouching = 0
    if (i == 9) and (j == 9):                                   #if box is in bottom corner
        if mineMap[i-1][j] == 1:
            numMinesTouching += 1 
        if mineMap[i][j-1] == 1:
            numMinesTouching += 1
        if mineMap[i-1][j-1] == 1:
            numMinesTouching += 1
        return numMinesTouching
        
    if i == 9:                                                  #if bottom row
        if mineMap[i-1][j] == 1:
            numMinesTouching += 1
        if mineMap[i][j+1] == 1:
            numMinesTouching += 1
        if mineMap[i][j-1] == 1:
            numMinesTouching += 1
        if mineMap[i-1][j-1] == 1:
            numMinesTouching += 1
        if mineMap[i-1][j+1] == 1:
            numMinesTouching += 1
        return numMinesTouching

    if j == 9:                                                  #if last column
        if mineMap[i+1][j] == 1:
            numMinesTouching += 1
        if mineMap[i-1][j] == 1:
            numMinesTouching += 1
        if mineMap[i][j-1] == 1:
            numMinesTouching += 1
        if mineMap[i-1][j-1] == 1:
            numMinesTouching += 1
        if mineMap[i+1][j-1] == 1:
            numMinesTouching += 1
        return numMinesTouching

    if mineMap[i+1][j] == 1:
        numMinesTouching += 1
    if mineMap[i-1][j] == 1:
        numMinesTouching += 1
    if mineMap[i][j+1] == 1:
        numMinesTouching += 1
    if mineMap[i][j-1] == 1:
        numMinesTouching += 1
    if mineMap[i+1][j+1] == 1:
        numMinesTouching += 1
    if mineMap[i-1][j-1] == 1:
        numMinesTouching += 1
    if mineMap[i+1][j-1] == 1:
        numMinesTouching += 1
    if mineMap[i-1][j+1] == 1:
        numMinesTouching += 1
    return numMinesTouching

def main():
    run = True
    grid, mineMap = draw_easy()
    boxX = 0
    boxY = 0
    while run:
        time_delta = clock.tick(60) / 1000.0                    #frame rate

        for event in pygame.event.get():                        #logs events

            if event.type == pygame.QUIT:                       #user quits
                run = False
                
            if event.type == pygame_gui.UI_BUTTON_PRESSED:      #user presses button
                box = event.ui_element                          #box = button pressed
                x = box.rect.x                                  #x and y of the box pressed
                y = box.rect.y
                for i in range (0,10):
                    for j in range (0,10):
                        if ((grid[i][j].rect.x == x) and (grid[i][j].rect.y == y)):
                            if mineMap[i][j] == 1:              #if box is mine
                                draw_mine(x,y)
                            else:
                                numMinesTouching = minesTouching(mineMap, i, j)
                                if numMinesTouching == 0:
                                    draw_zero(x,y)
                                elif numMinesTouching == 1:
                                    draw_one(x,y)
                                elif numMinesTouching == 2:
                                    draw_two(x,y)
                                elif numMinesTouching == 3:
                                    draw_three(x,y)
                                elif numMinesTouching == 4:
                                    draw_four(x,y)
                                elif numMinesTouching == 5:
                                    draw_five(x,y)
                                elif numMinesTouching == 6:
                                    draw_six(x,y)
                                elif numMinesTouching == 7:
                                    draw_seven(x,y)
                                elif numMinesTouching == 8:
                                    draw_eight(x,y)
                
            manager.process_events(event)                       #processes events for gui

        manager.update(time_delta)                              #updates frame rate
        manager.draw_ui(display)                                #updates gui
        pygame.display.update()                                 #updates screen
        



main()
pygame.quit()
exit()