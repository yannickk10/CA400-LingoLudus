import pygame
import sys

def draw_button(button_colour, screen, width, height, mouse_pos):
	if width/2-150 <= mouse[0] <= width/2+150 and height <= mouse[1] <= height+40:
		pygame.draw.rect(screen,grey,[width/2-150,height,300,40])
		
	else:
		pygame.draw.rect(screen,black,[width/2-150,height,300,40])


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
	screen.fill(white)
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade

	# Draw Buttons
	button_height = 40
	i = 0
	while i <= 7:
		draw_button(grey, screen, width, button_height, mouse)
		button_height += 120
		i += 1
	
	# superimposing the text onto our button
	screen.blit(sel_lang , (width/2-150,45))
	screen.blit(new_game , (width/2-150,165))
	screen.blit(load_game , (width/2-150,285))
	screen.blit(view_stats , (width/2-150,405))
	screen.blit(sel_lang , (width/2-150,525))
	screen.blit(sel_lang , (width/2-150,645))

	
	# updates the frames of the game
	pygame.display.update()
