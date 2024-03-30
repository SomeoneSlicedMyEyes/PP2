import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    eraser = False
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    eraser = not eraser
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    if eraser:
                        points = []
                    else:
                        points.append(event.pos)
                elif event.button == 3: # right click
                    if eraser:
                        points = []
                    else:
                        points = points[:-1]
            
        screen.fill((0, 0, 0))
        
        drawShapes(screen, points, radius, mode, eraser)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawShapes(screen, points, radius, color_mode, eraser):
    for i in range(len(points) - 1):
        if not eraser:
            drawLineBetween(screen, points[i], points[i + 1], radius, color_mode)
        else:
            pygame.draw.circle(screen, (0, 0, 0), points[i], radius)
    if len(points) > 1 and not eraser:
        pygame.draw.circle(screen, (0, 0, 0), points[-1], radius)
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), point, radius - 2)

def drawLineBetween(screen, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * start[0] - 256))
    c2 = max(0, min(255, 2 * start[0]))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

if __name__ == "__main__":
    main()
