"""
Reference
1. Text input box: https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame

"""


import pygame
import random
from line import draw_line
from moon import Moon


pygame.init()
pygame.font.init()

small_font = pygame.font.SysFont('Comic Sans MS', 14)
medium_font = pygame.font.SysFont('Comic Sans MS', 20)
big_font = pygame.font.SysFont('Comic Sans MS', 30)

color_active = (255, 0, 0)
color_inactive = (255, 255, 0)

clock = pygame.time.Clock()

WIDTH, HEIGHT = 700, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WONDER!")


def welcome_screen(window):
    pass


def animate(window, moon, z0, z1):
    # At each step update the moons location and refresh the window

    zones = []
    if z1 >= z0:
        zones = [i for i in range(z0, z1 + 1)]
    else:
        zones = [i for i in range(z0, 8)]
        zones.extend([i for i in range(z1 + 1)])
    print(f"zones={zones}")

    for z in range(len(zones)):
        zone = zones[z]
        pixels = moon.orbit[zone]
        for p, pixel in enumerate(pixels):
            if z == 0:
                if p < len(pixels)//2 - 1:
                    continue
            if z == len(zones) - 1:
                if p > len(pixels)//2:
                    continue
            moon.x, moon.y = pixel[0], pixel[1]
            refresh_window(window, moon)
            pygame.time.delay(10)


def draw_axis(window):
    draw_line(window, HEIGHT, 0, 0, HEIGHT)
    draw_line(window, 0, 0, HEIGHT, HEIGHT)
    draw_line(window, HEIGHT//2, 0, HEIGHT//2, HEIGHT)
    draw_line(window, 0, HEIGHT // 2, HEIGHT, HEIGHT//2)
    # pygame.draw.line(window, (160, 32, 240), (HEIGHT, 0), (0, HEIGHT))
    # pygame.draw.line(window, (160, 32, 240), (0, 0), (HEIGHT, HEIGHT))
    # pygame.draw.line(window, (160, 32, 240),
    #                  (HEIGHT//2, 0), (HEIGHT//2, HEIGHT))
    # pygame.draw.line(window, (160, 32, 240),
    #                  (0, HEIGHT // 2), (HEIGHT, HEIGHT//2))


user_input = ""


def refresh_window(window, moon, input_box_color=(255, 0, 0), invalid=False):
    window.fill((0, 0, 0))

    pygame.draw.rect(window, (20, 20, 20), (0, 0, HEIGHT, HEIGHT))
    # Draw the axis
    draw_axis(window)

    # Draw the earth
    pygame.draw.circle(window, (0, 0, 180), (200, 200), 15)

    # draw the moon
    moon.draw(window)
    # moon.draw(window)

    # Render Text

    text1 = small_font.render(
        "Enter month and date in this format: mm dd", False, (255, 255, 255))
    text2 = big_font.render("!!! Invalid input !!!", False, (255, 0, 0))
    text3 = medium_font.render(f"{user_input}", False, (255, 0, 0))
    window.blit(text1, (405, 5))
    window.blit(text3, (510, 55))
    if invalid:
        window.blit(text2, (430, 100))

    # User Input
    pygame.draw.rect(window, input_box_color, (500, 50, 100, 40), 2)

    pygame.display.update()


def calculate_new_zone(month, day):
    print(f"Month & Day: {month} {day}")
    new_zone = (((month - 1) * 30 + day) % 7)
    # return random.choice([1, 2, 3, 4, 5, 6, 7])
    return new_zone


def main(window):
    global user_input
    moon = Moon(150)
    run = True
    z0 = moon.zone
    invalid = False
    input_box = pygame.Rect(500, 50, 100, 40)
    active = False
    color = color_inactive
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            if len(user_input) != 5 or user_input[2] != " ":
                                raise(Exception)
                            month = int(user_input[:2])
                            day = int(user_input[3:5])
                            if 1 <= month <= 12 and 1 <= day <= 30:
                                z0 = moon.zone
                                z1 = calculate_new_zone(month, day)
                                moon.rotation = True
                            else:
                                raise(Exception)
                                # invalid = True
                                # user_input = ""
                        except:
                            user_input = ""
                            invalid = True
                    elif event.key == pygame.K_BACKSPACE and active:
                        try:
                            user_input = user_input[:-1]
                        except:
                            pass
                    else:
                        if active and len(user_input) < 5:
                            print(f"keystroke: {event.unicode}")
                            user_input += event.unicode
                # if event.key == pygame.K_SPACE:
                #     moon.rotation = True

        if moon.rotation:
            animate(window, moon, moon.zone, z1)
            moon.zone = z1
            moon.rotation = False
            user_input = ""
            active = False
            invalid = False

        color = color_active if active else color_inactive

        refresh_window(window, moon, color, invalid)
        clock.tick(10)


if __name__ == "__main__":
    welcome_screen(window)
    main(window)
