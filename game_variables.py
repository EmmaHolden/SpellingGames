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

