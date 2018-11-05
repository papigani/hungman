# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:10:05 2018
@author: matsu
"""

def hangman(word):
    wrong=0
    stages=["",
            "________        ",
            "|               ",
            "|        |       ",
            "|        O       ",
            "|       /|\      ",
            "|       / \      ",
            "|                "
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    
    while wrong < len(stages)-1:
        print("\n")
        msg="1文字予想してね："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        
        print(" ".join(board))
        endnum= wrong+1
        print("\n".join(stages[0:endnum]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は　{}".format(word))

hangman("cat")
