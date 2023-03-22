###############################
#            PRINT            #
###############################
import lexer
import parser
from constants import pgnInputs


def test_print(pgn):
    for game in pgn:
        print(game[0])

        lex = lexer.Lexer()
        lex.createLexer()
        lex.test(game[1])
        if len(lex.error) > 0:
            print("Syntax error in output : ")
            for error in lex.error:
                print("error: " + error)
        else:
            pars = parser.Parser()
            result = pars.parser.parse(game[1])
            print(result)
            if pars.hasError:
                print("Invalid PGN File :( ")
            else:
                print("Valid PGN")

    # @TODO


###############################
#            INPUT            #
###############################

def test_inv_moves():
    samples = [
        [
            "Invalid (1 move)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            False
        ],
        [
            "Invalid (3 moves)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 f4 f4 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            False
        ],
    ]

    print("MOVES")
    test_print(samples)


def test_inv_win():
    samples = [
        [
            "Invalid (move after win)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 exf4 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0 e6
            """,
            False
        ],
        [
            "Invalid (turn after win)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 exf4 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0 e6 24. e6 e6
            """,
            False
        ],
        [
            "Invalid (syntax)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 exf4 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-1
            """,
            False
        ],
    ]

    print("WIN")
    test_print(samples)


def test_inv_castle():
    samples = [
        [
            "Invalid (2 castle on 1 player)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 O-O 2. f4 O-O-O 3. Bc4 Qh4+ 4. Kf1 b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            False
        ],
        [
            "Invalid (3 castles)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 O-O 2. O-O-O f4 3. Bc4 Qh4+ 4. O-O b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            False
        ],
        [
            "Invalid (syntax)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 O-O-O-O 2. f4 A-A-A 3. Bc4 Qh4+ 4. O-O- b5? 5. Bxb5 O-O 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 A-A 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            False
        ],
    ]

    print("MOVES")
    test_print(samples)


def test_valid():
    samples = [
        [
            "Valid (normal)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            True
        ],
        [
            "Valid (descriptors at the end)",
            """                
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0

            """,
            True
        ],
        [
            "Valid (no descriptors)",
            """
                1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            True
        ],
        [
            "Valid (move markers)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5? 5. Bxb5 Nf6 6. Nf3? Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6! 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6! 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            True
        ],
        [
            "Valid (detailled moves)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf8 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Q0xh5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. Nh8 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 0-1
            """,
            True
        ],
        [
            "Valid (turn recoveries)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 2. f4 {This is an example of a commentary} 2... exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 (comment.) 16... Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            True
        ],
        [
            "Valid (castle)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 O-O-O 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. O-O Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1/2-1/2
            """,
            True
        ],
        [
            "Valid (commentaries)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 {{} This is a nested [(commentary) which 1. ] 1... is ( working {)}} 1... e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            True
        ],
        [
            "Valid (real game #1)",
            """
                [Event "UK vs UKR Solidarity m"]
                [Site "London ENG"]
                [Date "2023.03.21"]
                [Round "1.1"]
                [White "Volokitin, Andrei"]
                [Black "Adams, Michael"]
                [Result "1/2-1/2"]
                [WhiteTitle "GM"]
                [BlackTitle "GM"]
                [WhiteElo "2665"]
                [BlackElo "2687"]
                [ECO "C50"]
                [Opening "Giuoco Piano"]
                [WhiteFideId "14107090"]
                [BlackFideId "400041"]
                [EventDate "2023.03.21"]

                1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. O-O d6 5. c3 Nf6 6. d3 a5 7. Re1 Ba7 8. Na3
                O-O 9. h3 h6 10. Nb5 Bb6 11. Be3 Bxe3 12. Rxe3 Re8 13. Qb3 Be6 14. Bxe6 Rxe6 15.
                c4 a4 16. Qd1 Qd7 17. Rc1 Ra6 18. Qe2 Nh5 19. g3 Nf4 20. Qf1 Rg6 21. Nh4 Rg5 22.
                Kh2 Rh5 23. Nf5 Ne6 24. f4 Rb6 25. Qf3 Rxf5 26. exf5 Ned4 27. Nxd4 Nxd4 28. Qf2
                exf4 29. gxf4 Nxf5 30. Re4 Kh7 31. Rc2 c5 32. Rce2 d5 33. cxd5 Rd6 34. Re5 f6
                35. Re8 Rxd5 36. Qg2 Rxd3 37. Qe4 Rd4 38. Qe6 Qxe6 39. R8xe6 b5 40. Rc6 c4 41.
                Rf2 b4 42. Rc5 Ne3 43. f5 b3 44. axb3 cxb3 45. Ra5 h5 46. Re2 Rd3 47. Rf2 Rd4
                48. Re2 Rd3 49. Rf2 Rd4 1/2-1/2
            """,
            True
        ],
        [
            "Valid (real game #2)",
            """
                [Event "American Cup Champ"]
                [Site "Saint Louis USA"]
                [Date "2023.03.21"]
                [Round "3.1"]
                [White "Nakamura, Hikaru"]
                [Black "So, Wesley"]
                [Result "1/2-1/2"]
                [WhiteTitle "GM"]
                [BlackTitle "GM"]
                [WhiteElo "2768"]
                [BlackElo "2761"]
                [ECO "C65"]
                [Opening "Ruy Lopez"]
                [Variation "Berlin defence"]
                [WhiteFideId "2016192"]
                [BlackFideId "5202213"]
                [EventDate "2023.03.17"]

                1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. d3 Bc5 5. O-O Nd4 6. Be3 Nxf3+ 7. Qxf3 Bxe3 8.
                Qxe3 c6 9. Bc4 d6 10. Nd2 Qb6 11. Qxb6 axb6 12. f4 exf4 13. Rxf4 b5 14. Bb3 Be6
                15. a3 O-O 16. Raf1 Rae8 17. Bxe6 Rxe6 18. Nf3 d5 19. e5 Nd7 20. d4 f6 21. h3
                Re7 22. exf6 Rxf6 23. Rxf6 Nxf6 24. Re1 Rxe1+ 25. Nxe1 Ne4 26. Nd3 Kf7 27. Kf1
                Ke6 28. Ke2 g5 29. g4 h6 30. Ke3 Kd6 31. Ne5 Ke6 32. Nd3 Kd6 33. Ne5 Ke6 34. Nd3 1/2-1/2
            """,
            True
        ],
        [
            "Valid (real game #3)",
            """
                [Event "American Cup Champ"]
                [Site "Saint Louis USA"]
                [Date "2023.03.21"]
                [Round "2.4"]
                [White "Caruana, Fabiano"]
                [Black "So, Wesley"]
                [Result "1/2-1/2"]
                [WhiteTitle "GM"]
                [BlackTitle "GM"]
                [WhiteElo "2766"]
                [BlackElo "2761"]
                [ECO "D26"]
                [Opening "QGA"]
                [Variation "classical variation"]
                [WhiteFideId "2020009"]
                [BlackFideId "5202213"]
                [EventDate "2023.03.17"]

                1. d4 d5 2. c4 dxc4 3. e3 Nf6 4. Nf3 e6 5. Bxc4 c5 6. Nc3 a6 7. Bb3 Nc6 8. O-O
                b5 9. Qe2 Bb7 10. Rd1 Be7 11. dxc5 Qc7 12. e4 O-O 13. e5 Nd7 14. Bf4 Nxc5 15.
                Bc2 Nb4 16. Rac1 Nxc2 17. Rxc2 Rac8 18. a3 Rfd8 19. Nd4 Qb6 20. Rcd2 Na4 21.
                Nxa4 bxa4 22. Qg4 Rd5 23. h4 Kh8 24. Be3 Qc7 25. Qf4 Kg8 26. Nf5 Rxd2 27. Nxe7+
                Qxe7 28. Rxd2 Bc6 29. Qg4 Kh8 30. Rd4 Rd8 31. Rf4 Qd7 32. Kh2 Qc7 33. Qh5 Be8
                34. Rb4 f6 35. Bb6 Bxh5 36. Bxc7 Rc8 37. Ba5 Be8 38. Rb6 Bc6 39. Rxa6 f5 40. f3
                h6 41. Kg3 Bd5 42. Bb4 Bb3 43. Ra7 Kg8 44. Bc3 Rd8 45. Kf2 Kh7 46. Rb7 Kg6 47.
                Bb4 Rc8 48. Ke3 Kh7 49. Bc3 Rd8 50. g4 fxg4 51. fxg4 Bd1 52. Rb4 h5 53. gxh5 Kh6
                54. Rb6 Bb3 55. Rb7 Kxh5 56. Rxg7 Kxh4 57. Bb4 Kh5 58. Bd6 Rc8 59. Bc7 Kh6 60.
                Rd7 Rg8 61. Ba5 Rg1 62. Rd8 Rd1 63. Rg8 Kh7 64. Rg4 Rd5 65. Bc3 Rd1 66. Ke2 Bc2
                67. Bd2 Rb1 68. Rb4 Rh1 69. Bc3 Kg6 70. Rb8 Kf5 71. Ke3 Rd1 72. Rf8+ Kg5 73. Bd2
                Kh5 74. Rg8 Rb1 75. Bc3 Rd1 76. Rg2 Rd3+ 77. Kf4 Bb3 78. Bd2 Bd5 79. Rh2+ Kg6
                80. Be3 Rb3 81. Rf2 Kf7 82. Kg5+ Ke8 83. Bd4 Rd3 84. Bc3 Rf3 85. Rh2 Kd7 86. Rh4
                Bb3 87. Rb4 Rf5+ 88. Kg6 Rf1 89. Rb6 Rg1+ 90. Kf6 Rf1+ 91. Kg5 Rf5+ 92. Kg4 Bd1+
                93. Kg3 Bb3 94. Rd6+ Kc7 95. Rd2 Rf1 96. Rh2 Rf7 97. Bd2 Rf1 98. Be3 Kc6 99. Rh4
                Bd5 100. Bf2 Bb3 101. Kf3 Rb1 102. Bd4 Re1 103. Bc3 Bd5+ 104. Kf2 Re4 105. Rh8
                Bb3 106. Rd8 Bd5 107. Rd6+ Kb5 108. Kg3 Bb3 109. Rd8 Bd5 110. Kf2 Bb3 111. Rb8+
                Kc6 112. Ra8 Bd5 113. Ra6+ Kb5 114. Rd6 Bb3 115. Bd4 Bd5 116. Rb6+ Kc4 117. Bc3
                Kd3 118. Rb5 Re2+ 119. Kg3 Re4 120. Ra5 Bb3 121. Bb4 Kc2 122. Kf3 Bd5 123. Kf2
                Bb3 124. Bc3 Bd5 125. Kf3 1/2-1/2
            """,
            True
        ],
        [
            "Valid (multiple games)",
            """
                [Event "American Cup Champ"]
                [Site "Saint Louis USA"]
                [Date "2023.03.17"]
                [Round "1.1"]
                [White "Nakamura, Hikaru"]
                [Black "Sevian, Samuel"]
                [Result "1-0"]
                [WhiteTitle "GM"]
                [BlackTitle "GM"]
                [WhiteElo "2768"]
                [BlackElo "2687"]
                [ECO "C77"]
                [Opening "Ruy Lopez"]
                [Variation "Morphy defence, Duras variation"]
                [WhiteFideId "2016192"]
                [BlackFideId "2040506"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. d3 d6 6. c4 Bg4 7. h3 Bxf3 8. Qxf3
                Nd7 9. Be3 Be7 10. Nc3 Nf8 11. Ne2 Ne6 12. d4 exd4 13. Nxd4 Nxd4 14. Bxd4 O-O
                15. Bxc6 bxc6 16. Rd1 Re8 17. O-O Bf6 18. c5 Re6 19. Bxf6 Qxf6 20. Qxf6 gxf6 21.
                f3 Rb8 22. Rf2 Rb5 23. Rc2 dxc5 24. Rd7 Rd6 25. Rxc7 c4 26. Kf2 Rb6 27. Ke3 Kg7
                28. Ra7 Rd3+ 29. Kf4 Rd4 30. h4 Kg6 31. h5+ Kg7 32. Ra8 h6 33. a4 c5 34. a5 Rc6
                35. Rb8 Kh7 36. Ke3 Kg7 37. Ke2 Re6 38. g4 Rc6 39. Rd2 Rc7 40. Rb6 Rcd7 41. Rxd4
                cxd4 42. Rxa6 Rc7 43. Rd6 Rb7 44. Rb6 Rc7 45. a6 c3 46. bxc3 Rxc3 47. a7 Ra3 48.
                Rb7 Re3+ 49. Kd2 Ra3 50. Rc7 f5 51. e5 fxg4 52. fxg4 1-0

                [Event "American Cup Champ"]
                [Site "Saint Louis USA"]
                [Date "2023.03.18"]
                [Round "1.2"]
                [White "Sevian, Samuel"]
                [Black "Nakamura, Hikaru"]
                [Result "1/2-1/2"]
                [WhiteTitle "GM"]
                [BlackTitle "GM"]
                [WhiteElo "2687"]
                [BlackElo "2768"]
                [ECO "D37"]
                [Opening "QGD"]
                [Variation "4.Nf3"]
                [WhiteFideId "2040506"]
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. d4 Nf6 2. c4 e6 3. Nf3 d5 4. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Bb7 13. b4 c6 14. Qb3 a5 15. Rfd1
                axb4 16. axb4 Ra7 17. Ra1 Rfa8 18. Rxa7 Rxa7 19. Ne1 Ne4 20. Nxe4 dxe4 21. f3
                Nf6 22. fxe4 Nxe4 23. Nf3 Bc8 24. Qc2 Bf5 25. Ne5 Qf6 26. Bd3 Qg5 27. Re1 Ra1
                28. Rxa1 Qxe3+ 29. Kf1 Nd2+ 30. Qxd2 Qxd2 31. Ra8+ Kh7 32. Bxf5+ g6 33. Bd3 Qc1+
                34. Ke2 Qb2+ 35. Ke3 c5 36. bxc5 bxc5 37. Rd8 cxd4+ 38. Rxd4 Qxg2 39. Rd7 Qg1+
                40. Ke4 Qe1+ 41. Kd5 Qa5+ 42. Ke4 Qe1+ 43. Kd5 Qa5+ 44. Ke4 Qe1+ 1/2-1/2
            """,
            True
        ],
    ]

    print("VALID")
    test_print(samples)


