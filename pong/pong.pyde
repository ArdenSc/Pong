screenX, screenY = 1280, 720
validKeys = [87, 83, 38, 40]

class Player():
    w, h = 16, 192
    velocity = 0
    def __init__(self, x, y):
        self.x, self.y = x - self.w / 2, y - self.h / 2
    def move(self):
        self.y += self.velocity
        if (self.y < 0):
            self.y = 0
        if (self.y + self.h > screenY):
            self.y = screenY - self.h
    def display(self):
        fill(0)
        noStroke()
        rect(self.x, self.y, self.w, self.h)
        
        
class Ball():
    speed = 6
    radius = 15
    x, y, xDir, yDir= screenX/2, screenY/2, 1, 1
    def move(self):
        self.x = self.x + (self.speed * self.xDir)
        self.y = self.y + (self.speed * self.yDir)
    def display(self):
        fill(255, 0, 0)
        stroke(0)
        circle(self.x, self.y, self.radius * 2)
    def collisionCheck(self):
        if (self.y + self.radius >= screenY or self.y <= self.radius):
            self.yDir *= -1
            return True
        for player in players:
            edgeX, edgeY = self.x, self.y
            if (self.x < player.x):
                edgeX = player.x
            elif (self.x > player.x + player.w):
                edgeX = player.x + player.w
            if (self.y < player.y):
                edgeY = player.y
            elif (self.y > player.y + player.h):
                edgeY = player.y + player.h
            distX, distY = self.x - edgeX, self.y - edgeY
            if (sqrt((distX ** 2) + (distY ** 2)) <= ball.radius):
                if ((edgeX == player.x and edgeY == self.y) \
                        or (edgeX == player.x + player.w and edgeY == self.y)):
                    print("hit x")
                    self.xDir *= -1
                    return True
                elif ((edgeX == self.x and edgeY == player.y) \
                    or (edgeX == self.x and edgeY == player.y + player.h)):
                    print("hit y")
                    self.yDir *= -1
                    return True
                else:
                    print("hit corner")
                    self.xDir *= -1
                    self.yDir *= -1
                    return True

def setup():
    global players, ball, gamestate, keysPressed
    size(screenX, screenY)
    players = []
    keysPressed = []
    players.append(Player(32, screenY/2))
    players.append(Player(screenX - 32, screenY/2))
    ball = Ball()
    gamestate = 0
    
def draw():
    global ball, players
    background(255)
    if "w" in keysPressed and not "s" in keysPressed:
        players[0].velocity = -4
    elif "s" in keysPressed and not "w" in keysPressed:
        players[0].velocity = 4
    else:
        players[0].velocity = 0
    if "up" in keysPressed and not "down" in keysPressed:
        players[1].velocity = -4
    elif "down" in keysPressed and not "up" in keysPressed:
        players[1].velocity = 4
    else:
        players[1].velocity = 0
    for player in players:
        player.display()
        player.move()
    ball.display()
    ball.move()
    if ball.collisionCheck():
        ball.move()
    
def convertKey(n):
    return "w" if n == 87 else "s" if n == 83 else "up" if n == 38 else "down" if n == 40 else 0
        
def keyPressed():
    if not convertKey(keyCode) in keysPressed and keyCode in validKeys:
        keysPressed.append(convertKey(keyCode))
    
def keyReleased():
    if keyCode in validKeys:
        keysPressed.remove(convertKey(keyCode))
