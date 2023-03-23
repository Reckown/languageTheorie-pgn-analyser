import constants.pgnInputs
import lexer
from constants import pgnInputs
import parser
import sys


def createLexer():
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgnInputs.inputFour)


def createParser(pgn):
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgn)
    if len(lex.error) > 0:
        # print("Syntax error in output : ")
        for error in lex.error:
            print("error: " + error)
    else:
        print("Most nested comment without capture : "+ str(lex.maxLevel))
        pars = parser.Parser()
        result = pars.parser.parse(pgn)
        # print(result)
        if pars.hasError:
            print("Invalid PGN File :( ")
        else:
            print("Valid PGN")


# testRegEx()
# createLexer()
# createParser()
# test_lexer()

# createParser(pgnInputs.inputFour)

# Handling the user arguments
if sys.argv[1] == '-pgn':
    print("Validation of the pgn in argument...")
    if sys.argv[2] is not None:
        createParser(sys.argv[2])
    else:
        print("No pgn, please add a pgn as the second argument")
elif sys.argv[1] == '-file':
    print("Validation du fichier : ")
    if sys.argv[2] is None:
        print("Please enter a file name as the second argument")
    else:
        f = open(sys.argv[2], "r")
        createParser(f.read())
else:
    print("Invalid argument, 1st argument should be : -pgn or -file")