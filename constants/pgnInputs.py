
# Valid input
inputOne = '[Event "Mannheim"] ' \
           '[Site "Mannheim GER"]' \
           '[Date "1914.08.01"]' \
           '[EventDate "1914.07.20"]' \
           '[Round "11"]' \
           '[Result "1-0"]' \
           '[White "Alexander Alekhine"]' \
           '[Black "Hans Fahrni"]' \
           '[ECO "C13"]' \
           '[WhiteElo "?"]' \
           '[BlackElo "?"]' \
           '[PlyCount "45"]' \
           '1. e4 {Notes by Richard Reti} 1... e6 2. d4 d5 3. Nc3 Nf6 4. Bg5 Be7 5. e5 Nfd7 ' \
           '6. h4 {This ingenious method of play which has subsequently been adopted by all' \
           'modern masters is characteristic of Alekhine s style.} 6... Bxg5 7. hxg5 Qxg5 ' \
           '8. Nh3 {! The short-stepping knight is always brought as near as possible to' \
           'the actual battle field. Therefore White does not make the plausible move 8 Nf3' \
           'but 8 Nh3 so as to get the knight to f4.} 8... Qe7 9. Nf4 Nf8 10. Qg4 f5 {The' \
           'only move. Not only was 11 Qxg7 threatened but also Nxd5.} 11. exf6 gxf6 12. ' \
           'O-O-O {He again threatens Nxd5.} 12... c6 13. Re1 Kd8 14. Rh6 e5 15. Qh4 Nbd7 ' \
           '16. Bd3 e4 17. Qg3 Qf7 {Forced - the sacrifice of the knight at d5 was' \
           'threatened and after 17...Qd6 18 Bxe4 dxe4 19 Rxe4 and 20 Qg7 wins.} 18. Bxe4 ' \
           'dxe4 19. Nxe4 Rg8 20. Qa3 {Here, as so often happens, a surprising move and one' \
           'difficult to have foreseen, forms the kernel of an apparently simple Alekhine' \
           'combination.} 20... Qg7 {After 20.Qe7 21.Qa5+ b6 22.Qc3 would follow.} 21. ' \
           'Nd6 Nb6 22. Ne8 Qf7 {White mates in three moves.} 23. Qd6+ Qd6 1-0'

# Invalid input
inputTwo = '1. e4 e4 3. e5 e5 4. e4 0-1'

# Invalid input
inputThree = '1. e4 e5 { Nf3 1-0'

# Valid input
inputFour = """[Event "London 'Immortal game'"]
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
1. e4 { Text1 (f4 [ f5 ] ) text3 f6 [ f7 ] test5  } 1... e5 2. f4 exf4 3. Bc4 Qh4+ 4. Kf1 b5 5. Bxb5 Nf6 6. Nf3 Qh6 7. d3 Nh5 8.
Nh4 Qg5 9. Nf5 c6 10. g4 Nf6 11. Rg1 cxb5 12. h4 Qg6 13. h5 Qg5 14. Qf3 Ng8 15.
Bxf4 Qf6 16. Nc3 Bc5 17. Nd5 Qxb2 18. Bd6 Bxg1 19. e5 Qxa1+ 20. Ke2 Na6 21.
Nxg7+ Kd8 22. Qf6+ Nxf6 23. Be7++ 1-0"""


# Valid input
inputFive = '[a "b"]' \
            '1. e4 d5 {Scandinavian defence (often follows 2. exd5 Da5 {not often 2... c6})}' \
            '1/2-1/2'
