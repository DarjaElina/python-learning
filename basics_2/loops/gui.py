import random
import time
import os
from colorama import Fore, Style, init
init(autoreset=True)

picture = [
    [0,0,0,0,4,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,1,2,1,0,0,0],
    [0,0,1,1,1,1,1,0,0],
    [0,1,1,2,1,2,1,1,0],
    [1,1,1,1,3,1,1,1,1],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,5,0,0,0,0,0,5,0],
]

def draw_tree(picture):
    for row in picture:
        print("".join(row))

symbols = {
    0: "  ",
    1: Fore.GREEN + "▲ ",
    2: Fore.RED + "● ",
    3: Fore.YELLOW + "✦ ",
    4: Fore.YELLOW + "★ ",
    5: Fore.MAGENTA + "■ "
}

while True:
    os.system("cls" if os.name == "nt" else "clear")

    snowy_picture = []
    for row in picture:
        new_row = []
        for cell in row:
            if cell == 0 and random.random() < 0.08:
                new_row.append("❄️ ")
            else:
                new_row.append(symbols.get(cell, cell))
        snowy_picture.append(new_row)

    draw_tree(snowy_picture)

    time.sleep(0.4)