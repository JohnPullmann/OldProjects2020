import time, pygame, sys, random
pygame.init()
fps = pygame.time.Clock()
time = 0
width = 800
height = 600
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((width, height))
game_over = False
# player
player_position = [400, 320]
player_size = [40, 40]
lastdirection = 'right'
direction = 'right'
directions = ['right']
food_p = {}
food_n = 0
food_n_all = 0
eaten = 0
body = []
class body_m:
    def __init__(self, position, direction, name, d_n):
        self.position = position
        self.direction = direction
        self.name = name
        self.d_n = d_n
b1 = body_m(player_position, directions[-1], 'b1', -1)
body.append(b1)
def col_wall(player_position, width, height, direction, game_over, body):
    if len(body) > 1:
        if direction == 'left':
            if player_position[0] < 0:
                pygame.quit()
        if direction == 'right':
            if player_position[0] >= width:
                pygame.quit()
        if direction == 'up':
            if player_position[1] < 0:
                pygame.quit()
        if direction == 'down':
            if player_position[1] >= height:
                pygame.quit()
    else:
        if direction == 'left':
            if player_position[0] - 40 < 0:
                pygame.quit()
        if direction == 'right':
            if player_position[0] + 40 >= width:
                pygame.quit()
        if direction == 'up':
            if player_position[1] - 40 < 0:
                pygame.quit()
        if direction == 'down':
            if player_position[1] + 40 >= height:
                pygame.quit()
    return game_over
while game_over == False:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and lastdirection != 'right':
                direction = 'left'
            if event.key == pygame.K_RIGHT and lastdirection != 'left':
                direction = 'right'
            if event.key == pygame.K_UP and lastdirection != 'down':
                direction = 'up'
            if event.key == pygame.K_DOWN and lastdirection != 'up':
                direction = 'down'
    if time > 15:
        directions.append(direction)
    for x in body:
        if x.name == 'b1' :
            x.position = body[0].position
            x.direction = directions[-1]
    for x in body:
        if x.name != 'b1':
            x.direction = directions[x.d_n]
    for x in body:
        if time > 15:
            if x.direction == 'left':
                game_over = col_wall(b1.position, width, height, direction, game_over, body)
                x.position[0] -= 40
            if x.direction == 'right':
                game_over = col_wall(b1.position, width, height, direction, game_over, body)
                x.position[0] += 40
            if x.direction == 'up':
                game_over = col_wall(b1.position, width, height, direction, game_over, body)
                x.position[1] -= 40
            if x.direction == 'down':
                game_over = col_wall(b1.position, width, height, direction, game_over, body)
                x.position[1] += 40
    if time > 15:
        time = 0
    for x in body:
        if x.name != 'b1':
            if b1.position == x.position:
                pygame.quit()
    if food_n == 0:
        food_p[str(food_n_all)] = (random.randint(0, 19) * 40, random.randint(0, 14) * 40)
        food_n = 1
        food_n_all += 1
    for key, value in food_p.items():
        pygame.draw.rect(screen, (255, 0, 0), (value, (40, 40)))
    for key, value in food_p.items():
        if b1.position[0] == value[0] and b1.position[1] == value[1]:
            food_n = 0
            eaten += 1
            positionx = 0
            positiony = 0
            q = 'b'+str(eaten+1)
            if body[-1].direction == 'up':
                positiony = 40
            if body[-1].direction == 'down':
                positiony = -40
            if body[-1].direction == 'right':
                positionx = -40
            if body[-1].direction == 'left':
                positionx = 40
            q = body_m([body[-1].position[0]+ positionx,body[-1].position[1]+positiony], directions[-eaten-1],'b'+ str(eaten+1), -eaten-1)
            body.append(q)
    for x in body:
        if x.name != 'b1':
            if len(list(x.name)) == 2:
                color = int(list(x.name)[1]) * 5 +100
            else:
                color = int(list(x.name)[1]+list(x.name)[2]) * 5 + 100
            if color > 240:
                color = 250
            pygame.draw.rect(screen, (0, color, 0), (x.position, player_size))
        else:
            pygame.draw.rect(screen, (0, 100, 0), (x.position, player_size))
    if food_n == 0:
        food_p.clear()
    time += 1
    fps.tick(60)
    lastdirection = direction
    pygame.display.update()
print('GAME OVER')