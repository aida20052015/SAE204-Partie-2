import pygame
import math
import random
import os

# Initialisation de Pygame sans fenêtre
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

# Dimensions de l'écran
WIDTH, HEIGHT = 800, 800
screen = pygame.Surface((WIDTH, HEIGHT))  # Surface en mémoire, pas de fenêtre

def draw_siemens_star(surface, center_x, center_y, outer_radius, inner_radius, num_spokes, color1, color2):
    if num_spokes % 2 != 0:
        print("Le nombre de rayons doit être un multiple de 2.")
        return

    angle_per_spoke = 2 * math.pi / num_spokes

    for i in range(num_spokes):
        current_color = color1 if i % 2 == 0 else color2

        x1_outer = center_x + outer_radius * math.cos(i * angle_per_spoke)
        y1_outer = center_y + outer_radius * math.sin(i * angle_per_spoke)

        x2_outer = center_x + outer_radius * math.cos((i + 1) * angle_per_spoke)
        y2_outer = center_y + outer_radius * math.sin((i + 1) * angle_per_spoke)

        x3_inner = center_x + inner_radius * math.cos((i + 1) * angle_per_spoke)
        y3_inner = center_y + inner_radius * math.sin((i + 1) * angle_per_spoke)

        x4_inner = center_x + inner_radius * math.cos(i * angle_per_spoke)
        y4_inner = center_y + inner_radius * math.sin(i * angle_per_spoke)

        pygame.draw.polygon(surface, current_color,
                            [(x1_outer, y1_outer), (x2_outer, y2_outer),
                             (x3_inner, y3_inner), (x4_inner, y4_inner)])

# Remplir l'arrière-plan
screen.fill((255, 255, 255))  # Blanc

# Paramètres aléatoires pour personnaliser l'étoile
center_x = WIDTH // 2
center_y = HEIGHT // 2
outer_radius = random.randint(200, min(WIDTH, HEIGHT) // 2 - 20)
inner_radius = random.randint(10, outer_radius // 4)
num_spokes = random.choice([24, 36, 48, 60, 72, 96, 120])
color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while sum(abs(c1 - c2) for c1, c2 in zip(color1, color2)) < 150:
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Dessiner l'étoile
draw_siemens_star(screen, center_x, center_y, outer_radius, inner_radius, num_spokes, color1, color2)

# Enregistrer l'image dans Symfony (public/)
pygame.image.save(screen, "public/etoile.png")
pygame.quit()