inputSix = '[test "crazy"]' \
           '[Nzscf5qWgtgNVX "56BnnQIeAhy"]' \
           '[gvk7dXkliRpR "2LAkQJGhz81"]' \
           '[NFS5lBHW4MmNmJsP "e4ZhVulzl"]' \
           '[yZ1PSI4r78KP "XwWzscEtUqkAunNt7Hq5"]' \
           '[GArzOdNanITcsbFO9ES "WUodxeqxI"]' \
           '1. 1d7 d7 2. Rf8 gg7 1-0' \
           '[2ujZrN6LTmOBGss5jzqw "pnAGk"]' \
           '[kRM "lihgftp5kLaiAvuNSub2"]' \
           '[vUPhgAiKx "a9C7isOkq0vyep7svNE"]' \
           '[Lbfh "j6htrD1wKNFryNGHdUcG"]' \
           '1. Pxe7 Pad3 2. Be6 b6 3. Bb2 h3 4. Qc1 Kh3 5. Pb1 Pb2 6. Ra1 ' \
           'a7! 7. Nce4 Qxa3 8. Kd4 Qh1 9. Kd8 fh6 10. Nc1 Pg1 11. Nh2 Bf4 ' \
           '12. ca6 Kd8 13. Nb4 d5 14. e1 Ra5 15. f8 K5xd3 16. b6 (Ka4 h ' \
           '5a2) 16... g7 17. e5 Bg2 18. f3 Re2 19. Qc6 Kb4 20. Rg4 Rg3 21. ' \
           'g3 N2c7 22. Pb7 Rh7 23. Qd3 {bf8 B b3 K Nxf5 wuFzW c1 Pbd2 T c8 ' \
           'ka Pg3 K Ke6+ n Kg5 Pb7 f8 e2 O 1c5 Rxe4 Pxc5} 23... e6 24. d5 ' \
           'Nh7 25. Qxc6 Bxc3 26. Bf5 Qfa3 27. f4 Ka7 28. Nxb6 d6 29. Bg1 ' \
           'Qf2 30. Pb3 d6 31. Ba3 e7 32. Bab4 Kda1 33. Ph1 e2 34. cf4 Nxd7 ' \
           '35. Nc7 (gr Pfg2 iONp utl Pcd2 t (Pd3 Rc2 Bxd6 Kxg8 Kxh2 h6 Bxc8 ' \
           'zAx g2 qX Nh2 N c3 n Bxb5 D Nd1 h8 a1 c7 PVAO Rg7 g5 Kb6 oGq) rt ' \
           'Pf8 Qp) 35... e2 36. Ra6 Bhb8 37. Q5a4 c5 38. Qg7 g1 39. g6 Pg7 ' \
           '40. Kd6 d1 41. h7+ Kcc5 42. Qd8 ce1 43. Qxh3 Pa6 44. Bxe2 e4 45. ' \
           'Bh7 d2+ 1/2-1/2' \
           '[BYsR4sFynE2Rn2 "lNykA4WPhvh2kKPTjfaD"]' \
           '[loCuhQ "WDOTwZIISKjDikn6"]' \
           '1. Pb7 ec6 2. f4 Nxf7 3. Kxe5 d7 4. Kc7 Rd6 5. e7 Qc7 6. h1 {s' \
           'Rxb7 iI d5 Nh7} 6... e4+ 7. 7d6 Nf7a3 8. Pa7 e2 9. h8 h4 10. g8 ' \
           'Kxf6 11. 2b3 Bxg3 12. Q5h1 Pb6 13. fd4 e5 14. 5c6 f3 15. cb6 {l' \
           'Pb6} 15... Pb1 16. Nb3 h7 17. b2 Nb7 18. Ra1 N8h6 19. f2 c8 20. ' \
           'P5g1 e1 21. Pg3 c3 22. f5 Kh1 23. Pd7 Nf3 24. Nd1 Rd1 25. Kd5 ' \
           'Ng8 26. e3 Nxg6 27. Rh8 fc3 28. Kxf1 Ncc4 29. c1+ e3 30. cc6 (a ' \
           'Kdxa3 e7 JQ Qe2 VLzeFq c7 FU f4 N Qxb7 Nd8++ Tf Nd2 yN ba2 me ' \
           '1b6 hu Kd7 R Pxe6 Nxg7 DaR Ba8 Kxd5 Nd7 ttxI fe7 GK a2 m f6 Skp) ' \
           '30... h8 31. Qh1 a1 32. fb7 b7 0-1' \

# Valid input
