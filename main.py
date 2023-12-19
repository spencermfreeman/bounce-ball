from vpython import *

scene = canvas(title = "<b>Bouncy Ball</b>")

scene.camera.pos = vector(0,4,4)
floor = box (pos=vector(0,0,0), length=4, height=0.2, width=4, color=color.white)
ball = sphere (pos=vector(0,8,0), radius=1, color=color.orange)
ball.velocity = vector(0,-1,0)

dt = 0.01
t = 0

while t<10:
    rate (100)
    ball.pos.y = ball.pos.y + ball.velocity.y*dt
    if ball.pos.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
