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
    collidingWithPlayer = False
    x, y, xDir, yDir = screenX/2, screenY/2, 1, 1

    def move(self):
        for i in range(self.speed):
            self.x = self.x + (self.xDir)
            self.y = self.y + (self.yDir)
            if self.collisionCheck():
                break

    def display(self):
        fill(255, 0, 0)
        stroke(0)
        circle(self.x, self.y, self.radius * 2)

    def collisionCheck(self):
        if (self.y + self.radius >= screenY or self.y <= self.radius):
            self.yDir *= -1
            return True
        for player in players:
            edge = {"x": "middle", "y": "middle"}
            edgeX, edgeY = self.x, self.y
            if (self.x < player.x):
                edge["x"] = "left"
                edgeX = player.x
            elif (self.x > player.x + player.w):
                edge["x"] = "right"
                edgeX = player.x + player.w
            if (self.y < player.y):
                edge["y"] = "top"
                edgeY = player.y
            elif (self.y > player.y + player.h):
                edge["y"] = "bottom"
                edgeY = player.y + player.h
            distX, distY = self.x - edgeX, self.y - edgeY
            if (sqrt((distX ** 2) + (distY ** 2)) <= ball.radius):
                print(edge)
                if (edge["x"] != "middle" and edge["y"] == "middle"): 
                    self.xDir *= -1
                    return True
                elif (edge["x"] == "middle" and edge["y"] != "middle"):
                    self.yDir *= -1
                    self.collidingWithPlayer = True
                    return True
                elif (edge["x"] == "middle" and edge["y"] == "middle"):
                    print("this really shouldnt happen")
                    print(edgeX, edgeY)
                    print(distX, distY)
                    print(sqrt((distX ** 2) + (distY ** 2)))
                    exit()
                else:
                    if (edge["x"] == "left" and edge["y"] == "top"):
                        self.xDir = -1
                    elif (edge["x"] == "right" and edge["y"] == "top"):
                        self.xDir = 1
                    elif (edge["x"] == "right" and edge["y"] == "bottom"):
                        self.xDir = 1
                    elif (edge["x"] == "left" and edge["y"] == "bottom"):
                        self.xDir = -1
                    if (player.velocity == 6):
                        
                    self.collidingWithPlayer = True
                    return True
            else:
                self.collidingWithPlayer = False


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
    if "w" in keysPressed and "s" not in keysPressed:
        players[0].velocity = -6
    elif "s" in keysPressed and "w" not in keysPressed:
        players[0].velocity = 6
    else:
        players[0].velocity = 0
    if "up" in keysPressed and "down" not in keysPressed:
        players[1].velocity = -6
    elif "down" in keysPressed and "up" not in keysPressed:
        players[1].velocity = 6
    else:
        players[1].velocity = 0
    if ball.collidingWithPlayer:
        for player in players:
            player.velocity = 0
    for player in players:
        player.display()
        player.move()
    ball.display()
    ball.move()


def convertKey(n):
    return "w" if n == 87 else \
        "s" if n == 83 else \
        "up" if n == 38 else \
        "down" if n == 40 else 0


def keyPressed():
    if convertKey(keyCode) not in keysPressed and keyCode in validKeys:
        keysPressed.append(convertKey(keyCode))


def keyReleased():
    if keyCode in validKeys:
        keysPressed.remove(convertKey(keyCode))
