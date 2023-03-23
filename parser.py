import lexer
import ply.yacc as yacc


# -----------------------------------------------------------------------------
# tokens = ['HEADER', 'TURN', 'TURN_RECOVERY', 'SHORT_CASTLE',
#           'LONG_CASTLE', 'COMMENTARY', 'VICTORY', 'MOVE']
#
# log           : game

# game          : descriptor play game
#               | empty
#
# descriptor    : HEADER descriptor
#               | empty
#
# play          : turn play
#               | empty result
#               | ending_turn result
#
# turn          : TURN move_p1 com_p1 move_p2 com_p2
#
# ending_turn   : TURN move_p1 com_p1_final
#
# com_p1_final  : commentary
#               | empty
#
# com_p1        : commentary TURN_RECOVERY
#               | empty
#
# com_p2        : commentary
#               | empty
#
# move_p1       : MOVE
#               | LONG_CASTLE
#               | SHORT_CASTLE
#
# move_p2       : MOVE
#               | LONG_CASTLE
#               | SHORT_CASTLE
#
# commentary    : COMMENTARY
#
# result        : VICTORY
#
# empty         : pass
# -----------------------------------------------------------------------------

class Parser(object):
    # Tokens defined in lexer
    tokens = lexer.Lexer.tokens
    # Turn counter in the game
    currentTurn = 1
    # Castle counter player one
    castlePlayerOne = 0
    # Castle counter player two
    castlePlayerTwo = 0
    # True if there is an error in the pgn
    hasError = False

    def __init__(self):
        self.lexer = lexer.Lexer()
        self.parser = yacc.yacc(module=self)

    # Empty production
    def p_log(self, p):
        """log : game"""
        p[0] = ('game is present', p[1])

    def p_game(self, p):
        """game : descriptor play game"""
        p[0] = ('game started', p[1], p[2], p[3])

    def p_game_empty(self, p):
        """game : empty"""
        p[0] = (p[1])

    def p_descriptor(self, p):
        """descriptor : HEADER descriptor"""
        p[0] = ('descriptor', p[1], p[2])

    def p_descriptor_empty(self, p):
        """descriptor : empty"""
        p[0] = p[1]

    def p_play(self, p):
        """play : turn play"""
        p[0] = ('play', p[1], p[2])

    def p_play_empty(self, p):
        """play : empty result"""
        p[0] = (p[1], p[2])

    def p_play_final(self, p):
        """play : ending_turn result"""
        p[0] = ('end of', p[1], p[2])

    def p_turn(self, p):
        """turn : TURN move_p1 com_p1 move_p2 com_p2"""
        nbTurn = p.slice[1].value[:-2]
        if int(nbTurn) == self.currentTurn:
            self.currentTurn = self.currentTurn + 1
            p[0] = ('turn', p[1], p[2], p[3], p[4], p[5])
        else:
            self.p_error(p)
            # print("\033[91mError in player 1 turn number ! Turn : " + nbTurn)

    def p_ending_turn(self, p):
        """ending_turn : TURN move_p1 com_p1_final"""
        p[0] = ('final p1 turn', p[1], p[2], p[3])

    def p_com_p1_final(self, p):
        """com_p1_final : commentary
                        | empty"""
        p[0] = ('final commentary', p[1])

    def p_com_p1(self, p):
        """com_p1 : commentary TURN_RECOVERY"""
        nbTurn = p.slice[2].value[:-3]
        if int(nbTurn) == self.currentTurn:
            p[0] = ('com_p1', p[1], p[2])
        else:
            self.p_error(p)
            # print("\033[91mError in player 2 turn number ! Turn : " + nbTurn)

    def p_com_p1_empty(self, p):
        """com_p1 : empty
           """
        p[0] = p[1]

    def p_com_p2(self, p):
        """com_p2 : commentary"""
        p[0] = ('com_p2', p[1])

    def p_com_p2_empty(self, p):
        """com_p2 : empty
           """
        p[0] = p[1]

    def p_commentary(self, p):
        """commentary : COMMENTARY"""
        p[0] = ('commentary content', p[1])

    def p_move_p1(self, p):
        """move_p1 : MOVE
                   | LONG_CASTLE
                   | SHORT_CASTLE"""
        # We check how many time the player one has castle. If he castle more than once
        # We raise an error
        if p.slice[1].type == "SHORT_CASTLE" or p.slice[1].type == "LONG_CASTLE":
            self.castlePlayerOne = self.castlePlayerOne + 1
            if self.castlePlayerOne > 1:
                self.p_error(p)
                # print("\033[91mTwo casle for player One !")
            else:
                p[0] = ('move_p1', p[1])
        else:
            p[0] = ('move_p1', p[1])

    def p_move_p2(self, p):
        """move_p2 : MOVE
                   | LONG_CASTLE
                   | SHORT_CASTLE"""
        if p.slice[1].type == "SHORT_CASTLE" or p.slice[1].type == "LONG_CASTLE":
            self.castlePlayerTwo = self.castlePlayerTwo + 1
            if self.castlePlayerTwo > 1:
                self.p_error(p)
                # print("\033[91mTwo casle for player Two !")
            else:
                p[0] = ('move_p2', p[1])
        else:
            p[0] = ('move_p2', p[1])

    def p_result(self, p):
        """result : VICTORY"""
        # If we start another game we put everything to 0
        self.currentTurn = 1
        self.castlePlayerOne = 0
        self.castlePlayerTwo = 0
        p[0] = ('result', p[1])

    def p_empty(self, p):
        """empty :"""
        # print("p_empty")
        pass

    # Error rule for syntax errors
    def p_error(self, p):
        self.hasError = True
