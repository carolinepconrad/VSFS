'''
Cairn University, Fall 2023, CIS 321, Prof Petcaugh
Student Name: Caroline Conrad
'''

import pygame


# Start up, and set up, pygame
pygame.init()
screen = pygame.display.set_mode([900, 750])
clock = pygame.time.Clock()


# Data Structures


# Classes
class HDrive:
    def __init__(self, x, y, w, h, c,b):
        # x, y coord; w width; h height; c for color ; border
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.b = b

    def draw(self):
        pygame.draw.rect(screen, self.c, (self.x, self.y, self.w, self.h),self.b)



#Hard Drive Structure
sblock = HDrive(50,100,100,100,(0,0,0),2)
ibmap = HDrive(150,100,100,100,(0,0,0),2)
dbmap = HDrive(250,100,100,100,(0,0,0),2)
i1 = HDrive(350,100,100,100,(0,0,0),2)
i2 = HDrive(450,100,100,100,(0,0,0),2)
d1 = HDrive(550,100,100,100,(0,0,0),2)
d2 = HDrive(650,100,100,100,(0,0,0),2)
d3 = HDrive(750,100,100,100,(0,0,0),2)


# Helper Functions
def addText(mytext, t_dest, f_color, f_size):
    font = pygame.font.SysFont(None, f_size)
    font_final = font.render(mytext, True, f_color)
    screen.blit(font_final, t_dest)

screen.fill((255, 255, 255))


