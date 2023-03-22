import lexer
from constants import pgnInputs
import parser


def createLexer():
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgnInputs.inputFour)


def createParser():
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgnInputs.inputFour)
    if len(lex.error) > 0:
        print("Syntax error in output : ")
        for error in lex.error:
            print("error: "+error)
    else:
        pars = parser.Parser()
        result = pars.parser.parse(pgnInputs.inputFour)
        print(result)
        if pars.hasError:
            print("Invalid PGN File :( ")
        else:
            print("Valid PGN")


# testRegEx()
# createLexer()
createParser()
# test_lexer()
