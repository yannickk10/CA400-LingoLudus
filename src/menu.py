import pygame
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

background_image = pygame.image.load("src/images/LiLu_Logo.png").convert()

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font

sel_lang = smallfont.render('Select Language' , True , white)
new_game = smallfont.render('New Game' , True , white)
load_game = smallfont.render('Load Game' , True , white)
view_stats = smallfont.render('Select Language' , True , white)
sel_lang = smallfont.render('Select Language' , True , white)
sel_lang = smallfont.render('Select Language' , True , white)


while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
			#if the mouse is clicked on the
			# button the game is terminated
			if width/2 <= mouse[0] <= width/2+120 and height/2 <= mouse[1] <= height/2+40:
				pygame.quit()
				
	# fills the screen with a color
	screen.blit(background_image, [0,0])
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade

	# Draw Buttons
	button_height = 280
	i = 0
	while i <= 4:
		if (i % 2) == 0:
			draw_button(grey, screen, width, button_height, mouse,540)
			button_height += 120
		else:
			draw_button(grey, screen, width-480 , button_height, mouse,540)
			button_height += 120
		i += 1
	
	# superimposing the text onto our button
	screen.blit(load_game , (width/2-150,285))
	screen.blit(view_stats , (width/2-150,405))
	screen.blit(sel_lang , (width/2-150,525))
	screen.blit(sel_lang , (width/2-150,645))

	
	# updates the frames of the game
	pygame.display.update()