# Event list for simulation
def sim_events(c):
    match c:

        case 0:
            addText("Hello! Let's learn about the parts of a simple file system and how they interact together.", (100, 335),
            (0, 0, 0), 25)

        case 1:
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1000, 1000), 0)
            pygame.draw.rect(screen, (137, 194, 194), (50, 100, 100, 100), 0) #SUPERBLOCK
            pygame.draw.rect(screen, (243, 247, 193), (550, 100, 300, 100), 0) #DATA
            pygame.draw.rect(screen, (188, 120, 158), (350, 100, 200, 100), 0) #INODE
            pygame.draw.rect(screen, (245, 162, 162), (150, 100, 100, 100), 0) #IBMAP
            pygame.draw.rect(screen, (183, 159, 241), (250, 100, 100, 100), 0) #DBMAP
            addText("The data structures of a simple file system are divided into blocks of the same size.", (100, 335), (0, 0, 0), 25)
            addText("For this simulation we will use the size of 4KB.", (250, 365), (0, 0, 0), 25)

        case 2:
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (255, 255, 255), (50, 100, 800, 100), 0)

            pygame.draw.rect(screen, (137, 194, 194), (50, 100, 100, 100), 0)
            addText("The first block is typically reserved for the superblock which creates the ", (150, 335), (0, 0, 0), 25)
            addText("system and it's components, and contains information about the particular file system.", (100, 365), (0, 0, 0), 25)

        case 3:
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (255, 255, 255), (50, 100, 100, 100), 0)
            pygame.draw.rect(screen, (243, 247, 193), (550, 100, 300, 100), 0)
            addText("Most space in a file system should be reserved for user data.", (220, 335), (0, 0, 0), 25)
            addText("We call this the data region. It is where the files are stored by 0's and 1's.", (175, 365), (0, 0, 0), 25)

        case 4:
            pygame.draw.rect(screen, (255, 255, 255), (550, 100, 300, 100), 0)
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (188, 120, 158), (350, 100, 200, 100), 0)
            pygame.draw.rect(screen, (0, 0, 0), (50, 330, 100, 40), 2)
            pygame.draw.rect(screen, (0, 0, 0), (80, 300, 40, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 300, 100, 100), 2)
            addText("Inodes are stored in the inode table on the disk. Inodes store metadata,", (220, 300), (0, 0, 0), 25)
            addText("which is where data about a file is stored. This include the name, timestamp,", (220, 330),(0, 0, 0), 25)
            addText("file size, location of which data block the file is in, etc.", (220, 360),(0, 0, 0), 25)
            addText("INODE TABLE", (55, 280), (0, 0, 0), 20)
            addText("0      1       2", (65, 310), (0, 0, 0), 20)
            addText("3      4       5", (65, 347), (0, 0, 0), 20)
            addText("6      7       8", (65, 382), (0, 0, 0), 20)


        case 5:
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (255, 255, 255), (350, 100, 200, 100), 0)
            pygame.draw.rect(screen, (245, 162, 162), (150, 100, 100, 100), 0)
            pygame.draw.rect(screen, (183, 159, 241), (250, 100, 100, 100), 0)

            addText("File systems use different  allocation structures to track whether inodes or data blocks are free or allocated.",  (45, 335),(0, 0, 0), 24)
            addText("For this simulation we will use the bitmap structure, one for both data and inodes.",  (125, 365),(0, 0, 0), 25)
        case 6:
            pygame.draw.rect(screen, (255, 255, 255), (150, 100, 200, 100), 0)
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (0, 0, 0), (50, 250, 50, 450), 2)
            pygame.draw.rect(screen, (0, 0, 0), (100, 250, 50, 450), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 350, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 300, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 500, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 550, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 600, 100, 100), 2)
            pygame.draw.rect(screen, (245, 162, 162), (150, 100, 100, 100), 0)

            addText("The inode bitmap keeps track to see which block is free or in use ", (220, 335),(0, 0, 0), 25)
            addText("for inodes as well as where to put a file.", (220, 365),(0, 0, 0), 25)
            addText("0       0", (70, 270), (0, 0, 0), 30)
            addText("1       0", (70, 320), (0, 0, 0), 30)
            addText("2       0", (70, 370), (0, 0, 0), 30)
            addText("3       0", (70, 420), (0, 0, 0), 30)
            addText("4       0", (70, 470), (0, 0, 0), 30)
            addText("5       0", (70, 520), (0, 0, 0), 30)
            addText("6       0", (70, 570), (0, 0, 0), 30)
            addText("7       0", (70, 620), (0, 0, 0), 30)
            addText("8       0", (70, 670), (0, 0, 0), 30)



        case 7:
            pygame.draw.rect(screen, (255, 255, 255), (150, 100, 200, 100), 0)
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (183, 159, 241), (250, 100, 100, 100), 0)

            addText("The data bitmap labels each space of the hard drive, and uses 0's and 1's", (210, 335),(0, 0, 0), 25)
            addText("to tell if a space is free or not. From the RAM it takes the 0's and 1's", (210, 365),(0, 0, 0), 25)
            addText("and adds it to the hard drive in the data blocks", (210, 395),(0, 0, 0), 25)
            pygame.draw.rect(screen, (0, 0, 0), (50, 250, 50, 400), 2)
            pygame.draw.rect(screen, (0, 0, 0), (100, 250, 50, 400), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 350, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 300, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 500, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 550, 100, 100), 2)
            addText("0       0", (70, 270), (0, 0, 0), 30)
            addText("1       0", (70, 320), (0, 0, 0), 30)
            addText("2       0", (70, 370), (0, 0, 0), 30)
            addText("3       0", (70, 420), (0, 0, 0), 30)
            addText("4       0", (70, 470), (0, 0, 0), 30)
            addText("5       0", (70, 520), (0, 0, 0), 30)
            addText("6       0", (70, 570), (0, 0, 0), 30)
            addText("7       0", (70, 620), (0, 0, 0), 30)

        case 8:
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (255, 255, 255), (250, 100, 100, 100), 0)
            addText("Let's see an example with this simple file.",(270, 330), (0, 0, 0), 25)
            pygame.draw.rect(screen, (0, 0, 0), (290, 365, 300, 200), 2)
            pygame.draw.rect(screen, (0, 0, 0), (290, 365, 80, 30), 2)

            pygame.draw.rect(screen, (0, 0, 0), (290, 365, 300, 120), 2)

            addText("HELLO.txt",(300, 370), (0, 0, 0), 20)
            addText("owner: lil circle",(345, 400), (0, 0, 0), 15)
            addText("size: 4KB",(345, 420), (0, 0, 0), 15)
            addText("ctime: 12:01:03",(345, 440), (0, 0, 0), 15)
            addText("mtime: 04:06:23",(345, 460), (0, 0, 0), 15)
            addText("time: 04:06:25",(450, 400), (0, 0, 0), 15)
            addText("blocks: 1",(450, 420), (0, 0, 0), 15)
            addText("block: 5",(450, 440), (0, 0, 0), 15)

            addText("HELLO",(370, 500), (0, 0, 0), 60)

        case 9:
            pygame.draw.rect(screen, (255, 255, 255), (0, 200, 1000, 1000), 0)
            pygame.draw.rect(screen, (0, 0, 0), (200, 250, 50, 450), 2) ##INODE BITMAP
            pygame.draw.rect(screen, (0, 0, 0), (250, 250, 50, 450), 2)
            pygame.draw.rect(screen, (0, 0, 0), (200, 350, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (200, 300, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (200, 500, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (200, 550, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (200, 600, 100, 100), 2)
            addText("INODE BITMAP", (200, 230), (0, 0, 0), 20)
            addText("0       1", (220, 270), (0, 0, 0), 30)
            addText("1       0", (220, 320), (0, 0, 0), 30)
            addText("2       0", (220, 370), (0, 0, 0), 30)
            addText("3       0", (220, 420), (0, 0, 0), 30)
            addText("4       1", (220, 470), (0, 0, 0), 30)
            addText("5       0", (220, 520), (0, 0, 0), 30)
            addText("6       1", (220, 570), (0, 0, 0), 30)
            addText("7       0", (220, 620), (0, 0, 0), 30)
            addText("8       0", (220, 670), (0, 0, 0), 30)

            pygame.draw.rect(screen, (0, 0, 0), (50, 250, 50, 400), 2) ##DATA BITMAP
            pygame.draw.rect(screen, (0, 0, 0), (100, 250, 50, 400), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 350, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 300, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 500, 100, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (50, 550, 100, 100), 2)
            addText("DATA BITMAP", (55, 230), (0, 0, 0), 20)
            addText("0       1", (70, 270), (0, 0, 0), 30)
            addText("1       1", (70, 320), (0, 0, 0), 30)
            addText("2       1", (70, 370), (0, 0, 0), 30)
            addText("3       1", (70, 420), (0, 0, 0), 30)
            addText("4       1", (70, 470), (0, 0, 0), 30)
            addText("5       0", (70, 520), (0, 0, 0), 30)
            addText("6       0", (70, 570), (0, 0, 0), 30)
            addText("7       0", (70, 620), (0, 0, 0), 30)

            pygame.draw.rect(screen, (0, 0, 0), (330, 280, 100, 35), 2) #INODE TABLE
            pygame.draw.rect(screen, (0, 0, 0), (360, 250, 40, 100), 2)
            pygame.draw.rect(screen, (0, 0, 0), (330, 250, 100, 100), 2)
            addText("INODE TABLE", (340, 230), (0, 0, 0), 20)
            addText("0      1       2", (345, 263), (0, 0, 0), 20)
            addText("3      4       5", (345, 295), (0, 0, 0), 20)
            addText("6      7       8", (345, 325), (0, 0, 0), 20)

            pygame.draw.rect(screen, (0, 0, 0), (550, 500, 300, 200), 2) #SAMPLE FILE
            pygame.draw.rect(screen, (0, 0, 0), (550, 500, 80, 30), 2)
            pygame.draw.rect(screen, (0, 0, 0), (550, 500, 300, 140), 2)
            addText("HELLO.txt", (555, 510), (0, 0, 0), 20)
            addText("owner: lil circle", (600, 550), (0, 0, 0), 15)
            addText("size: 4KB", (600, 570), (0, 0, 0), 15)
            addText("ctime: 12:01:03", (600, 590), (0, 0, 0), 15)
            addText("mtime: 04:06:23", (600, 610), (0, 0, 0), 15)
            addText("time: 04:06:25", (745, 550), (0, 0, 0), 15)
            addText("blocks: 1", (745, 570), (0, 0, 0), 15)
            addText("block: 5", (745, 590), (0, 0, 0), 15)
            addText("HELLO", (640, 650), (0, 0, 0), 60)
            addText("As mentioned before, the inode contains all the information", (380, 380), (0, 0, 0), 25)
            addText("about the file also known as the metadata. ", (380, 405), (0, 0, 0), 25)


        case 10:
            pygame.draw.rect(screen, (145, 245, 255), (550, 500, 300, 140), 2)


        case 11:
            pygame.draw.rect(screen, (183, 159, 241), (150, 100, 100, 100), 0)
            pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)

            addText("The inode bitmap tells us which inode is free or in use", (380, 380), (0, 0, 0), 25)
            addText("with it's corresponding i-number.", (380, 405), (0, 0, 0), 25)
            pygame.draw.rect(screen, (183, 159, 241), (200, 500, 100, 51), 3)

        case 12:
            pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)
            addText("Let's save the metadata in inode 5", (380, 380), (0, 0, 0), 25)

        case 13:
            pygame.draw.rect(screen, (188, 120, 158), (350, 100, 100, 100), 0)
            pygame.draw.rect(screen, (188, 120, 158), (400, 280, 32, 34), 3)

        case 14:
         pygame.draw.rect(screen, (145, 245, 255), (550, 500, 300, 140), 2)
         pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)
         addText("The bit will change from 0 to 1 to show that it's occupied.", (380, 380), (0, 0, 0), 25)

        case 15:
            pygame.draw.rect(screen, (255, 255, 255), (252, 502, 45, 45), 0)
            addText("        1", (220, 520), (0, 0, 0), 30)
        case 16:
            pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)
            pygame.draw.rect(screen, (255, 255, 255), (350, 100, 100, 100), 0)
            pygame.draw.rect(screen, (0, 0, 0), (400, 280, 32, 34), 3)
            pygame.draw.rect(screen, (0, 0, 0), (200, 500, 100, 51), 3)
            pygame.draw.rect(screen, (255, 255, 255), (150, 100, 200, 100), 0)
            pygame.draw.rect(screen, (0, 0, 0), (550, 500, 300, 140), 2)
            addText("A simple approach to refer to where data blocks are is to have", (380, 380), (0, 0, 0), 25)
            addText("a direct pointer inside each inode, with each pointer referring ", (380, 405), (0, 0, 0), 25)
            addText("to one data block that belongs to the file.", (380, 430), (0, 0, 0), 25)

        case 17:
            pygame.draw.rect(screen, (255, 255, 255), (350, 100, 100, 100), 0)
            pygame.draw.rect(screen, (181, 142, 188), (550, 640, 300, 60), 2)
            pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)

            addText("Let's say inode 5 directly points to block 5.", (380, 380), (0, 0, 0), 25)

        case 18:
            pygame.draw.rect(screen, (183, 159, 241), (250, 100, 100, 100), 0)
            pygame.draw.rect(screen, (183, 159, 241), (50, 502, 100, 47), 3)
            pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)
            addText("Checking the databitmap it shows that block 5 is free.", (380, 380), (0, 0, 0), 25)



        case 19:
            pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)
            addText("As you can see the 0 change to 1 to show it's occupied.", (380, 380), (0, 0, 0), 25)
            pygame.draw.rect(screen, (255, 255, 255), (103, 505, 40, 40), 0)
            addText("            1", (50, 520), (0, 0, 0), 30)
        case 20:
            pygame.draw.rect(screen, (255, 255, 255), (350, 370, 700, 100), 0)
            addText("The data is then transferred onto the data block.", (380, 380), (0, 0, 0), 25)
            addText("01001000 01100101", (562, 160), (0, 0, 0), 14)
            addText("01101100 01101100", (562, 168), (0, 0, 0), 14)
            addText("01101111", (580, 176), (0, 0, 0), 15)

        case 21:
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1000, 1000), 0)
            addText("THE END!", (350, 335),(0, 0, 0), 60)

        case _:
            print("Simulation is over")


