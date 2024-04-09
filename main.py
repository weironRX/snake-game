import keyboard
import time
import os
import random

class Game:
    def __init__(self, movements, current_move, size, latency,):
        self.movements = movements
        self.current_move = current_move
        self.size = size
        self.latency = latency

    def __validate_step(self, move) -> None:

        if (self.current_move == "w" and move == "s" or
            self.current_move == "s" and move == "w" or
            self.current_move == "a" and move == "d" or
            self.current_move == "d" and move == "a"):
                return

        self.current_move = move


    def __next_step(self, head) -> list[int]:

        if (self.current_move == "w"):
            return [head[0] - 1, head[1]]
        if (self.current_move == "s"):
            return [head[0] + 1, head[1]]
        if (self.current_move == "a"):
            return [head[0], head[1] - 1]
        if (self.current_move == "d"):
            return [head[0], head[1] + 1]



    def start(self):

        print(
            "░██████╗███╗░░██╗░█████╗░██╗░░██╗███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗",
            "██╔════╝████╗░██║██╔══██╗██║░██╔╝██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝",
            "╚█████╗░██╔██╗██║███████║█████═╝░█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░",
            "░╚═══██╗██║╚████║██╔══██║██╔═██╗░██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░",
            "██████╔╝██║░╚███║██║░░██║██║░╚██╗███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗",
            "╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝", sep="\n")

        print("\n")

        time.sleep(1)

        print(
            "█▄▄ █▄█   █▀█ █▀▀ ▀█▀ █▀█ █▀█ █░█   █▀▄ █▀▄▀█ █ ▀█▀ █▀█ █▄█",
            "█▄█ ░█░   █▀▀ ██▄ ░█░ █▀▄ █▄█ ▀▄▀   █▄▀ █░▀░█ █ ░█░ █▀▄ ░█░",
        sep = "\n")

        time.sleep(1)


        board = Board(self.size)
        snake = Snake([[self.size // 2, self.size // 2]])

        food = Food(self.size)

        score = 0


        for move in self.movements:
            keyboard.add_hotkey(move, self.__validate_step, args=(move))

        while True:
            time.sleep(self.latency)

            snake_cords = snake.get_snake()

            next_step = self.__next_step(snake_cords[0])
            food_cords = food.get_cords()

            if (next_step[0] == food_cords[0] and next_step[1] == food_cords[1]):
                snake.addition_update([food_cords[0], food_cords[1]])
                food.update(snake.get_snake())
                score += 1
            else:
                snake.simple_update(next_step)


            snake_cords = snake.get_snake()
            board.update(snake_cords, food_cords)

            board.output(score=score)



class Board:
    def __init__(self, size) -> None:
        self.size = size
        body = []

        for i in range(self.size):
            body.append([0] * self.size)

        self.body = body

    def update(self, snake_body, food_cords) -> None:
        self.clear()

        for cords in snake_body:
            self.body[cords[0]][cords[1]] = 1

        self.body[food_cords[0]][food_cords[1]] = 9

    def output(self, score):
        os.system("cls")

        print("score:", score)
        for row in self.body:
            print(*row)

    def clear(self) -> None:
        self.body.clear()

        body = []

        for i in range(self.size):
            body.append([0] * self.size)

        self.body = body


    def get_size(self) -> None:
        return self.size


class Snake:

    def __init__(self, body) -> None:
        self.body = body

    def simple_update(self, head) -> None:
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]

        self.body[0] = head

    def addition_update(self, head) -> None:
        self.body.insert(0, head)

    def get_snake(self):
        return self.body

class Food:

    def __init__(self, size) -> None:
        self.size = size
        self.x = self.__generate_number()
        self.y = self.__generate_number()

    def update(self, snake_body) -> None:
        self.x = self.__generate_number()
        self.y = self.__generate_number()

        while ([self.x, self.y] in snake_body):
            self.x = self.__generate_number()
            self.y = self.__generate_number()


    def get_cords(self) -> list[int]:
        return [self.x, self.y]

    def __generate_number(self):
        return random.randint(0, self.size - 1)


Snake_Game = Game(["w", "a", "s", "d"], "w", 9, 0.5)

Snake_Game.start()