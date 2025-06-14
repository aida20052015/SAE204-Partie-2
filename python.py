# fichier : generate_etoile.py (à placer à la racine de ton projet Symfony SAE204partie2)
import pygame
import math
import random
import os

# Initialisation de Pygame
pygame.init()

# Dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Étoile de Siemens")

# Dessine une étoile simple (version aléatoire possible)
def draw_star(surface):
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    outer_radius = random.randint(200, min(WIDTH, HEIGHT) // 2 - 20)
    inner_radius = random.randint(10, outer_radius // 4)
    num_spokes = random.choice([24, 36, 48, 60, 72])
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while sum(abs(c1 - c2) for c1, c2 in zip(color1, color2)) < 150:
        color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    angle_per_spoke = 2 * math.pi / num_spokes

    for i in range(num_spokes):
        color = color1 if i % 2 == 0 else color2
        x1 = center_x + outer_radius * math.cos(i * angle_per_spoke)
        y1 = center_y + outer_radius * math.sin(i * angle_per_spoke)
        x2 = center_x + outer_radius * math.cos((i + 1) * angle_per_spoke)
        y2 = center_y + outer_radius * math.sin((i + 1) * angle_per_spoke)
        x3 = center_x + inner_radius * math.cos((i + 1) * angle_per_spoke)
        y3 = center_y + inner_radius * math.sin((i + 1) * angle_per_spoke)
        x4 = center_x + inner_radius * math.cos(i * angle_per_spoke)
        y4 = center_y + inner_radius * math.sin(i * angle_per_spoke)
        pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

# Effacer l’écran en blanc
screen.fill((255, 255, 255))
draw_star(screen)

# Enregistrement dans le dossier public/ (absolu ou relatif)
output_path = os.path.join("public", "etoile.png")
pygame.image.save(screen, output_path)
print(f"[✔] Image générée à : {output_path}")

pygame.quit()
