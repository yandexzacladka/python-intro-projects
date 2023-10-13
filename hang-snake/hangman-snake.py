import os
import random
import time
from pynput import keyboard

class Snake:
    def __init__(self):
        self.direction = 'up' #начальное направление движения змейки вверх
        self.koor = [[WIDTH // 2, HEIGHT // 2], [WIDTH // 2, HEIGHT // 2 + 1], [WIDTH // 2, HEIGHT // 2 + 1]] #список координат точек собой
        # змейку на игровом поле
        self.letters_on_field = [] # список букв на игровом поле
        self.game = 'play'
        self.direction_changed = False #флаг, указывающий на то, было ли изменено направление змейки
        self.mistakes = 0 #количество ошибок
        self.word = '' #  загаданное слово
        self.word_line = [] # список символов, показывающий угаданные буквы в загаданном слове
        self.upload_templates() #используется для загрузки шаблона

    def upload_templates(self): #добавление виселицы
        self.templates = [[] for _ in range(6)]
        file = open('otobr.txt').readlines()
        for i in range(6):
            for j in range(30):
                self.templates[i].append(file[30 * i + j].replace('\n', ''))
        self.hangman = self.templates[0]

    def move(self):
        new_x, new_y = self.koor[0] #координаты первой точки тела змейки (головы).
        match self.direction:
            case 'up':
                self.koor.insert(0, [new_x, new_y - 1])
            case 'left':
                self.koor.insert(0, [new_x - 1, new_y])
            case 'right':
                self.koor.insert(0, [new_x + 1, new_y])
            case 'down':
                self.koor.insert(0, [new_x, new_y + 1])
        flag = False
        for i in range(len(self.letters_on_field)): #представляет буквы на игровом поле.
            if self.letters_on_field[i][1] == self.koor[0]:
                self.eat(i)
                flag = True #змейка съела букву.
                self.letters_on_field.pop(i)
                break
        if not flag:
            self.koor.pop()


        if self.koor[0][0] < 0 or self.koor[0][1] < 0 or self.koor[0][0] >= WIDTH or \
                self.koor[0][1] >= HEIGHT or self.koor.count(self.koor[0]) == 2:
            self.game = 'defeat'




    def eat(self, index):
        if self.letters_on_field[index][0] in self.word:
            for i in range(len(self.word)):
                if self.word[i] == self.letters_on_field[index][0]:
                    self.word_line[i] = self.letters_on_field[index][0]

            if ''.join(self.word_line) == self.word:
                self.game = 'win'

        else:
            self.mistakes += 1
            self.hangman = self.templates[self.mistakes]
            if self.mistakes >= MAX_MISTAKES:
                self.game = 'defeat'


    def generate_bukv(self):
        for i in alfafit:
            self.letters_on_field.append([i, [random.randint(0, WIDTH - 2), random.randint(0, HEIGHT - 2)]])


def on_press(key):
    if not snake.direction_changed: #не было ли изменено направление движения змейки, чтобы избежать мгновенного изменения направления.
        match key:
            case keyboard.Key.left:
                if snake.direction != 'right': #Это, чтобы избежать двойного поворота змейки.
                    snake.direction = 'left' #Если условие истинно, направление движения змейки устанавливается в "влево".
            case keyboard.Key.up:
                if snake.direction != 'down':
                    snake.direction = 'up'
            case keyboard.Key.right:
                if snake.direction != 'left':
                    snake.direction = 'right'
            case keyboard.Key.down:
                if snake.direction != 'up':
                    snake.direction = 'down'
        snake.direction_changed = True #флаг указывающий, что направление движения было изменено.



def update_world():
    os.system('cls||clear')
    world = [[" " for i in range(WIDTH)] for i in range(HEIGHT)] #Здесь создается двумерный список представляет игровой мир
    for i in snake.letters_on_field:
        world[i[1][1]][i[1][0]] = i[0]
    print(' ' * WIDTH)
    print(' ' + '_' * WIDTH)
    for i in snake.koor[1:]:
        world[i[1]][i[0]] = '*'
    world[snake.koor[0][1]][snake.koor[0][0]] = '0'
    for i in range(len(world)):
        world[i].append(snake.hangman[i])
    world[2][-1] = 5 * ' ' + ' '.join(snake.word_line)
    for i in range(len(world)):
        print('|' + ''.join(world[i][:-1]) + '|' + world[i][-1])
    print(' ' + '¯' * WIDTH)


if __name__ == '__main__':
    WIDTH = 50
    HEIGHT = 30
    os.system(f"mode con cols={WIDTH + 50} lines={HEIGHT + 5}")
    fps = 5
    file = open('hand.txt', encoding='utf-8')
    WORDS = list(map(lambda x: x.strip(), file.readlines()))
    alfafit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    file.close()
    used_words = [] #использованные слова
    MAX_MISTAKES = 5
    while True:
        snake = Snake()
        listener = keyboard.Listener(on_press=on_press, suppress=False) #реагирует на нажатие клавиш
        snake.word = random.choice(WORDS)
        while snake.word in used_words:
             snake.word = random.choice(WORDS)
        used_words.append(snake.word)
        snake.word_line = ['_' for _ in range(len(snake.word))]
        snake.generate_bukv()
        listener.start()
        while snake.game == 'play':
            snake.direction_changed = False
            snake.move()
            if snake.game == 'play':
                update_world()
                time.sleep(1/fps)
        if snake.game == 'defeat':
            listener.stop()
            snake.word_line = list(snake.word)
            update_world()
            if input('GG ты проиграл. 0 - выйти, 1 - заново: ') == '1':
                snake.game = 'play'
            else:
                break
        elif snake.game == 'win':
            listener.stop()
            update_world()
            if input('Победа получается. 0 - выйти, 1 - заново:') == '1':
                snake.game = 'play'
            else:
                break
