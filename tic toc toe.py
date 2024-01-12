import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
width, height = 600, 600
line_color = (0, 0, 0)
white = (255, 255, 255)
board = [['', '', ''], ['', '', ''], ['', '', '']]
human_player = 'O'
agent_player = 'X'
winner = None

# Initialisation de la fenêtre
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")


# Fonction pour dessiner la grille
def draw_board():
    screen.fill(white)

    # Dessiner les lignes verticales
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (width // 3 * i, 0), (width // 3 * i, height), 5)

    # Dessiner les lignes horizontales
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (0, height // 3 * i), (width, height // 3 * i), 5)

    # Dessiner les X et O
    font = pygame.font.Font(None, 100)
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                text = font.render('X', True, line_color)
                screen.blit(text, (col * width // 3 + 20, row * height // 3 + 20))
            elif board[row][col] == 'O':
                text = font.render('O', True, line_color)
                screen.blit(text, (col * width // 3 + 20, row * height // 3 + 20))


# Fonction pour vérifier s'il y a un gagnant
def check_winner():
    global winner
    # Vérifier les lignes et colonnes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            winner = board[i][0]
            return True
        elif board[0][i] == board[1][i] == board[2][i] != '':
            winner = board[0][i]
            return True

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        return True
    elif board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        return True

    return False


# Fonction pour vérifier s'il y a un match nul
def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True


# Fonction pour que l'agent joue
def agent_play():
    # Choisissez une action aléatoire pour l'agent (simulation d'apprentissage par renforcement)
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = agent_player


# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and winner is None:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // (height // 3)
            clicked_col = mouseX // (width // 3)

            # Vérifier si la case est vide
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = human_player

                # Vérifier s'il y a un gagnant ou un match nul
                if check_winner():
                    print(f"Le joueur {winner} a gagné !")
                elif check_draw():
                    print("Match nul !")

                # Laisser l'agent jouer
                if not check_winner() and not check_draw():
                    agent_play()
                    if check_winner():
                        print(f"L'agent {agent_player} a gagné !")
                    elif check_draw():
                        print("Match nul !")

    draw_board()
    pygame.display.flip()
