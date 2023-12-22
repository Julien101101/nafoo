import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Triangle")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up triangle parameters
triangle_size = 50
triangle_x = width // 2
triangle_y = height // 2
triangle_speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle VIDEORESIZE event
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height))

        # Handle MOUSEBUTTONDOWN event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            print(f"Mouse button down at ({mouse_x}, {mouse_y})")

    keys = pygame.key.get_pressed()

    # Update triangle position based on arrow keys
    if keys[pygame.K_LEFT] and triangle_x > 0:
        triangle_x -= triangle_speed
    if keys[pygame.K_RIGHT] and triangle_x < width - triangle_size:
        triangle_x += triangle_speed
    if keys[pygame.K_UP] and triangle_y > 0:
        triangle_y -= triangle_speed
    if keys[pygame.K_DOWN] and triangle_y < height - triangle_size:
        triangle_y += triangle_speed

    # Draw background
    screen.fill(white)

    # Draw triangle
    pygame.draw.polygon(screen, red, [(triangle_x, triangle_y),
                                      (triangle_x + triangle_size, triangle_y),
                                      (triangle_x + triangle_size / 2, triangle_y - triangle_size)])

    # Update display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)
