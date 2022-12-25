from Shape import shape
def viwe(oop,shape1=shape(),shape2=shape()):
    import pygame 
    pygame.init()
    print(shape1,shape2)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # set screen size
    clock = pygame.time.Clock()   
    w , h = pygame.display.get_surface().get_size()
    
    done = False 
    x=0
    y=0
    my_font = pygame.font.SysFont('Tahoma', 20)
    if(shape1.gettype()!=""):
        #shape color :
        s1_color1 = shape1.getcolor().split("(")[1].split(")")[0].split(",")
        color_text1=(int(s1_color1[0]),int(s1_color1[1]), int(s1_color1[2]))
        print(s1_color1)
        if(shape1.gettype()== "circle"):
            text_r = my_font.render(f'R1 : {str(shape1.getr())}', False, color_text1)
            text_p = my_font.render(f'Center1 : {str(shape1.getc())}', False, color_text1)
            text_area = my_font.render(f'Area1 : {str(int(shape1.area()))} m^2', False, color_text1)
            text_perimeter= my_font.render(f'Perimeter1 : {str(int(shape1.perimeter()))} m', False, color_text1)
            text_mabda1= my_font.render(f'Distance1 : {str(int(shape1.distance()))} m', False, color_text1)
        else:
            text_x = my_font.render(f'X1 : {str(shape1.getx())}', False, color_text1)
            text_y = my_font.render(f'Y1 : {str(shape1.gety())}', False, color_text1)
            text_p = my_font.render(f'Center1 : {str(shape1.getc())}', False, color_text1)
            text_area = my_font.render(f'Area1 : {str(int(shape1.area()))} m^2', False, color_text1)
            text_perimeter= my_font.render(f'Perimeter1 : {str(int(shape1.perimeter()))} m', False, color_text1)
            text_mabda1= my_font.render(f'Distance1 : {str(int(shape1.distance()))} m', False, color_text1)
    if(shape2.gettype()!=""):
        #shape color :
        s2_color1 = shape2.getcolor().split("(")[1].split(")")[0].split(",")
        color_text2 =(int(s2_color1[0]), int(s2_color1[1]), int(s2_color1[2]))
        if(shape2.gettype()== "circle"):
            text_r2 = my_font.render(f'R2 : {str(shape2.getr())}', False,color_text2 )
            text_p2 = my_font.render(f'Center2 : {str(shape2.getc())}', False, color_text2)
            text_area2 = my_font.render(f'Area2 : {str(int(shape2.area()))} m^2', False, color_text2)
            text_perimeter2= my_font.render(f'Perimeter2 : {str(int(shape2.perimeter()))} m', False, color_text2)
            text_mabda2= my_font.render(f'Distance2 : {str(int(shape2.distance()))} m', False, color_text2)
        else:
            text_x2 = my_font.render(f'X2 : {str(shape2.getx())}', False, color_text2)
            text_y2 = my_font.render(f'Y2 : {str(shape2.gety())}', False, color_text2)
            text_p2 = my_font.render(f'Center2 : {str(shape2.getc())}', False, color_text2)
            text_area2 = my_font.render(f'Area2 : {str(int(shape2.area()))} m^2', False, color_text2)
            text_perimeter2= my_font.render(f'Perimeter2 : {str(int(shape2.perimeter()))} m', False, color_text2)
            text_mabda2= my_font.render(f'Distance2 : {str(int(shape2.distance()))} m', False, color_text2)
        distance2s= my_font.render(f'Distance 1-2 :{str(int(shape1.distanceFrom(shape2)))} m', False, (0,0,0))
        isinside= my_font.render(f'in Side 1-2 : {str(shape1.isinside(shape2))}', False, (0,0,0))
            
    origin= my_font.render(f'Coordinate origin', False, (0,0,0))
            
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if event is quit
                done = True   
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # if event is keydown and key is escape
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key==1073741903:
                    x+=50
                if event.key==1073741904:
                    x-=50    
                if event.key==1073741905:
                    y+=50
                if event.key==1073741906:
                    y-=50 
        screen.fill((255, 255, 255)) # set screen color

        if(shape1.gettype()!=""):
            shape_color =(int(s1_color1[0]), int(s1_color1[1]), int(s1_color1[2]))
            if(shape1.gettype()== "circle"):
                pygame.draw.circle(screen, shape_color, (200+shape1.getc().getw()+x,h- shape1.getc().getz()+y), shape1.getr())
            else:
                rectangle3 = pygame.Rect(200 + (shape1.getc().getw()-(shape1.getx()/2)) +x, h- (shape1.getc().getz()+(shape1.gety()/2))+y, shape1.getx(), shape1.gety())
                pygame.draw.rect(screen, shape_color, rectangle3)    
        if(shape2.gettype()!=""):
            shape_color =(int(s2_color1[0]), int(s2_color1[1]), int(s2_color1[2]))
            if(shape2.gettype()== "circle"):
                pygame.draw.circle(screen, shape_color, (200+shape2.getc().getw()+x,h- shape2.getc().getz()+y), shape2.getr())
            else:
                rectangle2 = pygame.Rect(200 + (shape2.getc().getw()-(shape2.getx()/2)) +x, h- (shape2.getc().getz()+(shape2.gety()/2))+y, shape2.getx(), shape2.gety())
                pygame.draw.rect(screen, shape_color, rectangle2)
            pygame.draw.line(screen, (230, 230, 230), (200 +shape1.getc().getw()+x, h- shape1.getc().getz()+y), (200 +shape2.getc().getw()+x, h- shape2.getc().getz()+y), 3)
             
        pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, h), 3)
        pygame.draw.circle(screen, (0,0,0), (200+x,h+y), 5,4)
        if(shape1.gettype()!=""):
            if(shape1.gettype()== "circle"):
                screen.blit(text_r, (10,0))
                screen.blit(text_p, (10,20))
                screen.blit(text_area, (10,42))
                screen.blit(text_perimeter, (10,64))
                screen.blit(text_mabda1, (10,86))
            else:
                screen.blit(text_x, (10,0))
                screen.blit(text_y, (10,20))
                screen.blit(text_p, (10,42))
                screen.blit(text_area, (10,64))
                screen.blit(text_perimeter, (10,86))
                screen.blit(text_mabda1, (10,108))
        if(shape2.gettype()!=""):
            if(shape2.gettype()== "circle"):
                screen.blit(text_r2, (10,138))
                screen.blit(text_p2, (10,160))
                screen.blit(text_area2, (10,182))
                screen.blit(text_perimeter2, (10,204))
                screen.blit(text_mabda2, (10,226))
            else:
                screen.blit(text_x2, (10,138))
                screen.blit(text_y2, (10,160))
                screen.blit(text_p2, (10,182))
                screen.blit(text_area2, (10,204))
                screen.blit(text_perimeter2, (10,226))
                screen.blit(text_mabda2, (10,248))
            screen.blit(distance2s,(10,320))
            screen.blit(isinside,(10,350))

        screen.blit(origin,(210+x,h+y))
        pygame.display.flip() # update screen
        clock.tick(120) # set fps
    oop.show()
    if done :
        pygame.quit()
        
       
