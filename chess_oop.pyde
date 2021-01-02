#################################
# imports 


##################################
# classes 

#conttrols the game
class Game:
    #default settings of the game 
    def __init__(self):
        #current game screen
        self.mode = "HOME"
        #turn of player
        self.turn = "WHITE"
        #captuCURRENT pieces on both sides 
        self.blackpieces = {"BLACK King": 0, "BLACK Knight": 0, "BLACK Rook": 0, "BLACK Bishop": 0, "BLACK Queen":0, "BLACK Pawn": 0}
        self.whitepieces = {"WHITE King": 0, "WHITE Knight": 0, "WHITE Rook": 0, "WHITE Bishop": 0, "WHITE Queen":0, "WHITE Pawn": 0}
        self.whitemoves = 0
        self.blackmoves = 0
        #whether or not a pawn has reached either side
        self.generate = False
        self.genside = ''
    
    #return the list of captured pieces 
    def pieces(self):
        return self.whitepieces, self.blackpieces
    
    #change the screen
    def change_screen(self, mode):
        self.mode = mode   
    
    #run the home screen
    def home_screen(self):
        image(homeimg,0,0)
        

    #control game screens
    def run(self):
        #play game screen
        if self.mode == "HOME":
            self.home_screen()
        if self.mode == "GAME":
            self.game_screen()
        if self.mode == "END":
            self.end_screen()
        if self.mode == "INSTRUCT":
            self.instruct_screen()
        if self.mode == "TIE":
            self.tie_screen()

    #main game screen 
    def game_screen(self):
        #border around board
        background(245,234,205)
        
        #if pawn has reached the end add tint for background
        if self.generate:
            tint(255,75)
        else:
            #no tint 
            noTint()
      
        #draw out the side interface 
        self.side_ui()
        
        #draws the board
        board.draw()   
        
        #check if there is a tie (only two kings left)
        board.tie()        
        
        #if there is a pawn at either side run screen that shows a player options 
        if self.generate:
          self.gen_screen()
    
    #instruciton screen
    def instruct_screen(self):
        image(instructions,0,0)
    
    #generate a new piece!
    def gen_true(self, piece, row, col):
        self.generate = True 
        self.genside = piece
        self.gen_row = row
        self.gen_col = col
    
    #no need to generate a new piece anymore
    def gen_false(self):
        self.generate = False 
        
    #get bool for if game is generating piece or not
    def get_gen(self):
        return self.generate  

    #if game is generating a piece run this screen
    def gen_screen(self):
        global select1, select2
        noTint()
        #different images based on what is being generated 
        if self.genside == "WHITE":
            image(select1, 72,72,SCREEN_WIDTH-150, SCREEN_LENGTH-150)
        if self.genside == "BLACK":
            image(select2, 72, 72, SCREEN_WIDTH-150, SCREEN_LENGTH-150)
    
    #get the info for the piece that will be generated
    def get_geninfo(self):
        return self.genside, self.gen_row, self.gen_col, self.whitepieces, self.blackpieces
    
    #returns the game mode 
    def get_screen(self):
        return self.mode    
    
    #get the turn of which player
    def get_turn(self):
        return self.turn
    
    #changes the turn
    def change_turn(self, turn):
        if self.turn == "BLACK":
            self.blackmoves+=1
        if self.turn == "WHITE":
            self.whitemoves+=1        
        self.turn = turn

    #if a piece is captured add it to the captured list
    def captured(self, piece):
        if piece != "'EMPTY'":
            if self.get_turn() == "WHITE":
                self.blackpieces[piece] += 1
                                
            if self.get_turn() == "BLACK":
                self.whitepieces[piece] += 1
                
    #final screen if checkmate has occured with no more possible options        
    def end_screen(self):
        if game.get_turn() == "WHITE":
            image(blackimg, 0,0)
        if game.get_turn() == "BLACK":
            image(whiteimg, 0,0)   
    
    #game is tied 
    def tie_screen(self):
        image(tie,0,0)
    
    #side user interface 
    def side_ui(self):
        global whitepawn, blackpawn, whiteknight, blackknight, whitequeen, blackqueen, whiteking, blackking, whiterook, blackrook, whitebishop, blackbishop, whitepanel, blackpanel
        
        #runs the wooden panel design based on who's turn it is
        if self.turn == "WHITE":
            image(whitepanel,SCREEN_WIDTH, 0)
        elif self.turn == "BLACK":
            image(blackpanel,SCREEN_WIDTH,0)

        #list of all the images 
        blackimgs = [blackbishop, blackqueen, blackking, blackrook, blackknight, blackpawn]
        whiteimgs = [whitepawn, whiteknight, whiterook, whitequeen, whiteking,  whitebishop]
        
        fill(255)
        
        #starting x and y location  of each piece to draw it to the board 
        x = SCREEN_WIDTH + 20
        y = SCREEN_LENGTH - 225
        
        #drawing each image to the board looping through the pieces 
        for i in range(len(self.blackpieces)):
            image(blackimgs[i], x, y, 75, 75)
            textSize(20)
            text(self.blackpieces.values()[i], x+32, y + 95)
            x += 90
            if i == 2:
                y += 100
                x = SCREEN_WIDTH + 20
                

        x = SCREEN_WIDTH + 20
        y = 25
        
        #draw each image to the board looping through the pieces
        for i in range(len(self.whitepieces)):
            image(whiteimgs[i], x, y, 75, 75)
            textSize(20)
            text(self.whitepieces.values()[i], x+32, y + 95)
            x += 90
            if i == 2:
                y += 100
                x = SCREEN_WIDTH + 20
                            
    
