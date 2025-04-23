import tkinter as tk
import random
import math

WIDTH, HEIGHT = 800, 600
HEPTAGON_RADIUS = 200
BALL_RADIUS = 10
NUM_BALLS = 20
GRAVITY = 0.5
FRICTION = 0.9
SPIN_SPEED = 0.05
COLORS = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'black']

class Ball:
    def __init__(self, x, y, vx, vy, radius, color, number):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.number = number

def create_heptagon_points(center_x, center_y, radius, angle):
    points = []
    for i in range(7):
        theta = 2 * math.pi * i / 7 + angle
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        points.append((x, y))
    return points

def point_in_heptagon(point, heptagon_points):
    x, y = point
    n = len(heptagon_points)
    inside = False
    p1x, p1y = heptagon_points[0]
    for i in range(n + 1):
        p2x, p2y = heptagon_points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def generate_random_point_in_heptagon(heptagon_points):
    while True:
        x = random.uniform(0, WIDTH)
        y = random.uniform(0, HEIGHT)
        if point_in_heptagon((x, y), heptagon_points):
            return x, y

def update_balls(balls, heptagon_points):
    for ball in balls:
        ball.x += ball.vx
        ball.y += ball.vy
        ball.vy += GRAVITY
        if not point_in_heptagon((ball.x, ball.y), heptagon_points):
            ball.vx *= -FRICTION
            ball.vy *= -FRICTION
        if ball.x - ball.radius < 0 or ball.x + ball.radius > WIDTH:
            ball.vx *= -FRICTION
        if ball.y - ball.radius < 0 or ball.y + ball.radius > HEIGHT:
            ball.vy *= -FRICTION

def draw_balls(canvas, balls):
    for ball in balls:
        canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                            ball.x + ball.radius, ball.y + ball.radius,
                            fill=ball.color)

def draw_heptagon(canvas, heptagon_points):
    for i in range(7):
        p1 = heptagon_points[i]
        p2 = heptagon_points[(i + 1) % 7]
        canvas.create_line(p1, p2, fill='black')

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    center_x, center_y = WIDTH // 2, HEIGHT // 2
    angle = 0

    balls = []
    for _ in range(NUM_BALLS):
        heptagon_points = create_heptagon_points(center_x, center_y, HEPTAGON_RADIUS, angle)
        x, y = generate_random_point_in_heptagon(heptagon_points)
        vx = random.uniform(-2, 2)
        vy = random.uniform(-2, 2)
        color = random.choice(COLORS)
        balls.append(Ball(x, y, vx, vy, BALL_RADIUS, color, _))

    def animate():
        nonlocal angle
        canvas.delete("all")
        angle += SPIN_SPEED
        heptagon_points = create_heptagon_points(center_x, center_y, HEPTAGON_RADIUS, angle)
        draw_heptagon(canvas, heptagon_points)
        update_balls(balls, heptagon_points)
        draw_balls(canvas, balls)
        root.after(30, animate)

    animate()
    root.mainloop()

if __name__ == "__main__":
    main()
