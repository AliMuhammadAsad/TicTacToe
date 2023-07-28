import pygame; pygame.init()

#Display Screen Size
screen_width = 500; screen_height = 650
gameWindow = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock(); fps = 60

#Game Title
pygame.display.set_caption("Tic Tac Toe")
pygame.display.update()

#colors
white = (255, 255, 255); black = (0, 0, 0); red = (255, 0, 0); green = (0, 255, 0); blue = (0, 0, 255)

#Home Screen
def home():
    exithome = False
    clickarea_twoplayer = pygame.Rect(123, 440, 245, 40) # (x, y, width, height)
    clickarea_computer = pygame.Rect(123, 497, 245, 40)
    while not exithome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exithome = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos, ypos = pygame.mouse.get_pos()
                # print(f"Mouse x: {xpos}, Mouse y: {ypos}")
                if clickarea_twoplayer.collidepoint(xpos, ypos): twoplayergame()
                if clickarea_computer.collidepoint(xpos, ypos): computergame()

        img = pygame.image.load("assets/HomeScreen.png")
        gameWindow.fill(white)
        gameWindow.blit(img, (0, 0))
        
        pygame.display.update()
        clock.tick(fps)
    pygame.quit(); quit()

#Game Loop
def twoplayergame():
    exitgame = False; gameover = False
    wincheck = False; winplayer = None; drawcheck = False
    curr_player = "X"
    ximg = pygame.image.load("assets/x.png"); ximg = pygame.transform.scale(ximg, (160, 160))
    oimg = pygame.image.load("assets/o.png"); oimg = pygame.transform.scale(oimg, (160, 160))

    board = [["" for _ in range(3)] for _ in range(3)]

    while not exitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exitgame = True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: 
                    home()
                if event.key == pygame.K_r: twoplayergame()
            if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
                xpos, ypos = pygame.mouse.get_pos()
                row = ypos // 166; col = xpos // 166
                print(xpos, ypos, row, col)
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                    board[row][col] = curr_player
                    if check_winner(board, curr_player):
                        wincheck = True; winplayer = curr_player
                        print(f"Player {curr_player} wins!")
                        gameover = True
                    elif check_draw(board):
                        drawcheck = True
                        print("It's a Draw")
                        gameover = True
                    else:
                        curr_player = "X" if curr_player == "O" else "O"
        
        gameWindow.fill(black)
        img = pygame.image.load("assets/field.png")
        img = pygame.transform.scale(img, (500, 500))
        gameWindow.blit(img, (0, 0))

        drawboard(board)
        if wincheck == True: 
            drawline(board, winplayer)

        font = pygame.font.Font(None, 72)
        if not wincheck and not drawcheck:
            text = font.render(f"Player {curr_player}'s Turn", True, white)
        
        if wincheck: text = font.render(f"Player {curr_player} Wins!", True, white)
        if drawcheck: text = font.render(f"It's a Draw!", True, white)

        gameWindow.blit(text, (75, 555))

        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit(); quit()

def computergame():
    exitgame = False
    while not exitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exitgame = True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: 
                    home()
        
        gameWindow.fill(black)
        img = pygame.image.load("assets/field.png")
        img = pygame.transform.scale(img, (500, 500))
        gameWindow.blit(img, (0, 0))
        
        font = pygame.font.Font(None, 48)
        text = font.render("Game Mode in Development", True, white)
        gameWindow.blit(text, (25, 555))

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

def check_winner(board, player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)): return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): return True
    if board[0][0] == board[1][1] == board[2][2] == player: return True
    if board[0][2] == board[1][1] == board[2][0] == player: return True
    return False

def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "": return False
    return True

def drawboard(board):
    for row in range(3):
        for col in range(3):
            cx = col * 166; cy = row * 166
            if board[row][col] == "X":
                ximg = pygame.image.load("assets/x.png")
                ximg = pygame.transform.scale(ximg, (160, 160))
                gameWindow.blit(ximg, (cx, cy))
            elif board[row][col] == "O":
                oimg = pygame.image.load("assets/o.png"); oimg = pygame.transform.scale(oimg, (160, 160))
                gameWindow.blit(oimg, (cx, cy))

def drawline(board, player):
    if board[0][0] == board[0][1] == board[0][2] == player: xs = 0; ys = 0; xe = 2; ye = 0
    elif board[1][0] == board[1][1] == board[1][2] == player: xs = 0; ys = 1; xe = 2; ye = 1
    elif board[2][0] == board[2][1] == board[2][2] == player: xs = 0; ys = 2; xe = 2; ye = 2
    elif board[0][0] == board[1][0] == board[2][0] == player: xs = 0; ys = 0; xe = 0; ye = 2
    elif board[0][1] == board[1][1] == board[2][1] == player: xs = 1; ys = 0; xe = 1; ye = 2
    elif board[0][2] == board[1][2] == board[2][2] == player: xs = 2; ys = 0; xe = 2; ye = 2
    elif board[0][0] == board[1][1] == board[2][2] == player: xs = 0; ys = 0; xe = 2; ye = 2
    elif board[0][2] == board[1][1] == board[2][0] == player: xs = 2; ys = 0; xe = 0; ye = 2

    xs = xs * 166 + 83; ys = ys * 166 + 83; xe = (xe + 1) * 166 - 83; ye = (ye + 1) * 166 - 83
    pygame.draw.line(gameWindow, green, (xs, ys), (xe, ye), 10)
    # pygame.display.update()
    return  

if __name__ == "__main__":
    home()