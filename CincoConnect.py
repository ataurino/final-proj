rows = 6
columns = 9

def buildBoard():
    return [[' ' for _ in range(columns)] for _ in range(rows)]

def drawBoard(board):
    for row in board:
        print('|', end="")
        for spot in row:
            print("  " + spot + "  |", end="")
        print("\n" + '-' * (6 * len(board[0]) + 1))

def playerTurn(turns):
    players = ['X', 'O']
    return players[turns % 2]

def inBoard(r, c):
    return (0 <= r < rows) and (0 <= c < columns)

def makeMove(board, column, turns):
    for row in range(rows - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = playerTurn(turns)
            return row, column
    return None

def checkForWin(board, lastMove):
    lastRow, lastCol = lastMove
    lastLetter = board[lastRow][lastCol]

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

    for rowChange, colChange in directions:
        count = 1

        for move in range(1, 5):
            r, c = lastRow + rowChange * move, lastCol + colChange * move
            if inBoard(r, c) and board[r][c] == lastLetter:
                count += 1
            else:
                break

        for move in range(1, 5):
            r, c = lastRow - rowChange * move, lastCol - colChange * move
            if inBoard(r, c) and board[r][c] == lastLetter:
                count += 1
            else:
                break

        if count >= 5:
            drawBoard(board)
            print(lastLetter + " is the winner!")
            return lastLetter
    return False

def playGame():
    print("Welcome to Cinco Connect")
    board = buildBoard()
    turns = 0
    lastMove = None
    gameOver = False

    while True:
        drawBoard(board)
        if gameOver:
            break

        playerInput = input(playerTurn(turns) + "'s turn. Select a column (1-9): ")

        if playerInput.isdigit():
            chosenColumn = int(playerInput) - 1
            moveResult = makeMove(board, chosenColumn, turns)

            if moveResult:
                lastMove = moveResult
                gameOver = checkForWin(board, lastMove)
                turns += 1

playGame()
