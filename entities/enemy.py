import pygame
import random
from core.vector2 import Vector2
from core.collider import CircleCollider


class Enemy:
    def __init__(self, x, y, radius=20):
        self.position = Vector2(x, y)
        self.collider = CircleCollider(x, y, radius)
        self.collider.position = self.position

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (200, 60, 60),
            (int(self.position.x), int(self.position.y)),
            self.collider.radius
        )


def spawn_enemies(num, width, height, obstacles, min_radius=15, max_radius=30, max_attempts=30):
    enemies = []

    for _ in range(num):
        for attempt in range(max_attempts):

            radius = random.randint(min_radius, max_radius)

            x = random.randint(radius, width - radius)
            y = random.randint(radius, height - radius)

            new_enemy = Enemy(x, y, radius)

            collision = False
            for ob in obstacles:
                diff = new_enemy.position.sub(ob.collider.position)
                dist = diff.length()
                min_dist = radius + ob.collider.radius

                if dist < min_dist:
                    collision = True
                    break

            if not collision:
                enemies.append(new_enemy)
                break

    return enemies

