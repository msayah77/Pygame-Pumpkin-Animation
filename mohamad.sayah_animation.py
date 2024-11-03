import pygame

def main():
    pygame.init()
    
    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move the Pumpkin")
    
    # custom background image
    background = pygame.image.load("Backround.png").convert()
    background = pygame.transform.scale(background, screen.get_size())  
    
    # Load an pumpkin image
    pumpkin = pygame.image.load("pumpkin.png").convert_alpha()
    pumpkin = pygame.transform.scale(pumpkin, (50, 50))  
    
    # start at the center of the screen
    pumpkin_x = screen.get_width() - 50  
    pumpkin_y = 200
    pumpkin_speed_x = -5  
    pumpkin_speed_y = 3   
    
    # variables
    clock = pygame.time.Clock()
    keepGoing = True
    
    
    while keepGoing:
        clock.tick(30)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    pumpkin_x = screen.get_width() - 50  
                    pumpkin_y = 200  
        
        
        pumpkin_x += pumpkin_speed_x  
        pumpkin_y += pumpkin_speed_y  

        
        if pumpkin_y <= 0:  
            pumpkin_y = 0
            pumpkin_speed_y = -pumpkin_speed_y  
        elif pumpkin_y >= screen.get_height() - 50:  
            pumpkin_y = screen.get_height() - 50
            pumpkin_speed_y = -pumpkin_speed_y  
        
        
        if pumpkin_x < -50:  
            pumpkin_x = screen.get_width()
            pumpkin_y = 200  
        
        # Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(pumpkin, (pumpkin_x, pumpkin_y))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
