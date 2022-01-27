import pygame
import test as gt
import sys

def draw_button(button_colour, screen, width, height, mouse_pos, alt):
	if width/2-540 <= mouse[0] <= width/2+540 and height <= mouse[1] <= height+40:
		pygame.draw.rect(screen,grey,[width/2-150,height,alt,40])
		
	else:
		pygame.draw.rect(screen,black,[width/2-150,height,alt,40])


# initializing the constructor
pygame.init()

# screen resolution
res = (720,720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
white = (255,255,255)

red = (255,0,0)

# light shade of the button
grey = (170,170,170)

# dark shade of the button
black = (100,100,100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

pressed_keys = pygame.key.get_pressed()

background_image = pygame.image.load("images/LiLu_Logo.png").convert()

# defining a font
smallfont = pygame.font.SysFont('twcencondensedextra',30)
bigfont = pygame.font.SysFont('lucidafax',40)
print(pygame.font.get_fonts())

# rendering a text written in
# this font
main_menu = bigfont.render('Main menu' , True , red)
sel_lang = smallfont.render('Select Language' , True , white)
Game_sel = smallfont.render('Game Selection' , True , white)
new_game = smallfont.render('New Game' , True , white)
load_game = smallfont.render('Load Game' , True , white)
view_stats = smallfont.render('View Stats' , True , white)
quit_game = smallfont.render('Quit Game' , True , white)


while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
			#if the mouse is clicked on the
			# button the game is terminated

			if width/2+150 <= mouse[0] <=0 and 645 <= mouse[1] <= 640+40:
				pygame.quit()

			else:
				if width/2+150 <= mouse[0] <= 0 and 285 <= mouse[1] <= 320+40:
					gt.space_invaders()
				
	# fills the screen with a color
	screen.blit(background_image, [0,0])
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade

	# Draw Buttons
	button_height = 320
	i = 0
	while i <= 4:
		if (i % 2) == 0:
			draw_button(grey, screen, width, button_height, mouse,540)
			button_height += 160
		else:
			draw_button(grey, screen, width-480 , button_height, mouse,540)
			button_height += 160
		i += 1
	
	# superimposing the text onto our button
	screen.blit(main_menu , (width/2-110,250))
	screen.blit(new_game , (width/2-75,320))
	screen.blit(sel_lang , (width/2-105,480))
	screen.blit(quit_game , (width/2-75,640))

	
	# updates the frames of the game
	pygame.display.update()