def test_inv_commentaries():
    samples = [
        [
            "Invalid (2 following commentaries)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 {comm1} {comm2} e5 2. f4 (comm1) (comm2) exf4 3. Bc4 Qh4+ (comm1)(comm2) 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            False
        ],
        [
            "Invalid (commentaries not in the game)",
            """
                [Event "London 'Immortal game'"]
                {bad commentary}
                [Site "London"]
                {[also a bad commentary]}
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
                Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
                Bxf4 Qf6 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
                Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0
            """,
            False
        ],
        [
            "Invalid (syntax)",
            """
                [Event "London 'Immortal game'"]
                [Site "London"]
                [Date "1851.06.21"]
                [Round "?"]
                [White "Anderssen, Adolf"]
                [Black "Kieseritzky, Lionel Adalbert BF"]
                [Result "1-0"]
                [ECO "C33"]
                [PlyCount "45"]
                [EventDate "1851.06.21"]
                [EventType "game"]
                [EventRounds "1"]
                [EventCountry "ENG"]
                [Source "ChessBase"]
                [SourceDate "1999.07.01"]
                1. e4 e5 [bad commentary] 2. f4 exf4 {this is
            """,
            False
        ],
    ]

    print("COMMENTARIES")
    test_print(samples)


def test_inv_descriptors():
    samples = [
        [
            "Invalid (half before half after)",
            """
                [Event "American Cup Champ"]
                [Site "Saint Louis USA"]
                [Date "2023.03.17"]
                [Round "1.1"]
                [White "Aronian, Levon"]
                [Black "Dominguez Perez, Leinier"]
                [Result "1/2-1/2"]
                [WhiteTitle "GM"]
                [BlackTitle "GM"]
                [WhiteElo "2745"]
                [BlackElo "2743"]

                1. c4 e6 2. Nc3 d5 3. d4 Nf6 4. cxd5 exd5 5. Bg5 c6 6. e3 Bf5 7. Qf3 Bg6 8. Bxf6
                Qxf6 9. Qxf6 gxf6 10. Nf3 Nd7 11. Nh4 Be7 12. Ne2 f5 13. Nf3 Bb4+ 14. Kd1 Bd6
                15. Ne1 Ke7 16. Nd3 Bh5 17. f3 Bg6 18. Nef4 a5 19. Ke1 Nf8 20. g3 Ne6 21. Rc1
                Rhe8 22. Kf2 Kf6 23. Be2 Re7 24. Bd1 Kg7 25. Re1 Ree8 26. Re2 Re7 27. Rc3 Kf8
                28. a3 Bxf4 29. Nxf4 Nxf4 30. exf4 f6 31. Rb3 Rxe2+ 32. Bxe2 b5 33. Rc3 Be8 34.
                Bd3 Bd7 35. g4 Ke7 36. Bxf5 Bxf5 37. gxf5 Kd7 38. Rc1 a4 39. Rg1 Re8 40. h4 Re7
                41. h5 c5 42. dxc5 Kc6 43. h6 Kxc5 44. Rg6 Kc4 45. Rxf6 Rb7 46. Re6 Kb3 47. Re2
                Rb6 48. Ke3 Rf6 49. Rg2 Rf8 50. Kd4 Rxf5 51. Rf2 Ka2 52. Ke3 Kb3 53. Rd2 Kc4 54.
                Rd3 Kc5 55. Rc3+ Kd6 56. Rc8 Rf6 57. Rd8+ Kc5 58. Rc8+ Kd6 59. Re8 Rxh6 60. f5
                Rh4 61. Rd8+ Ke5 62. f4+ Kxf5 63. Rxd5+ Kf6 64. Rxb5 Rh2 65. Ke4 Re2+ 66. Kf3
                Rd2 67. Kg3 Re2 68. Rb7 Kf5 69. Kf3 Rh2 70. Rb5+ Kf6 71. Ke4 Re2+ 72. Kd3 Rf2
                73. Rb7 h5 74. Ke3 Rg2 75. Kf3 Rd2 76. Kg3 Re2 77. Rb6+ Kf5 78. Rb5+ Kf6 79. Kf3
                Rd2 80. Ke3 Rg2 81. Kf3 Rd2 82. Ke4 Re2+ 83. Kd3 Rf2 84. Ke3 Rg2 85. Rb6+ Kf5
                86. Kf3 Rd2 87. Rb4 Rc2 88. Kg3 Rd2 89. Rb8 Re2 90. Rf8+ Kg6 91. Rg8+ Kf6 92.
                Rb8 Kf5 93. Rb4 Rd2 94. Rxa4 Rxb2 95. Ra5+ Kf6 96. Kf3 Rb3+ 97. Ke4 h4 98. Rh5
                Rxa3 99. Rh6+ Kf7 100. Rh7+ Kf6 101. Rh6+ Kf7 102. Rh7+ Kf6 103. Rh6+ 1/2-1/2

                [ECO "D35"]
                [Opening "QGD"]
                [Variation "exchange, positional line, 5...c6"]
                [WhiteFideId "13300474"]
                [BlackFideId "3503240"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]
            """,
            False
        ],
        [
            "Invalid (inside of game)",
            """
                1. c4 e6 2. Nc3 d5 3. d4 Nf6 4. cxd5 exd5 5. Bg5 c6 6. e3 Bf5 7. Qf3 Bg6 8. Bxf6
                Qxf6 9. Qxf6 gxf6 10. Nf3 Nd7 11. Nh4 Be7 12. Ne2 f5 13. Nf3 Bb4+ 14. Kd1 Bd6
                15. Ne1 Ke7 16. Nd3 Bh5 17. f3 Bg6 18. Nef4 a5 19. Ke1 Nf8 20. g3 Ne6 21. Rc1
                Rhe8 22. Kf2 Kf6 23. Be2 Re7 24. Bd1 Kg7 25. Re1 Ree8 26. Re2 Re7 27. Rc3 Kf8
                28. a3 Bxf4 29. Nxf4 Nxf4 30. exf4 f6 31. Rb3 Rxe2+ 32. Bxe2 b5 33. Rc3 Be8 34.
                Bd3 Bd7 35. g4 Ke7 36. Bxf5 Bxf5 37. gxf5 Kd7 38. Rc1 a4 39. Rg1 Re8 40. h4 Re7
                [Event "American Cup Champ"]
                [Site "Saint Louis USA"]
                [Date "2023.03.18"]
                [Round "1.2"]
                [White "Sevian, Samuel"]
                [Black "Nakamura, Hikaru"]
                [Result "1/2-1/2"]
                [WhiteTitle "GM"]
                [BlackTitle "GM"]   
                41. h5 c5 42. dxc5 Kc6 43. h6 Kxc5 44. Rg6 Kc4 45. Rxf6 Rb7 46. Re6 Kb3 47. Re2
                Rb6 48. Ke3 Rf6 49. Rg2 Rf8 50. Kd4 Rxf5 51. Rf2 Ka2 52. Ke3 Kb3 53. Rd2 Kc4 54.
                Rd3 Kc5 55. Rc3+ Kd6 56. Rc8 Rf6 57. Rd8+ Kc5 58. Rc8+ Kd6 59. Re8 Rxh6 60. f5
                Rh4 61. Rd8+ Ke5 62. f4+ Kxf5 63. Rxd5+ Kf6 64. Rxb5 Rh2 65. Ke4 Re2+ 66. Kf3
                Rd2 67. Kg3 Re2 68. Rb7 Kf5 69. Kf3 Rh2 70. Rb5+ Kf6 71. Ke4 Re2+ 72. Kd3 Rf2
                73. Rb7 h5 74. Ke3 Rg2 75. Kf3 Rd2 76. Kg3 Re2 77. Rb6+ Kf5 78. Rb5+ Kf6 79. Kf3
                Rd2 80. Ke3 Rg2 81. Kf3 Rd2 82. Ke4 Re2+ 83. Kd3 Rf2 84. Ke3 Rg2 85. Rb6+ Kf5
                86. Kf3 Rd2 87. Rb4 Rc2 88. Kg3 Rd2 89. Rb8 Re2 90. Rf8+ Kg6 91. Rg8+ Kf6 92.
                Rb8 Kf5 93. Rb4 Rd2 94. Rxa4 Rxb2 95. Ra5+ Kf6 96. Kf3 Rb3+ 97. Ke4 h4 98. Rh5
                Rxa3 99. Rh6+ Kf7 100. Rh7+ Kf6 101. Rh6+ Kf7 102. Rh7+ Kf6 103. Rh6+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (syntax)",
            """
                [Event "American Cup Champ"]
                [Site "Saint Louis USA"]
                [Date "2023.03.18"]
                ["1.2"]
                [White "Sevian, Samuel"]
                [Black]
                [Result "1/2-1/2"]
                [WhiteTitle "GM"]
                []
                [WhiteElo "2687"]
                [BlackElo "2768"]
                [ECO "D37"]
                [Opening "QGD"]
                [Variation "4.Nf3"]
                [WhiteFideId "2040506"]
                [BlackFideId "2016192"]
                [EventDate "2023.03.17]
                [EventType "k.o."]

                1. d4 Nf6 2. c4 e6 3. Nf3 d5 4. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Bb7 13. b4 c6 14. Qb3 a5 15. Rfd1
                axb4 16. axb4 Ra7 17. Ra1 Rfa8 18. Rxa7 Rxa7 19. Ne1 Ne4 20. Nxe4 dxe4 21. f3
                Nf6 22. fxe4 Nxe4 23. Nf3 Bc8 24. Qc2 Bf5 25. Ne5 Qf6 26. Bd3 Qg5 27. Re1 Ra1
                28. Rxa1 Qxe3+ 29. Kf1 Nd2+ 30. Qxd2 Qxd2 31. Ra8+ Kh7 32. Bxf5+ g6 33. Bd3 Qc1+
                34. Ke2 Qb2+ 35. Ke3 c5 36. bxc5 bxc5 37. Rd8 cxd4+ 38. Rxd4 Qxg2 39. Rd7 Qg1+
                40. Ke4 Qe1+ 41. Kd5 Qa5+ 42. Ke4 Qe1+ 43. Kd5 Qa5+ 44. Ke4 Qe1+ 1/2-1/2
            """,
            False
        ],
    ]

    print("DESCRIPTORS")
    test_print(samples)


def test_inv_turns():
    samples = [
        [
            "Invalid (bad start index)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                2. d4 Nf6 3. c4 e6 4. Nf3 d5 5. Nc3 h6 6. Bf4 Bd6 7. Bxd6 Qxd6 8. e3 O-O 9. Rc1
                a6 10. a3 b6 11. cxd5 exd5 12. Be2 Nbd7 13. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (no start)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                d4 d4 1. d4 Nf6 2. c4 e6 3. Nf3 d5 4. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (missing turn)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. d4 Nf6 2. Nf3 d5 4. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (bad order)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. d4 Nf6 2. c4 e6 4. Nf3 d5 3. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (same turn twice)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. d4 Nf6 2. c4 e6 2. c4 c4 3. Nf3 d5 4. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (unnecessary recovery)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. d4 Nf6 2. c4 2... e6 3. Nf3 d5 4. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (recovery not matching)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. d4 Nf6 2. c4 e6 3... 3. Nf3 d5 4. Nc3 h6 5. Bf4 Bd6 6. Bxd6 Qxd6 7. e3 9... O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 8... Nbd7 12. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
        [
            "Invalid (syntax)",
            """
                [BlackFideId "2016192"]
                [EventDate "2023.03.17"]
                [EventType "k.o."]

                1. d4 Nf6 2.. c4 (commentary) 2.... e6 3. Nf3 d5 D. Nc3 h6 5. Bf4 Bd6 6.2 Bxd6 Qxd6 7. e3 O-O 8. Rc1
                a6 9. a3 b6 10. cxd5 exd5 11. Be2 Nbd7 12. O-O Qe1+ 1/2-1/2
            """,
            False
        ],
    ]

    print("TURNS")
    test_print(samples)


###############################
#             MAIN            #
###############################

if __name__ == '__main__':
    # test_valid()
    # test_inv_descriptors()
    # test_inv_turns()
    # test_inv_commentaries()
    # test_inv_castle()
    # test_inv_moves()
    test_inv_win()
