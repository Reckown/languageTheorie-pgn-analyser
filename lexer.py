import ply.lex as lex
import re

from constants.regExConstants import REGEX_END_GAME, REGEX_TURN, REGEX_TURN_SECOND, REGEX_ROC_LONG, REGEX_ROC_SHORT, \
    REGEX_DESCRIPTORS, REGEX_COMMENTARY, REGEX_ACTION


class Lexer:
    # List of token names.
    # Regular expression rules for simple tokens
    t_VICTORY = REGEX_END_GAME

    t_TURN = REGEX_TURN

    t_TURN_RECOVERY = REGEX_TURN_SECOND

    t_LONG_CASTLE = REGEX_ROC_LONG

    t_SHORT_CASTLE = REGEX_ROC_SHORT

    t_MOVE = REGEX_ACTION

    t_HEADER = REGEX_DESCRIPTORS

    maxLevel = 0

    def t_COMMENTARY(self, t):
        r"""\(.*?\)|\{.*?\}"""
        errorComm = self.handleCommentary(t)
        if not errorComm:
            print("WARNING: inside one of the commentary, bracket not matching")
        return t

    def handleCommentary(self, t):
        # When we get a commentary we want to handle it,
        # Then we ignore it

        # If true then we ended this commentary
        end = False

        # Stack to get the things inside
        stack = []

        # Current level of depth in the nested commentary
        currentLevel = 0

        # Starting id search
        startingId = -1

        # Ending id search
        endingId = 0

        # Regex to get move without capture: (?<=\s)[NBQRK]?[0-8a-h]?[a-h][1-8](\+{0,2})[?!]?(?=\s)
        regExMoveWithoutCapture = '[NBQRK]?[0-8a-h]?[a-h][1-8](\+{0,2})[?!]?'

        # Regex to get move with capture : (?<=\s)[NBQRK]?[0-8a-h]?x[a-h][1-8](\+{0,2})[?!]?(?=\s)
        regExMoveWithCapture = '[NBQRK]?[0-8a-h]?x[a-h][1-8](\+{0,2})[?!]?'

        while not end:
            for i in range(len(t.value)):
                if t.value[i] in ["(", "{"]:
                    # Push the element in the stack
                    stack.append(t.value[i])
                    currentLevel = currentLevel + 1
                    if startingId != -1:
                        endingId = i
                        newString = t.value[startingId:endingId]
                        # print("1- "+newString, currentLevel)
                        m = re.search(regExMoveWithCapture, newString)
                        if m is None:
                            m = re.search(regExMoveWithoutCapture, newString)
                            if m is not None:
                                if currentLevel > self.maxLevel:
                                    self.maxLevel = currentLevel
                    startingId = i
                else:
                    # IF current character is not opening
                    # bracket, then it must be closing.
                    # So stack cannot be empty at this point.
                    if not stack:
                        return False
                    if t.value[i] == ')' or t.value[i] == ']' or t.value[i] == '}':
                        change = False
                        current_char = stack.pop()
                        if current_char == '(':
                            if t.value[i] != ")":
                                return False
                            else:
                                change = True
                        if current_char == '{':
                            if t.value[i] != "}":
                                return False
                            else:
                                change = True
                        if change:

                            # We search between the starting and the ending id :
                            endingId = i
                            newString = t.value[startingId:endingId]
                            # print("2- "+newString, currentLevel)
                            m = re.search(regExMoveWithCapture, newString)
                            if m is None:
                                m = re.search(regExMoveWithoutCapture, newString)
                                if m is not None:
                                    if currentLevel > self.maxLevel:
                                        self.maxLevel = currentLevel
                            startingId = i
                            currentLevel = currentLevel - 1
                # Check Empty Stack
            if stack:
                return False
            return True

    t_ignore = ' \t \n'

    tokens = ['VICTORY', 'TURN', 'TURN_RECOVERY', 'LONG_CASTLE', 'SHORT_CASTLE',
              'MOVE', 'HEADER', 'COMMENTARY']

    # Error handling rule
    def t_error(self, t):
        if self.lastErrorPos is None:
            self.lastErrorPos = t.lexpos
            self.lastErrorLine = t.lineno
            self.error.append(t.value[0])
        else:
            if self.lastErrorPos == t.lexpos - 1:
                self.error[self.numberError] += t.value[0]
            else:
                self.numberError = self.numberError + 1
                self.error.append(t.value[0])
            self.lastErrorPos = t.lexpos
            self.lastErrorLine = t.lineno
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = None
        self.error = []
        self.lastErrorPos = None
        self.lastErrorLine = None
        self.numberError = 0
        self.tokenList = []

    def createLexer(self):
        self.lexer = lex.lex(module=self)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            self.tokenList.append(tok)
            if not tok:
                break
            # print(tok)
        ## print(self.tokenList)
