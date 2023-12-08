#CIT end of course program
'''
Blaine Boothe
CIT 144
'''
import random 
import time

class wins: 
    def __init__(self,playerx,playero,tiles): 
        self.playerx = playerx
        self.playero = playero
        self.game_over = False
        self.tiles=tiles
    def winning_checks(self): 
        for i in range(2): 
            hori_wins=[[1,2,3],[4,5,6],[7,8,9]]  
            vert_wins=[[1,4,7],[2,5,8],[3,6,9]] 
            dia_wins=[[1,5,9],[3,5,7]]          
            if i == 0:  
                player = playerx  
                Player = "Player X"  
            else:  
                player = playero
                Player = "Player O"
            for value in player:  
                for instance in hori_wins:  
                    if value in instance:  
                        index = instance.index(value)  
                        del instance[index]  
            for instance in hori_wins: 
                if instance == []:  
                    self.game_over = True  
                    print_board(self.tiles)  
                    print(f"{Player} has won the game with a horizontal win!")  
                    if self.game_over:  
                        return self.game_over  
            for value in player:  
                for instance in vert_wins:
                    if value in instance:
                        index=instance.index(value)
                        del instance[index]
            for instance in vert_wins:
                if instance == []:
                    self.game_over = True
                    print_board(self.tiles)
                    print(f'{Player} has won the game with a verticle win!')
                    if self.game_over:
                        return self.game_over
            for value in player:
                for instance in dia_wins:
                    if value in instance:
                        index=instance.index(value)
                        del instance[index]
            for instance in dia_wins:
                if instance == []:
                    self.game_over=True
                    print_board(self.tiles)
                    print(f'{Player} has won the game with a diagonal win!')
                    if self.game_over:
                        return self.game_over
        
positions = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]  
tiles = ["-","-","-","-","-","-","-","-","-",]  
playerx = []  
playero = []  
global turn  
turn = 2  
turn2 = 2  
def print_board(tiles):  
    print(f'\n    1   2   3\n  _____________ \nA | {tiles[0]} | {tiles[1]} | {tiles[2]} | \n  |―――|―――|―――| \nB | {tiles[3]} | {tiles[4]} | {tiles[5]} | \n  |―――|―――|―――| \nC | {tiles[6]} | {tiles[7]} | {tiles[8]} | \n  -------------')

def player_check(turn):  
    if turn % 2 == 0:  
        return ("X")
    else: 
        return ("O")

def get_chosen_tile(positions,playerx,playero,mode,turn2,tiles,stalemate):  
    checkoverall = True 
    number = 0
    while stalemate == False:  
        for value in tiles:  
            if value == '-':
                number += 1
        if number !=0: 
            if turn2 % 2 == 0:   
                while checkoverall:  
                    check = True
                    while check:  
                        x = input("row: ")  
                        x=x.upper()  
                        if x == "A" or x == "B" or x == "C":  
                            check = False
                        else:  
                            print("Referenced row value does not exist, please input either A, B, or C")
                    check = True
                    while check:  
                        y = int(input("column: "))
                        if y >= 1 and y <= 3:
                            check = False
                        else:
                            print("Referenced column value does not exist, please input either 1, 2, or 3")
                    x=x.upper()
                    tile = x + str(y)  
                    index = positions.index(tile)  
                    if index+1 in playerx or index+1 in playero:  
                        print("You cannot overlap positions! Please pick an empty position on the board.")
                    else:  
                        checkoverall=False  
                        if mode == 1:  
                            turn2+=1  
                        return tile,turn2  
            elif turn2%2==1:  
                options = ["A","B","C"] 
                overlap = True 
                print("Opponent is picking...") 
                while overlap:  
                    letter = random.randint(0,2) 
                    x = options[letter]  
                    y = random.randint(1,3) 
                    tile = x + str(y) 
                    index = positions.index(tile) 
                    if index+1 in playerx or index+1 in playero: 
                        continue 
                    else: 
                        overlap = False 
                seconds=random.randint(1,7) 
                time.sleep(seconds)  
                turn2+=1 
                return tile,turn2 
        else: 
            stalemate = True 
            print("Game Over. Stalemate (No Winners)") 
            return stalemate, turn2 
        

def update_tile(chosen_tile, tiles, positions, turn, playerx, playero): 
    index = positions.index(chosen_tile) 
    tiles[index] = player_check(turn) 
    if player_check(turn) == "X": 
        playerx.append(index+1) 
        playerx.sort()
    elif player_check(turn) == "O": 
        playero.append(index+1)
        playero.sort()
    else: 
        print("STORE ERROR: Value could not be stored due to no player recognized")
    return playerx,playero,positions,tiles 

def play(no_winner,turn,tiles,positions,playerx,playero,mode,turn2,stalemate): 
    while no_winner: 
        print_board(tiles) 
        chosen_tile,turn2 = get_chosen_tile(positions,playerx,playero,mode,turn2,tiles,stalemate) 
        if chosen_tile == True: 
            no_winner = False 
            break 
        playerx,playero,positions,tiles = update_tile(chosen_tile, tiles, positions, turn, playerx, playero) 
        conditions=wins(playerx,playero,tiles) 
        check = conditions.winning_checks() 
        if check: 
            no_winner = False 
            break 
        turn += 1 

no_winner = True 
string_check = True 
stalemate = False 
print("Ready to play some Tic Tac Toe? Before you do that...")
while string_check:
    try:
        mode = int(input("Select a mode from the options below: \n   1. 1 Player \n   2. 2 Player \nSelection: "))
        if mode != 1 and mode != 2:
            while mode != 1 and mode != 2: 
                print("Invalid option, please pick either 1 or 2.")
                try:
                    mode = int(input("Selection: "))
                    string_check = False
                except:
                    continue
        else:
            string_check = False
    except:
        print("Invalid option, please select either 1 or 2.")
        continue
play(no_winner,turn,tiles,positions,playerx,playero,mode,turn2,stalemate)
Play_again = input("Do you want to play again? ")
if Play_again == 'yes':
    play(no_winner,turn,tiles,positions,playerx,playero,mode,turn2,stalemate)
else:
    print("Hope you enjoyed")


