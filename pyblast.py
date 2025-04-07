import pygame
import random

pygame.init()
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("BlockBlast")

# Farger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Spillbrettet (0 er tom rute)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Størrelse på hver rute i brettet
cell_size = 50
board_padding = 50  # Padding rundt brettet
board_area = pygame.Rect(board_padding, board_padding, cell_size * 8, cell_size * 8)

# Tetromino-former (I, O, T, S, Z, J, L)
# Hver tetromino defineres som en liste av (x, y) koordinater relativt til et referansepunkt
tetrominos = {
    'I': [(0, 0), (0, 1), (0, 2), (0, 3)],
    'O': [(0, 0), (0, 1), (1, 0), (1, 1)],
    'T': [(0, 0), (0, 1), (0, 2), (1, 1)],
    'S': [(0, 1), (0, 2), (1, 0), (1, 1)],
    'Z': [(0, 0), (0, 1), (1, 1), (1, 2)],
    'J': [(0, 0), (1, 0), (1, 1), (1, 2)],
    'L': [(0, 2), (1, 0), (1, 1), (1, 2)]
}

# Farge for hver tetromino
tetromino_colors = {
    'I': CYAN,
    'O': YELLOW,
    'T': PURPLE,
    'S': GREEN,
    'Z': RED,
    'J': BLUE,
    'L': ORANGE
}

# Aktive tetrominos på siden (3 stk)
available_tetrominos = []
selected_tetromino = None
selected_tetromino_offset = (0, 0)

def get_new_tetromino():
    """Velger en tilfeldig tetromino"""
    tetromino_type = random.choice(list(tetrominos.keys()))
    return {
        'type': tetromino_type,
        'blocks': tetrominos[tetromino_type].copy(),
        'color': tetromino_colors[tetromino_type],
        'rect': pygame.Rect(0, 0, 0, 0)  # Oppdateres senere
    }
def rotate_tetromino(tetromino):
    """Roterer en tetromino 90 grader med klokka"""
    tetromino['blocks'] = [(-y, x) for x, y in tetromino['blocks']]
def normalize_tetromino(tetromino):
    """Justerer tetromino slik at den starter fra (0,0)"""
    min_x = min(x for x, y in tetromino['blocks'])
    min_y = min(y for x, y in tetromino['blocks'])
    tetromino['blocks'] = [(x - min_x, y - min_y) for x, y in tetromino['blocks']]
def get_tetromino_dimensions(tetromino):
    """Returnerer bredde og høyde for en tetromino"""
    max_x = max(x for x, y in tetromino['blocks']) + 1
    max_y = max(y for x, y in tetromino['blocks']) + 1
    return max_x, max_y
def can_place_tetromino(tetromino, board_x, board_y):
    """Sjekker om en tetromino kan plasseres på brettet"""
    for block_x, block_y in tetromino['blocks']:
        x = board_x + block_x
        y = board_y + block_y
        
        # Sjekk om utenfor brettet
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return False
        
        # Sjekk om ruten er opptatt
        if board[y][x] != 0:
            return False
    
    return True
def place_tetromino(tetromino, board_x, board_y):
    """Plasserer en tetromino på brettet"""
    color_value = list(tetromino_colors.values()).index(tetromino['color']) + 1
    
    for block_x, block_y in tetromino['blocks']:
        x = board_x + block_x
        y = board_y + block_y
        board[y][x] = color_value
    
    return True
def clear_full_rows_and_columns(board):
    """Fjerner fulle rader og kolonner"""
    rows_to_clear = []           
    columns_to_clear = []                                    

    for row in range(8):
        if all(val != 0 for val in board[row]):
            rows_to_clear.append(row)

    for col in range(8):  
        if all(board[row][col] != 0 for row in range(8)):  
            columns_to_clear.append(col)

    for row in rows_to_clear:
        board[row] = [0] * 8

    for col in columns_to_clear:
        for row in range(8):
            board[row][col] = 0  

    return len(rows_to_clear) + len(columns_to_clear)  # Returnerer antall fjernede rader/kolonner
def draw_board():
    """Tegner spillbrettet"""
    # Tegn bakgrunn
    screen.fill(BLACK)
    
    # Tegn brett bakgrunn
    pygame.draw.rect(screen, (50, 50, 50), board_area)
    
    # Tegn hver celle
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(
                board_padding + x * cell_size, 
                board_padding + y * cell_size, 
                cell_size, 
                cell_size
            )
            # Tegn rutenett
            pygame.draw.rect(screen, WHITE, rect, 1)
            
            # Fyll ruter som har blokker
            if board[y][x] != 0:
                color_index = board[y][x] - 1
                color = list(tetromino_colors.values())[color_index]
                pygame.draw.rect(screen, color, rect.inflate(-2, -2))
def draw_tetromino(tetromino, pos_x, pos_y):
    """Tegner en tetromino på skjermen"""
    for block_x, block_y in tetromino['blocks']:
        rect = pygame.Rect(
            pos_x + block_x * cell_size, 
            pos_y + block_y * cell_size, 
            cell_size, 
            cell_size
        )
        pygame.draw.rect(screen, tetromino['color'], rect.inflate(-2, -2))
        pygame.draw.rect(screen, WHITE, rect, 1)