# Run Simulation
# Running loop
running = True
counter = 0
while running:
    # looks for inputs: keyboard presses, mouse clicks, etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # checking if key "->" was pressed
            if event.key == pygame.K_RIGHT:
                sim_events(counter)
                counter += 1
#Draw Elements
    sblock.draw()
    ibmap.draw()
    dbmap.draw()
    i1.draw()
    i2.draw()
    d1.draw()
    d2.draw()
    d3.draw()


    # Static screen elements
    addText("Caroline Conrad CIS 321- Operating Systems", (275, 15), (0, 0, 0), 25)
    addText("SIMPLE FILE SYSTEM", (275, 65), (0, 0, 0), 50)
    addText("SUPER", (65, 130), (0, 0, 0), 30)
    addText("BLOCK", (65, 150), (0, 0, 0), 30)
    addText("INODE", (170, 130), (0, 0, 0), 30)
    addText("BITMAP", (160, 150), (0, 0, 0), 30)
    addText("DATA", (275, 130), (0, 0, 0), 30)
    addText("BITMAP", (260, 150), (0, 0, 0), 30)
    addText("INODE", (370, 140), (0, 0, 0), 30)
    addText("INODE", (470, 140), (0, 0, 0), 30)
    addText("DATA", (575, 140), (0, 0, 0), 30)
    addText("DATA", (675, 140), (0, 0, 0), 30)
    addText("DATA", (775, 140), (0, 0, 0), 30)
    addText("4KB", (125, 185), (0, 0, 0), 15)
    addText("4KB", (225, 185), (0, 0, 0), 15)
    addText("4KB", (325, 185), (0, 0, 0), 15)
    addText("4KB", (425, 185), (0, 0, 0), 15)
    addText("4KB", (525, 185), (0, 0, 0), 15)
    addText("4KB", (625, 185), (0, 0, 0), 15)
    addText("4KB", (725, 185), (0, 0, 0), 15)
    addText("4KB", (825, 185), (0, 0, 0), 15)
    addText("0", (55, 180), (0, 0, 0), 25)
    addText("1", (155, 180), (0, 0, 0), 25)
    addText("2", (255, 180), (0, 0, 0), 25)
    addText("3", (355, 180), (0, 0, 0), 25)
    addText("4", (455, 180), (0, 0, 0), 25)
    addText("5", (555, 180), (0, 0, 0), 25)
    addText("6", (655, 180), (0, 0, 0), 25)
    addText("7", (755, 180), (0, 0, 0), 25)


    # Update the screen, go to the next frame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

