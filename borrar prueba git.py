#!/usr/bin/env python3
"""
Simple Pong game using pygame.

Controls:
- Move left paddle with the mouse (move the mouse vertically).
- Or use arrow keys Up and Down to move left paddle (keys override mouse while held).
- Press Esc or close window to quit.

The right paddle is a simple computer AI that follows the ball.
Includes bouncing ball, scoreboard, and collision detection for paddles and walls.
"""

import pygame
import random
import sys

# --- Configuration ---
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

PADDLE_WIDTH = 12
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6

BALL_SIZE = 14
BALL_START_SPEED = 5
BALL_SPEED_INCREMENT = 0.3
BALL_MAX_SPEED = 12

AI_SPEED = 4.0  # max speed the computer paddle moves per frame

SCORE_FONT_SIZE = 48
SCORE_MARGIN_TOP = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Pygame init ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, SCORE_FONT_SIZE)

# --- Game objects ---
left_paddle = pygame.Rect(30, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 30 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect((SCREEN_WIDTH - BALL_SIZE) // 2, (SCREEN_HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)

# Ball movement is stored as floats for smoothness
ball_speed_x = BALL_START_SPEED * random.choice((1, -1))
ball_speed_y = random.uniform(-3, 3)

score_left = 0
score_right = 0

# Input state
move_up = False
move_down = False

def reset_ball(towards_right=True):
    global ball, ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    # Give a slightly randomized angle
    angle = random.uniform(-0.5, 0.5)  # radians-ish for y component
    direction = 1 if towards_right else -1
    speed = BALL_START_SPEED
    ball_speed_x = direction * speed
    ball_speed_y = angle * speed

def clamp_paddle(p):
    if p.top < 0:
        p.top = 0
    if p.bottom > SCREEN_HEIGHT:
        p.bottom = SCREEN_HEIGHT

def draw():
    screen.fill(BLACK)
    # center line
    for y in range(0, SCREEN_HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH//2 - 1, y, 2, 10))

    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Score
    score_surf = font.render(f"{score_left}    {score_right}", True, WHITE)
    score_rect = score_surf.get_rect(center=(SCREEN_WIDTH//2, SCORE_MARGIN_TOP + SCORE_FONT_SIZE//2))
    screen.blit(score_surf, score_rect)

    pygame.display.flip()

def ball_collide_paddle(paddle: pygame.Rect):
    # Adjust ball.x so next frame isn't stuck inside paddle
    if ball_speed_x < 0:
        # moving left, collided with left paddle
        ball.left = paddle.right
    else:
        # moving right, collided with right paddle
        ball.right = paddle.left

def main():
    global move_up, move_down
    global ball_speed_x, ball_speed_y, score_left, score_right

    reset_ball(towards_right=random.choice((True, False)))

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds passed this frame (unused but handy)
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    move_up = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
            elif event.type == pygame.MOUSEMOTION:
                # We'll use the mouse Y as a control unless the arrow keys are pressed.
                mx, my = event.pos
                # center the paddle on mouse y unless keys pressed
                if not (move_up or move_down):
                    left_paddle.centery = my
                    clamp_paddle(left_paddle)

        # --- Player paddle movement (keyboard) ---
        if move_up:
            left_paddle.y -= PADDLE_SPEED
            clamp_paddle(left_paddle)
        elif move_down:
            left_paddle.y += PADDLE_SPEED
            clamp_paddle(left_paddle)

        # --- Computer AI for right paddle ---
        # Simple follow-the-ball with speed cap
        if right_paddle.centery < ball.centery:
            right_paddle.y += min(AI_SPEED, ball.centery - right_paddle.centery)
        elif right_paddle.centery > ball.centery:
            right_paddle.y -= min(AI_SPEED, right_paddle.centery - ball.centery)
        clamp_paddle(right_paddle)

        # --- Move the ball ---
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # --- Collisions with top/bottom walls ---
        if ball.top <= 0:
            ball.top = 0
            ball_speed_y = -ball_speed_y
        if ball.bottom >= SCREEN_HEIGHT:
            ball.bottom = SCREEN_HEIGHT
            ball_speed_y = -ball_speed_y

        # --- Collisions with paddles ---
        if ball.colliderect(left_paddle) and ball_speed_x < 0:
            # reflect horizontally, add some vertical change based on where it hit the paddle
            ball_collide_paddle(left_paddle)
            ball_speed_x = -ball_speed_x
            # influence y velocity by paddle hit position
            offset = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2)
            ball_speed_y += offset * 3.0
            # increase speed slightly
            sign = 1 if ball_speed_x > 0 else -1
            new_speed = min(abs(ball_speed_x) + BALL_SPEED_INCREMENT, BALL_MAX_SPEED)
            ball_speed_x = sign * new_speed

        if ball.colliderect(right_paddle) and ball_speed_x > 0:
            ball_collide_paddle(right_paddle)
            ball_speed_x = -ball_speed_x
            offset = (ball.centery - right_paddle.centery) / (PADDLE_HEIGHT / 2)
            ball_speed_y += offset * 3.0
            sign = 1 if ball_speed_x > 0 else -1
            new_speed = min(abs(ball_speed_x) + BALL_SPEED_INCREMENT, BALL_MAX_SPEED)
            ball_speed_x = sign * new_speed

        # --- Score handling ---
        if ball.left <= 0:
            # right player scores
            score_right += 1
            reset_ball(towards_right=False)  # serve towards left (loser side), but you can invert
            # small pause
            pygame.time.delay(300)
        elif ball.right >= SCREEN_WIDTH:
            score_left += 1
            reset_ball(towards_right=True)
            pygame.time.delay(300)

        # --- Draw everything ---
        draw()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()