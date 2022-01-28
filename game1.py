game=(" 1 2 3\n 4 5 6\n 7 8 9")
print(game)

for i in range(9):
    game1=game.replace(input(str("введите номер поля ")),
                       input(str("введите Х или О ")))
    game=game1
    print(game)
    if game[1]==game[3]==game[5]=="X" or game[1]==game[10]==game[19]=="X" or game[1]==game[8]==game[15]=="X" or game[3]==game[10]==game[17]=="X" or game[5]==game[10]==game[15]=="X" or game[5]==game[12]==game[19]=="X" or game[8]==game[10]==game[12]=="X" or game[15]==game[17]==game[19]=="X" :
       print("Победил первый игрок")
       break
    elif  game[1]==game[3]==game[5]=="O" or game[1]==game[10]==game[19]=="O" or game[1]==game[8]==game[15]=="O" or game[3]==game[10]==game[17]=="O" or game[5]==game[10]==game[15]=="O" or game[5]==game[12]==game[19]=="O" or game[8]==game[10]==game[12]=="O" or game[15]==game[17]==game[19]=="O" :
       print("Победил второй игрок")
       break
    else:
       print("следующий ход")
print("Конец")
   