#board of the game 
class Board:
    #instanciate the board
    def __init__(self):
        #all board pieces picking from every class
        self.board = [[Rook("BLACK", 0, 0), Knight("BLACK", 0, 1), Bishop("BLACK", 0, 2), King("BLACK", 0, 3), Queen("BLACK", 0, 4), Bishop("BLACK", 0, 5), Knight("BLACK",0, 6), Rook("BLACK", 0,7)],
                      [Pawn("BLACK", 1, 0), Pawn("BLACK", 1, 1), Pawn("BLACK", 1, 2), Pawn("BLACK", 1, 3), Pawn("BLACK", 1, 4), Pawn("BLACK", 1, 5), Pawn("BLACK", 1, 6), Pawn("BLACK", 1, 7)],
                      ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
                      ["EMPTY", "EMPTY", "EMPTY",  "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],             
                      ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],             
                      ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],   
                      [Pawn("WHITE", 6, 0), Pawn("WHITE", 6, 1), Pawn("WHITE", 6, 2), Pawn("WHITE", 6, 3), Pawn("WHITE", 6, 4), Pawn("WHITE", 6, 5), Pawn("WHITE", 6, 6), Pawn("WHITE", 6, 7)],
                      [Rook("WHITE", 7, 0), Knight("WHITE", 7, 1), Bishop("WHITE", 7, 2), King("WHITE", 7, 3), Queen("WHITE", 7, 4), Bishop("WHITE", 7, 5), Knight("WHITE", 7, 6), Rook("WHITE", 7, 7)]]
        #alternates squares
        self.tiles = [[Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE")],
                      [Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN")],
                      [Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE')],
                      [Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN")],
                      [Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE')],
                      [Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN")],
                      [Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE'), Square('GREEN'), Square('WHITE')],
                      [Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN"), Square("WHITE"), Square("GREEN")]]
        #no checkmate currently
        self.check = False 
    
    #checks whether or not game is tied
    def tie(self):
        #gets the captured pieces for both sides 
        white, black = game.pieces()
        
        #bools for which side has only a king 
        b_tie = False
        w_tie = False
        
        #checks which side only has a king 
        if white["WHITE Queen"] == 1 and white["WHITE Rook"] == 2 and white["WHITE Knight"] == 2 and white["WHITE PAWN"] == 8 and white["WHITE BISHOP"] == 2:
            w_tie = True 
            
        if black["BLACK Queen"] == 1 and black["BLACK Rook"] == 2 and white["BLACK Knight"] == 2 and black["BLACK PAWN"] == 8 and black["BLACK BISHOP"] == 2:
            b_tie = True 
            
        #if both only have a king, there is a tie!
        if b_tie and w_tie: 
            self.change_screen("TIE")
            
       
   #check if a pawn has reached the end of either side 
    def pawn_check(self):
        #get captured pieces
        white, black = game.pieces()
        
        #loop through the board
        for i in range (len(self.board)):
            for r in range(len(self.board[0])):
                #check if on the first row and the object is a pawn
                if self.board[i][r].__class__ == Pawn and i == 0:
                    #check if object is white
                    if self.board[i][r].get_type() == "WHITE":
                        #checks if any pieces have already been captured or not
                        if (white["WHITE Knight"] == 0 and white["WHITE Queen"] == 0 and white["WHITE Bishop"] == 0 and white["WHITE Rook"] == 0):
                            pass
                        else:
                            #game can generate pieces now 
                            game.gen_true("WHITE",i,r)
                #check if on the last row and the object is a pawn 
                if self.board[i][r].__class__ == Pawn and i == len(self.board)-1:
                    #checks if the object is a black pawn 
                    if self.board[i][r].get_type() == "BLACK":
                            #checks if any pieces have already been captured or not
                        if (black["BLACK Knight"] == 0 and black["BLACK Queen"] == 0 and black["BLACK Bishop"] == 0 and black["BLACK Rook"] == 0):
                            pass
                        else:
                            #game can generate pieces now 
                            game.gen_true("BLACK", i, r)
                
    def gen(self, piece):
        #get the information for generating a piece 
        type, row, col, white, black = game.get_geninfo()
            
        #adjusts the captured pieces numbers on the right side 
        if type == "BLACK":
            if black["BLACK " + str(piece)[9:]] == 0:
                return     
            black["BLACK " + str(piece)[9:]]-=1 
        if type == "WHITE":
            if white["WHITE " + str(piece)[9:]] == 0:
                return
            white["WHITE " + str(piece)[9:]]-=1 
            
        #adds piece to the board
        self.board[row][col] = piece(type, row, col)
        
        #game is no longer generating piece 
        game.gen_false()
    
    #draw the board out 
    def draw(self):
        #temp variables for drawing squares on board and pieces 
        x = 0
        y = 0
        #8 by 8 grid 
        for row in range(8):
            for col in range(8):
                #create square moving left to right in a column
                self.tiles[row][col].draw(x,y)
                #draw it from the center if the place is not 'empty'
                if self.board[row][col] != "EMPTY":
                    self.board[row][col].draw(x + SCREEN_WIDTH/16, y + SCREEN_LENGTH/16) 
                x += SCREEN_WIDTH/8
            #start from left again and move one row down
            x= 0 
            y+= SCREEN_WIDTH/8
    
    # spot is selected by the user 
    def check_piece(self, row, col):
        #if not an empty spot check the pieces possibilities and map out with NEXT marking and the piece corresponds to who's turn it is
        if self.board[row][col] != "EMPTY" and self.board[row][col].get_type() == game.get_turn():
            #finds next locations 
            self.board[row][col].find_spot()
        
    #reset all tile colours when clicking again
    def reset_tiles(self): 
        for row in self.tiles:
            for col in row:
                col.change_col("RESET")
                
    #return the board
    def get_board(self):
        return self.board
    
    #return the tiles 
    def get_tiles(self):
        return self.tiles 
    
    #move the piece if the tile selected is red 
    def move_piece(self,row,col):
        #get the piece which is attempting to move 
        temp_row, temp_col = self.tiles[row][col].get_selected()
        game.captured(self.board[row][col].__repr__())   
        
        #change the pice out with the one attempting to move
        self.board[row][col] = self.board[temp_row][temp_col]
        #make the old location empty
        self.board[temp_row][temp_col] = "EMPTY"
        
        #update the position of the new one
        self.board[row][col].update_position(row, col) 
        
        #check if there are pawns at either side of the board 
        self.pawn_check()
        
        #play sound to move piece 
        sound()
            
        #change the turns
        if game.get_turn() == "BLACK":
            game.change_turn("WHITE")
            
        elif game.get_turn() == "WHITE":
            game.change_turn("BLACK")
 
    #get status of a checkmate  
    def get_checked(self):
        return self.check
    
    #make checkmate not True anymore 
    def reset_check(self):
        self.check = False 
    
    #check for a checkmate after turn is completed 
    def checkmate(self): 
        #loop through board 
        for row in self.board:
            for piece in row:
                # if piece is a king 
                if (piece.__class__) == King:
                    # if current king is the same type as the current turn
                    if piece.get_type() == game.get_turn():
                        #check for a checkmate 
                        if piece.check_checkmate():
                            #checkmate is true 
                            self.check = True   
    
    def remove_selectedtiles(self):
        #remove only selected red tiles 
        for i in range(len(self.tiles)):
            for  r in range (len(self.tiles[0])):
                #checks if tile has same color scheme as a red tile and then resets it 
                if (self.tiles[i][r].get_r() == 255) and (self.tiles[i][r].get_g() == 102) and (self.tiles[i][r].get_b() == 102):
                    self.tiles[i][r].change_col("RESET")
                
                
#each selected square in conjuction with board 
class Square:
    #instanciate object
    def __init__(self, col):
        #set the color of the tile by rgb
        if col == "WHITE":
            self.r = 245
            self.g = 234
            self.b = 205
            #keeps two sets of color to restore afterwards
            self.dr = 245
            self.dg = 234
            self.db = 205
        if col == "GREEN":
            self.r = 196
            self.g = 178
            self.b = 131
            #keeps two sets of color to restore afterwards
            self.dr = 196
            self.dg = 178
            self.db  = 131
         #dimensions of a tile 
        self.dim =  SCREEN_WIDTH/8
    
    #draw the square
    def draw(self, x, y):
        #fill the square with certain color
        fill(self.r, self.g, self.b)
        square(x, y, self.dim)
        #reset
        fill(255)
    
    #change the color of the tile 
    def change_col(self, colo, (row ,col) = (0,0)):
        #piece is selected
        if colo == "CURRENT":
            self.r = 152
            self.g = 251
            self.b = 152       
        #reset tile 
        if colo == "RESET":
            self.r = self.dr
            self.g = self.dg
            self.b = self.db
        #moveable location
        if colo == "NEXT":
            self.r = 255
            self.g = 102
            self.b = 102       
            self.selected = (row, col) 
    
    #get the red value
    def get_r(self):
        return self.r
    
    #get the green value 
    def get_g(self):
        return self.g

    #get the blue value
    def get_b(self):
        return self.b
    
    #return the location of the piece that made the tile selected
    def get_selected(self):
        return self.selected 

#all pieces on the board inherit this class
class Piece: 
    #inherit to all pieces 
    def __init__(self, type, row, col):
        #side of the player ie. black or white
        self.type = type 
        #location of piece 
        self.row = row
        self.col = col
        
    #return the type of piece.. white or black    
    def get_type(self):
        return self.type    
    
    #update the position of the piece if it moves 
    def update_position(self, row, col):
        self.row = row
        self.col = col
        
    #return the current location
    def get_location(self):
        return (self.row, self.col) 
    
    #what a piece is reprsented as in the interpreter
    def __repr__(self):
        return self.type + " " + str(self.__class__)[9:]

#Pawn piece 
class Pawn(Piece):        
    #when drawing pass in the current x and y values 
    def draw(self, x, y):
        global whitepawn, blackpawn
        #draw from the center
        imageMode(CENTER)
        
        #draw the shape based on its color 
        if self.type == "WHITE":
            image(whitepawn, x, y,80,80) 
        if self.type == "BLACK":
            image(blackpawn, x,y, 80, 80) 
            
        #reset it 
        imageMode(CORNER)
        
    #default -  not checking for checkmate
    def find_spot(self): 
        #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
    
        
        #if white or black change direction
        if game.get_turn() == "WHITE":
            const = -1
        if game.get_turn() == "BLACK":
            const = 1     

        
        #if the location ahead of the pawn is empty (1 move up) and not checking for checkmate          
        if temp_board[self.row+(const*1)][self.col] == "EMPTY":
            #turns piece CURRENT 
            temp_tiles[self.row][self.col].change_col("CURRENT")
            #make selectable 
            temp_tiles[self.row+(const*1)][self.col].change_col("NEXT",(self.row,self.col))
            
            #if on the starting row and the row two spots ahead is empty.. first row ahead must be free hence nested conditional
            if game.get_turn() == "WHITE":
                if (self.row + const*2) >= 0:
                    if temp_board[self.row+(const*2)][self.col] == "EMPTY" and self.row ==6:
                        #make selectable 
                        temp_tiles[self.row + (const*2)][self.col].change_col("NEXT",(self.row,self.col))
            if game.get_turn() == "BLACK":
                if (self.row +const*2) <= 7:
                    if temp_board[self.row+(const*2)][self.col] == "EMPTY" and self.row ==1:
                        #make selectable 
                        temp_tiles[self.row + (const*2)][self.col].change_col("NEXT",(self.row,self.col))
                
        #boundary detection and capture
        if self.col != 7:
            #spot to the right is occupied by piece and not off screen and not own piece
            if temp_board[self.row+(const*1)][self.col+1] != "EMPTY" and temp_board[self.row+(const*1)][self.col+1].get_type() != game.get_turn():
                temp_tiles[self.row+(const*1)][self.col+1].change_col("NEXT",(self.row,self.col))
                temp_tiles[self.row][self.col].change_col("CURRENT")

        if self.col != 0: 
            #spot to the left is occupied by piece and not off screen
            if temp_board[self.row+(const*1)][self.col-1] != "EMPTY" and temp_board[self.row+(const*1)][self.col-1].get_type() != game.get_turn():
                temp_tiles[self.row+(1*const)][self.col-1].change_col("NEXT",(self.row,self.col)) 
                temp_tiles[self.row][self.col].change_col("CURRENT")
        
class Knight(Piece):
    #when drawing pass in the current x and y values 
    def draw(self, x, y):
        global whiteknight, blackknight
        #draw from the center
        imageMode(CENTER)
        
        #draw the shape based on its color 
        if self.type == "WHITE":
            image(whiteknight, x, y,80,80) 
        if self.type == "BLACK":
            image(blackknight, x,y,80,80) 
            
        #reset it 
        imageMode(CORNER)
    
    def find_spot(self):
        #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
      
        #checks every single L shaped pattern 
        for row, col in [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]:
            if (self.row+row >= 0) and (self.row + row <= 7) and (self.col + col >= 0) and (self.col + col <=7):
                if temp_board[self.row+row][self.col+col] == "EMPTY" or temp_board[self.row+row][self.col+col].get_type() != game.get_turn():
                    #if not checking for position make availiable
                    temp_tiles[self.row+row][self.col+col].change_col("NEXT",(self.row,self.col))
                    temp_tiles[self.row][self.col].change_col("CURRENT") 
            

class Queen(Piece):
    #when drawing pass in the current x and y values 
    def draw(self, x, y):
        global whitequeen, blackqueen
        #draw from the centers
        imageMode(CENTER)
        
        #draw the shape based on its color 
        if self.type == "WHITE":
            image(whitequeen, x, y,80,80) 
        if self.type == "BLACK":
            image(blackqueen, x,y,80,80) 
            
        #reset it 
        imageMode(CORNER)

    def find_spot(self):
       #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
        
        #diagonal check (loops through each vector) 
        for row, col in [(1,1), (-1,1), (-1,-1), (1,-1)]:
            #reset starting location
            temp_row = self.row 
            temp_col = self.col 
            #try 7 locations in that direction.. max num of moves at the corners is 7 tiles 
            for r in range(7):
                temp_row += row
                temp_col += col
                #checks if in boundaries                 
                if (temp_row >= 0) and (temp_row <= 7) and (temp_col >= 0) and (temp_col <=7): 
                    #if it is not on checkmode and there is an empty spot... highlight piece green and empty space red
                    if temp_board[temp_row][temp_col] == "EMPTY":
                        temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                        temp_tiles[self.row][self.col].change_col("CURRENT")
                    
                    #if it is not on checkmode and there is a piece to take... highlight piece green and other piece red
                    elif temp_board[temp_row][temp_col].get_type() != game.get_turn():
                         temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                         temp_tiles[self.row][self.col].change_col("CURRENT")
                         #break the loop and check other direction
                         break
                    # none of the options are viable.. break direction
                    else:
                        break
               #outside of boundaries 
                else:
                    break

        #horiztonal, vertical check (loop through each direction) 
        for row, col in [(0,1), (0,-1), (1,0), (-1,0)]:
            #reset to starting position
            temp_row = self.row 
            temp_col = self.col 
            for r in range(7):
                temp_row += row 
                temp_col += col
                #inside of all the boundaires 
                if (temp_row >= 0) and (temp_row <= 7) and (temp_col >= 0) and (temp_col <=7):
                   #normal check for empty spaces.. turn piece green and highlight emptyspace red 
                   if temp_board[temp_row][temp_col] == "EMPTY":
                        temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                        temp_tiles[self.row][self.col].change_col("CURRENT") 
                   
                   #normal check for any pieces 
                   elif temp_board[temp_row][temp_col].get_type() != game.get_turn():
                        temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                        temp_tiles[self.row][self.col].change_col("CURRENT")
                        break
                  #no options are viable.. stop checking from this direction 
                   else:
                       break
               #direction is not in boundaries 
                else:
                    break 
                        

class King(Piece):
    #when drawing pass in the current x and y values 
    def draw(self, x, y):
        global whiteking, blackking
        #draw from the center
        imageMode(CENTER)
        
        #draw the shape based on its color 
        if self.type == "WHITE":
            image(whiteking, x, y,80,80) 
        if self.type == "BLACK":
            image(blackking, x,y,80,80) 
            
        #reset it 
        imageMode(CORNER)
    
    #find spot of king 
    def find_spot(self,finding=True ):
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
        #if the game ends or not... checkmate or not
        win = True
        
        #loops through each surrounding location of king 
        for row, col in [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]:
            #check if place is on the board
            if (self.row +row >= 0) and (self.row +row  <= 7) and (self.col +col >= 0) and (self.col +col <=7):
                #check if all surrounding spots cannot be checked by an opposing piece, if it is, then it isn't highlighted
                if self.diagonal_check(self.row+row, self.col+col) and self.horizontal_check(self.row+row, self.col+col) and self.knight_check(self.row+row, self.col+col) and self.pawn_check(self.row+row, self.col+col) and self.king_check(self.row+row, self.col+col): 
                       #if the next location is empty 
                    if temp_board[self.row+row][self.col+col] == "EMPTY":
                        #if a normal check is happening (finding = True) all pieces will be highlighted
                        if finding:
                            temp_tiles[self.row+row][self.col+col].change_col("NEXT", (self.row, self.col))
                            temp_tiles[self.row][self.col].change_col("CURRENT") 
                        win = False
                    
                     #next location has a piece on it 
                    elif temp_board[self.row+row][self.col+col].get_type() != game.get_turn():
                         #highlight pieces 
                         if finding:
                            temp_tiles[self.row+row][self.col+col].change_col("NEXT",(self.row, self.col))
                            temp_tiles[self.row][self.col].change_col("CURRENT") 
                         win = False 
        #helps determine if game is checked or not 
        if win:
            return True 
   
   # check if there is a checkmate (scenario 1)         
    def check_checkmate(self): 
        #check if there is a checkmate
         if (not self.diagonal_check(self.row, self.col)) or (not self.horizontal_check(self.row, self.col)) or (not self.knight_check(self.row, self.col)) or (not self.pawn_check(self.row, self.col)) or (not self.king_check(self.row,self.col)):
           #piece mandatorily becomes green
            board.get_tiles()[self.row][self.col].change_col("CURRENT")
            #no other moveable positions 
            if self.find_spot(False):        
                game.change_screen("END")
            return True 
         else:
            return False

    #checks if the piece subbed in can be attacked diagnoally by bishop or queen
    def diagonal_check(self, row1, col1):
        #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
        
        #diagonal check (loops through each vector) 
        for row, col in [(1,1), (-1,1), (-1,-1), (1,-1)]:
            #reset starting location
            temp_row = row1
            temp_col = col1
            
            #checks through 7 board tiles in the same direction u
            for r in range(7):
                temp_row += row
                temp_col += col
                #checks if in boundaries                 
                if (temp_row >= 0) and (temp_row <= 7) and (temp_col >= 0) and (temp_col <=7): 
                    #if it is not on checkmode and there is an empty spot... highlight piece green and empty space red
                    if temp_board[temp_row][temp_col] == "EMPTY":
                        pass
                    #if the piece is the same as the one subbed in 
                    elif temp_board[temp_row][temp_col].get_type() == game.get_turn():
                        break 
                    #checks if the piece that can attack said row and column is a queen or bishop                            
                    elif ((temp_board[temp_row][temp_col].__class__) == Queen) or ((temp_board[temp_row][temp_col].__class__) == Bishop):
                        #checks if they are not the same type of piece or not 
                        if temp_board[temp_row][temp_col].get_type() != game.get_turn():
                            return False 
                    # none of the options are viable.. break direction
                    else:
                        break
               #outside of boundaries 
                else:
                    break        
        return True

    def horizontal_check(self, row1, col1):
        #gets the game and board 
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
        
        #diagonal check (loops through each vector) 
        for row, col in  [(0,1), (0,-1), (1,0), (-1,0)]:
            #reset starting location
            temp_row = row1
            temp_col = col1
            #checks all 7 tiles in same direction
            for r in range(7):
                temp_row += row
                temp_col += col
                #checks if in boundaries                 
                if (temp_row >= 0) and (temp_row <= 7) and (temp_col >= 0) and (temp_col <=7): 
                    #if it is not on checkmode and there is an empty spot... highlight piece green and empty space red
                    if temp_board[temp_row][temp_col] == "EMPTY":
                        pass    
                    #if the player is the same as the king 
                    elif temp_board[temp_row][temp_col].get_type() == game.get_turn():
                        break 
                   #if the player is a queen or a r ook 
                    elif ((temp_board[temp_row][temp_col].__class__) == Queen) or ((temp_board[temp_row][temp_col].__class__) == Rook):
                        #if they are not the same type of player 
                        if temp_board[temp_row][temp_col].get_type() != game.get_turn():
                            return False
                    # none of the options are viable.. break direction
                    else:
                        break
               #outside of boundaries 
                else:
                    break
        return True 
    
    #check if pawn can take passed in location
    def pawn_check(self, row1, col1):
        #get the board 
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
        
        #if it's white turn 
        if game.get_turn() == "WHITE":
            #piece does not go left off the board 
            if col1-1 >= 0:
                #the piece is a pawn
                if (temp_board[row1-1][col1-1].__class__) == Pawn:
                    #the piece is not the same as the king 
                    if temp_board[row1-1][col1-1].get_type() != game.get_turn():
                        return False        
            #piece does not go right off the board 
            if col1+1 <= 7:
                #the piece is a pawn
                if (temp_board[row1-1][col1+1].__class__) == Pawn:
                      #the piece is not the same as the king 
                    if temp_board[row1-1][col1+1].get_type() != game.get_turn():
                        return False        

        #it's black turn 
        if game.get_turn() == "BLACK":
            #piece does not right off the board
            if col1+1 <= 7:
                #the piece is a pawn 
                if (temp_board[row1+1][col1+1].__class__) == Pawn:
                    #the piece is not the same as the king checking 
                    if temp_board[row1+1][col1+1].get_type() != game.get_turn():
                        return False 
            #the piece does not go left off the board 
            if col1-1 >= 0:
                #the piece is a pawn 
                if (temp_board[row1+1][col1-1].__class__) == Pawn:
                    #the piece is not the same as the king checking 
                    if temp_board[row1+1][col1-1].get_type() != game.get_turn():
                        return False    
        return True        
            
    def knight_check(self, row1, col1): 
        #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
      
        #checks every single L shaped pattern 
        for row, col in [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]:
            #check if the piece is within the board
            if (row1+row >= 0) and (row1 + row <= 7) and (col1 + col >= 0) and (col1 + col <=7):
                #check if the object is a knight
                if (temp_board[row1+row][col1+col].__class__) == Knight:
                    #checks if the piece is not the same as king 
                    if temp_board[row1+row][col1+col].get_type() != game.get_turn():
                        return False 
            
        return True
    
    def king_check(self, row1, col1):    
        #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
      
      #checks for opposing in all the following locations realtive to the current 
        for row, col in [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]:
            #king is on the board
            if (row1 +row >= 0) and (row1 +row  <= 7) and (col1 +col >= 0) and (col1 +col <=7):
                #object is a king 
                if (temp_board[row1+row][col1+col].__class__) == King:
                    #checks if this king is not the same as the other king 
                    if temp_board[row1+row][col1+col].get_type() != game.get_turn():
                        return False 
        return True
                
class Rook(Piece):        
    #when drawing pass in the current x and y values 
    def draw(self, x, y):
        global whiterook, blackrook
        #draw from the center
        imageMode(CENTER)
        
        #draw the shape based on its color 
        if self.type == "WHITE":
            image(whiterook, x, y, 80,80) 
        if self.type == "BLACK":
            image(blackrook, x,y, 80, 80) 

        #reset it 
        imageMode(CORNER)
        
    def find_spot(self):
        #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()

        #horiztonal, vertical check (loop through each direction) 
        for row, col in [(0,1), (0,-1), (1,0), (-1,0)]:
            #reset to starting position
            temp_row = self.row 
            temp_col = self.col 
            for r in range(7):
                temp_row += row 
                temp_col += col
                #inside of all the boundaires 
                if (temp_row >= 0) and (temp_row <= 7) and (temp_col >= 0) and (temp_col <=7):
                
                   #normal check for empty spaces.. turn piece green and highlight emptyspace red 
                   if temp_board[temp_row][temp_col] == "EMPTY":
                        temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                        temp_tiles[self.row][self.col].change_col("CURRENT") 
                   
                   #normal check for any pieces 
                   elif temp_board[temp_row][temp_col].get_type() != game.get_turn():
                        temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                        temp_tiles[self.row][self.col].change_col("CURRENT")
                        break
                  #no options are viable.. stop checking from this direction 
                   else:
                       break
               #direction is not in boundaries 
                else:
                    break                                         
        
class Bishop(Piece):       
    #when drawing pass in the current x and y values 
    def draw(self, x, y):
        global whitebishop, blackbishop
        #draw from the center
        imageMode(CENTER)
        
        #draw the shape based on its color 
        if self.type == "WHITE":
            image(whitebishop, x, y,80,80) 
        if self.type == "BLACK":
            image(blackbishop, x,y,80,80) 
            
        #reset it 
        imageMode(CORNER)
        
    def find_spot(self):
        #gets the board
        temp_board = board.get_board() 
        temp_tiles = board.get_tiles()
        
       #diagonal check (loops through each vector) 
        for row, col in [(1,1), (-1,1), (-1,-1), (1,-1)]:
            #reset starting location
            temp_row = self.row 
            temp_col = self.col 
            
            for r in range(7):
                temp_row += row
                temp_col += col
                #checks if in boundaries                 
                if (temp_row >= 0) and (temp_row <= 7) and (temp_col >= 0) and (temp_col <=7): 
                    #if on checkmode and there is an empty square pass                                            

                    #if it is not on checkmode and there is an empty spot... highlight piece green and empty space red
                    if temp_board[temp_row][temp_col] == "EMPTY":
                        temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                        temp_tiles[self.row][self.col].change_col("CURRENT")
                    
                    #if it is not on checkmode and there is a piece to take... highlight piece green and other piece red
                    elif temp_board[temp_row][temp_col].get_type() != game.get_turn():
                         temp_tiles[temp_row][temp_col].change_col("NEXT",(self.row,self.col))
                         temp_tiles[self.row][self.col].change_col("CURRENT")
                         #break the loop and check other direction
                         break
                    # none of the options are viable.. break direction
                    else:
                        break
               #outside of boundaries 
                else:
                    break
            
        
##################################
# functions 

#plays noise for piece moving
def sound():
    add_library("minim")
    minim=Minim(this)
    sound = minim.loadFile("move.mp3")
    sound.play()   #plays once only instead of loop


##################################
# object creation & variables 

#screen dimensions 
SCREEN_WIDTH = 750
SCREEN_LENGTH = 750

#create game object
game = Game()

#creates board object
board = Board()

##################################
# processing 

#screen setup and import of media
def setup():
    global whitepawn, blackpawn, whiteknight, blackknight, whitequeen, blackqueen, whiteking, blackking, whiterook, blackrook, whitebishop, blackbishop, whitepanel,blackpanel, select1, select2, homeimg, whiteimg, blackimg, tie, instructions
    size(SCREEN_WIDTH+300, SCREEN_LENGTH) 
    
    
    #play jeapordy music    
    add_library("minim") #jeapordy background music
    minim=Minim(this)
    sound = minim.loadFile("game.mp3") 
    sound.loop()
    
    #select screens 
    select1 = loadImage('select1.png')
    select2 = loadImage('select2.png')
    
    #import pawn images 
    whitepawn = loadImage('wp.png')
    blackpawn = loadImage('bp.png')
    
    #import knight images 
    whiteknight = loadImage('wN.png')
    blackknight = loadImage('bN.png')
    
    #import queen images
    whitequeen = loadImage('wQ.png')
    blackqueen = loadImage('bQ.png')
    
    #import king images
    whiteking = loadImage('wK.png')
    blackking = loadImage('bK.png')
    
    #import rook images
    whiterook = loadImage('wR.png')
    blackrook = loadImage('bR.png')
    
    #import bishop images
    whitebishop = loadImage('wB.png')
    blackbishop = loadImage('bB.png')
    
    #import side panel
    whitepanel = loadImage('whitepanel.png')
    blackpanel = loadImage('blackpanel.png')
    
    #screens
    homeimg = loadImage("home.png")
    whiteimg = loadImage("white.png")
    blackimg = loadImage("black.png")
    instructions = loadImage("instructions.png")
    tie = loadImage('tie.png')
    
    
#runs the game 
def draw():
    #run the game manager 
    game.run()    
    
#check for mouse clicks
def mousePressed():
    #if on the game screen 
    if game.get_screen() == "GAME" and mouseX < SCREEN_WIDTH:
        #gets the row and col 
        row = mouseY//(SCREEN_WIDTH/8)
        col = mouseX//(SCREEN_LENGTH/8)
        #clicking selected tile   
        if not game.get_gen():
            #if checkmate 
            if board.get_checked():
                #spot selected is green.. find red spots 
                if (board.get_tiles()[row][col].get_r() == 152) and (board.get_tiles()[row][col].get_g() == 251) and (board.get_tiles()[row][col].get_b() == 152):
                    board.get_board()[row][col].find_spot()
                # if spots are red 
                elif (board.get_tiles()[row][col].get_r() == 255) and (board.get_tiles()[row][col].get_g() == 102) and (board.get_tiles()[row][col].get_b() == 102):
                    #turn off checkmate
                    board.reset_check()     
                    #move the piece 
                    board.move_piece(row,col)
                    #reset all the tiles 
                    board.reset_tiles()
                    #check for a checkmate
                    board.checkmate()
                    #remove all selected tiles 
                else: 
                    #remove all the red tiles 
                    board.remove_selectedtiles()
    
            else:
                #if place selected is green and no checkmate 
                if (board.get_tiles()[row][col].get_r() == 255) and (board.get_tiles()[row][col].get_g() == 102) and (board.get_tiles()[row][col].get_b() == 102):
                    #move piece 
                    board.move_piece(row,col)
                    #reset all the tiles 
                    board.reset_tiles()
                    #check for a checkmate
                    board.checkmate() 
                    
                else:
                    #reset all colours previously 
                    board.reset_tiles()   
                    #highlights the position the player is selecting 
                    board.check_piece(row, col)
    
def keyPressed():
    global game, board   
    
    #if on gamescreen
    if game.get_screen() == "GAME":
        #if piece is on generate mode 
        if game.get_gen():
            #generate queen
            if key == "q" or key == "Q":
                board.gen(Queen)
            #generate king 
            if key == "k" or key == 'K':
                board.gen(Knight)
            #generate rookie
            if key == 'r' or key == 'R':
                board.gen(Rook)
            #generate bishop
            if key == 'b' or key == "B":
                board.gen(Bishop)
        #instruction menu
        if key == "I" or key == "i":
            game.change_screen("INSTRUCT")
            
        #return home
        if key == "H" or key == "h":
            game.change_screen("HOME")
            game = Game()
            board = Board()
        
    #if on the home page
    if game.get_screen() == "HOME":
     #   Switch to game 
       if keyCode == RIGHT:
           game.change_screen("GAME")
        #switch to instructions
       if keyCode == LEFT:
           game.change_screen("INSTRUCT")   
           
    #on instruction page chance to game 
    if game.get_screen() == "INSTRUCT":
        if keyCode == DOWN:
            game.change_screen("GAME")  
            
    #change it to the home and reset all variables 
    if (game.get_screen() == "END") or (game.get_screen() == "TIE"):
        if keyCode == DOWN:
            game.change_screen("HOME")
            game = Game()
            board = Board()
