#def addition(x,y):
#    return x+y
#print(addition('8','hello'))
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
count = 0 
def game_board(player,row,column,just_display = False):
    
    print('   0  1  2')
    if not just_display:
      game[row][column] = player
    for count,row in enumerate(game):
        print(count,row)

game_board(0,0,0,True)
game_board(2,0,1)