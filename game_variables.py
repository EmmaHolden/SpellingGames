import pygame

pygame.font.init()

# SPELLING WORDS
spelling_words = ["camel", "otter", "octopus", "sealion", "tiger"]

# HANGMAN FONTS
chalk_font_40 = pygame.font.Font('font/chalk.otf', 40)
chalk_font_60 = pygame.font.Font('font/chalk.otf', 60)
chalk_font_60_underlined = pygame.font.Font('font/chalk.otf', 60)
pygame.font.Font.set_underline(chalk_font_60_underlined, True)
chalk_font_120 = pygame.font.Font('font/chalk.otf', 120)

# CHOMPER FONTS
pixel_font_60 = pygame.font.Font('font/Pixeltype.ttf', 60)
pixel_font_40 = pygame.font.Font('font/Pixeltype.ttf', 40)
pixel_font_80 = pygame.font.Font('font/Pixeltype.ttf', 80)
pixel_font_120 = pygame.font.Font('font/Pixeltype.ttf', 120)

# HORSE RACING FONTS
horse_font_40 = pygame.font.Font('font/horse.ttf', 40)
horse_font_60 = pygame.font.Font('font/horse.ttf', 60)

game_colours = {
    "green": '#00DFA2',
    "lightblue": "#A2D2FF",
    "blue": '#0079FF',
    "yellow": '#F6FA70',
    "orange": '#FF9526',
    "red": '#FF0060',
    "purple": '#2A3492',
}