def draw_available_tetrominos():
    """Tegner de tilgjengelige tetrominos på høyre side"""
    sidebar_x = board_padding + 8 * cell_size + 50
    
    font = pygame.font.SysFont(None, 36)
    text = font.render("Tilgjengelige blokker:", True, WHITE)
    screen.blit(text, (sidebar_x, board_padding))
    
    y_offset = board_padding + 50
    spacing = 20
    
    for i, tetromino in enumerate(available_tetrominos):
        if tetromino is None:
            continue
            
        width, height = get_tetromino_dimensions(tetromino)
        
        # Oppdater plassering for denne tetromino
        tetromino_x = sidebar_x + (4 - width) * cell_size // 2
        tetromino_y = y_offset + i * (cell_size * 4 + spacing)
        
        # Lagre rektangelet for å kunne sjekke klikk
        tetromino['rect'] = pygame.Rect(
            tetromino_x, 
            tetromino_y, 
            width * cell_size, 
            height * cell_size
        )
        
        # Tegn bakgrunn for tetromino
        pygame.draw.rect(screen, (50, 50, 50), tetromino['rect'].inflate(10, 10))
        
        # Tegn tetromino
        draw_tetromino(tetromino, tetromino_x, tetromino_y)
        
        # Tegn roter-knapp
        rotate_button = pygame.Rect(
            tetromino_x + width * cell_size + 10, 
            tetromino_y, 
            30, 
            30
        )
        pygame.draw.rect(screen, (100, 100, 100), rotate_button)
        pygame.draw.polygon(screen, WHITE, [
            (rotate_button.centerx - 5, rotate_button.centery - 10),
            (rotate_button.centerx + 10, rotate_button.centery),
            (rotate_button.centerx - 5, rotate_button.centery + 10)
        ])
        
        # Lagre roter-knapp rektangel
        tetromino['rotate_button'] = rotate_button
def draw_ghost_tetromino(tetromino, mouse_pos):
    """Tegner en halvtransparent versjon av tetromino under musen"""
    # Finn brettrute under musen
    if board_area.collidepoint(mouse_pos):
        grid_x = (mouse_pos[0] - board_padding) // cell_size
        grid_y = (mouse_pos[1] - board_padding) // cell_size
        
        # Tegn tetromino på brettet
        can_place = can_place_tetromino(tetromino, grid_x, grid_y)
        ghost_color = (
            tetromino['color'][0] // 2, 
            tetromino['color'][1] // 2, 
            tetromino['color'][2] // 2
        )
        
        for block_x, block_y in tetromino['blocks']:
            x = grid_x + block_x
            y = grid_y + block_y
            
            # Bare tegn blokker som er innenfor brettet
            if 0 <= x < 8 and 0 <= y < 8:
                rect = pygame.Rect(
                    board_padding + x * cell_size, 
                    board_padding + y * cell_size, 
                    cell_size, 
                    cell_size
                )
                color = ghost_color if can_place else (255, 0, 0, 128)
                pygame.draw.rect(screen, color, rect.inflate(-2, -2))
                pygame.draw.rect(screen, WHITE, rect, 1)
    else:
        # Tegn tetromino under musen
        offset_x = mouse_pos[0] - selected_tetromino_offset[0]
        offset_y = mouse_pos[1] - selected_tetromino_offset[1]
        draw_tetromino(tetromino, offset_x, offset_y)
def refill_tetrominos():
    """Fyller opp tilgjengelige tetrominos"""
    while len(available_tetrominos) < 3:
        new_tetromino = get_new_tetromino()
        normalize_tetromino(new_tetromino)
        available_tetrominos.append(new_tetromino)

# Initialiser spillet
refill_tetrominos()
score = 0
running = True
clock = pygame.time.Clock()

while running:
    current_mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Venstre museknapp
            # Sjekk om vi klikker på en tilgjengelig tetromino
            for i, tetromino in enumerate(available_tetrominos):
                if tetromino is None:
                    continue
                    
                # Sjekk roter-knapp først
                if tetromino['rotate_button'].collidepoint(event.pos):
                    rotate_tetromino(tetromino)
                    normalize_tetromino(tetromino)
                    break
                
                # Sjekk selve tetromino
                elif tetromino['rect'].collidepoint(event.pos):
                    selected_tetromino = i
                    # Beregn offset for å holde tetromino der vi klikket
                    selected_tetromino_offset = (
                        event.pos[0] - tetromino['rect'].x,
                        event.pos[1] - tetromino['rect'].y
                    )
                    break
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Slipp venstre museknapp
            if selected_tetromino is not None:
                tetromino = available_tetrominos[selected_tetromino]
                
                # Sjekk om vi slipper på brettet
                if board_area.collidepoint(event.pos):
                    grid_x = (event.pos[0] - board_padding) // cell_size
                    grid_y = (event.pos[1] - board_padding) // cell_size
                    
                    # Forsøk å plassere tetromino
                    if can_place_tetromino(tetromino, grid_x, grid_y):
                        place_tetromino(tetromino, grid_x, grid_y)
                        
                        # Fjern tetromino fra tilgjengelige
                        available_tetrominos[selected_tetromino] = None
                        
                        # Sjekk for fulle rader/kolonner
                        cleared = clear_full_rows_and_columns(board)
                        score += cleared * 100
                        
                        # Fyll opp med nye tetrominos hvis nødvendig
                        available_tetrominos = [t for t in available_tetrominos if t is not None]
                        refill_tetrominos()
                
                selected_tetromino = None
    
    # Tegn alt
    draw_board()
    draw_available_tetrominos()
    
    # Tegn tetromino som dras
    if selected_tetromino is not None:
        draw_ghost_tetromino(available_tetrominos[selected_tetromino], current_mouse_pos)
    
    # Vis score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Poeng: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))
    
    pygame.display.flip()
    clock.tick(60)  # FPS

pygame.quit()