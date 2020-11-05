from math_engine import get_result
import pyglet
from pyglet import gl
from random import randrange, choice
from pyglet.window import key
from game_objects import Text_to_print, Bucket, Rectangle
import json
import os

width = 900
height = 650
window = pyglet.window.Window(width=width,
                              height=height,
                              caption="Math Game")
x, y = window.get_location()
window.set_location(x + 20, y + 20)

font_example = 17
speed = 100
headline_y = height - 2 * font_example
objects = []
right_examples = []
answer = []
right_answers = []
results = []
numbers = []
operation = []
operations = [" + ", " - ", " x ", " : "]
headlines = []
buckets = []
rectangles = []
score = [0]
colors = [(255, 255, 255, 250), (255, 255, 0, 255), (192, 192, 192, 255),
          (218, 165, 32, 255), (255, 0, 0, 255), (154, 205, 50, 255),
          (0, 255, 255, 250), (173, 255, 47, 255), (0, 255, 0, 255)]

distance_of_buckets = 10
space_of_lines = 3

answer_correct = False
counter = 0

min_x = []
max_x = []
starter_position = [0, 0]
starter_speed = speed

possible_y_objects = []
possible_x_objects = []
used_x_objects = []
game_over = False
end_texts = []
main = True
main_texts = []
name = []
name_user = []
main_questions = []
possibilities = []
difficulty = []

right_sound = pyglet.media.load("beep.wav", streaming=False)
wrong_sound = pyglet.media.load("oops.wav", streaming=False)


def main_screen():
    """
    Generates texts for the main screen and adds them to the list
    """
    headline = Text_to_print(2 * font_example,
                             [width / 2, headline_y - 3 * font_example],
                             0, "M A T H  G A M E", colors[3])
    instruction = Text_to_print(font_example,
                                [width / 2, 2 * font_example],
                                0, "Press SPACE BAR to Play", colors[0])
    main_texts.extend([headline, instruction])
    generate_questions()
    generate_possibilities()


def generate_questions():
    """
    Generates questions for the main screen and adds them to the list
    """
    instruction1 = Text_to_print(font_example,
                                 [300, 2 * height / 3],
                                 0, "Your name:", colors[0])
    instruction2 = Text_to_print(font_example,
                                 [300, 2 * height / 3 - 2 * font_example],
                                 0, "Choose difficulty:", colors[0])
    choice = Text_to_print(font_example,
                           [300, 2 * height / 3 - 8 * font_example],
                           0, "Your choice:", colors[0])
    main_questions.extend([instruction1, instruction2, choice])


def generate_possibilities():
    """
    Generates possibilities for main screen and adds them to the list
    """
    instruction3 = Text_to_print(font_example,
                                 [350, 2 * height / 3 - 2 * font_example],
                                 0, "addition, substraction   1", colors[0])
    instruction4 = Text_to_print(font_example,
                                 [350, 2 * height / 3 - 4 * font_example],
                                 0, "multiply, division           2", colors[0])
    instruction5 = Text_to_print(font_example,
                                 [350, 2 * height / 3 - 6 * font_example],
                                 0, "mix                              3", colors[0])
    possibilities.extend([instruction3, instruction4, instruction5])


def user_name():
    """
    Creates an object from the name entered by the user and adds it to the list
    """
    name_input = Text_to_print(font_example,
                               [350, 2 * height / 3],
                               0, "".join(name), colors[0])
    name_user.append(name_input)


def generate_headlines():
    """
    Generates headlines for game and adds them to the list
    """
    x = (buckets[3].coordx[0] - buckets[1].coordx[0]) / 2 + buckets[1].coordx[0]
    headline1 = Text_to_print(font_example, [x, headline_y], 0, "ANSWER", colors[0])
    headline2 = Text_to_print(font_example, [width - x, headline_y], 0, "SCORE", colors[0])
    headline3 = Text_to_print(font_example,
                              [width / 2, headline_y - 3 * font_example],
                              0, "M A T H  G A M E", colors[3])
    headlines.extend([headline1, headline2, headline3])


def generate_buckets():
    """Generates 5 buckets"""
    x1 = distance_of_buckets
    x3 = (width - distance_of_buckets) / 5
    side = x3 - x1
    y1 = (font_example + 2) * 3 + 2 * space_of_lines + 3
    y2 = space_of_lines

    k1 = x1 + space_of_lines
    l2 = y2 + space_of_lines
    k3 = x3 - space_of_lines

    bucket1 = Bucket([x1, x1, x3, x3], [y1, y2, y2, y1], colors[0], 1.5)
    buckets.append(bucket1)
    possible_x_objects.append(k1 + 1.6 * distance_of_buckets)

    bucket1_1 = Bucket([k1, k1, k3, k3], [y1, l2, l2, y1], colors[0], 1.5)
    buckets.append(bucket1_1)

    for i in range(4):
        x1 += distance_of_buckets + side
        k1 = x1 + space_of_lines
        x3 += distance_of_buckets + side
        k3 = x3 - space_of_lines
        bucket = Bucket([x1, x1, x3, x3], [y1, y2, y2, y1], colors[0], 1.5)
        buckets.append(bucket)
        bucket0_1 = Bucket([k1, k1, k3, k3], [y1, l2, l2, y1], colors[0], 1.5)
        buckets.append(bucket0_1)
        possible_x_objects.append(k1 + 1.6 * distance_of_buckets)

    for j in range(3):
        possible_y_objects.append(l2 + space_of_lines)
        l2 += font_example


def generate_rectangle_answer():
    """Generates rectangle - space for answer"""
    x1 = buckets[1].coordx[0]   # x2
    x3 = buckets[3].coordx[0]   # x4
    y2 = headline_y - font_example  # y3
    y1 = y2 - 3 * font_example    # y4
    rect_answer = Rectangle([x1, x1, x3, x3], [y1, y2, y2, y1], colors[0], 1.5)
    rectangles.append(rect_answer)


def generate_rectangle_score():
    """Generates rectangle - space for score"""
    x1 = buckets[-4].coordx[2]
    x3 = buckets[-2].coordx[2]
    y2 = headline_y - font_example  # y3
    y1 = y2 - 3 * font_example    # y4
    rect_score = Rectangle([x1, x1, x3, x3], [y1, y2, y2, y1], colors[0], 1.5)
    rectangles.append(rect_score)


def generate_div_line():
    """Generates dividing line"""
    indentation = 3
    x1 = indentation
    x3 = width - indentation
    y2 = rectangles[0].coordy[0] - font_example
    y1 = y2 - font_example
    div_line1 = Bucket([x1, x1, x3, x3], [y1, y2, y2, y1], colors[1], 1.5)
    k1 = x1 + space_of_lines
    k3 = x3 - space_of_lines
    l2 = y2 - space_of_lines
    div_line2 = Bucket([k1, k1, k3, k3], [y1, l2, l2, y1], colors[1], 1.5)
    buckets.extend([div_line1, div_line2])


def starter_coord():
    """Generates initial coordinates for starter"""
    distance = (width - distance_of_buckets) / 5 - 2 * distance_of_buckets
    starter_position[0] = distance / 2 + 2.5 * distance_of_buckets
    starter_position[1] = buckets[11].coordy[0]
    min_x.append(starter_position[0])
    max_x.append(width - starter_position[0])


def update_starter():
    """
    Creates objects acoording to current coordinates and adds them to the list
    """
    # buckets 12-15
    distance = (width - distance_of_buckets) / 5 - 2 * distance_of_buckets
    x3 = starter_position[0] - distance / 2  # x4
    x1 = x3 - distance_of_buckets  # x2
    y2 = starter_position[1]  # y3
    y1 = y2 + font_example - space_of_lines
    y4 = y2 - font_example - space_of_lines
    starter1 = Bucket([x1, x1, x3, x3], [y1, y2, y2, y4], colors[1], 1.5)
    x1 -= space_of_lines
    x3 -= space_of_lines
    y2 -= space_of_lines
    starter1_1 = Bucket([x1, x1, x3, x3], [y1, y2, y2, y4], colors[1], 1.5)
    x3 = starter_position[0] + distance / 2
    x1 = x3 + distance_of_buckets
    y2 = starter_position[1]
    y1 = y2 + font_example - space_of_lines
    y4 = y2 - font_example - space_of_lines
    starter2 = Bucket([x1, x1, x3, x3], [y1, y2, y2, y4], colors[1], 1.5)
    x1 += space_of_lines
    x3 += space_of_lines
    y2 -= space_of_lines
    starter2_2 = Bucket([x1, x1, x3, x3], [y1, y2, y2, y4], colors[1], 1.5)
    buckets.extend([starter1, starter1_1, starter2, starter2_2])


def find_y_coord(number):
    """
    Finds y coordinate for object with example. There can be a maximum of 3
    objects on one x coordinate
    """
    if number < 3:
        objects[-1].coord[1] = possible_y_objects[number]


def check_answer(number1, number2, answer, operation):
    """Checks if the answer is right"""
    result = get_result(number1, number2, operation)
    for_check = string_to_int(answer)
    if for_check == result:
        return True
    else:
        return False


def string_to_int(answer):
    """
    Input is a list answer. Function returns it as a string or None if the
    list is empty
    """
    string = ""
    for i in range(len(answer) - 1):
        string += str(answer[i])
    try:
        return int(string)
    except ValueError:
        return None


def number_generator():
    """Adds two random numbers to the list"""
    number1 = randrange(0, 11)
    number2 = randrange(0, 11)
    numbers.extend([number1, number2])


def choose_operation(level):
    """Function chooses math operation acoording to the difficulty and adds
    it to the list"""
    if level == 1:
        operation.append(choice(operations[:2]))
    elif level == 2:
        operation.append(choice(operations[2:]))
    else:
        operation.append(choice(operations))


def take_closest(num, collection):
    """
    From possible x coordinates returns the number which is closest to the x
    coordinate of the starter
    """
    return min(collection, key=lambda x: abs(x - num))


def generate_object():
    """Generates new object with example and adds it to the list"""
    x = take_closest(starter_position[0], possible_x_objects)
    y = buckets[-1].coordy[3] - font_example
    number_generator()
    choose_operation(difficulty[-1])   # dodat difficulty[-1]
    color = choice(colors[1:])
    if numbers[0] == 0 and operation[-1] == " : ":
        # aby nedošlo k dělení nulou
        if difficulty[-1] == 2:
            operation.append(operations[2])
        else:
            choose_operation(1)
    if operation[-1] == " : ":
        result = numbers[0] * numbers[1]
        example = str(result) + operation[-1] + str(numbers[0]) + " = "
    else:
        example = str(numbers[0]) + operation[-1] + str(numbers[1]) + " = "
    text = Text_to_print(font_example, [x, y], speed, example, color)
    objects.append(text)


def update_score():
    """Function for drawing the current score state"""
    x = (buckets[3].coordx[0] - buckets[1].coordx[0]) / 2 + buckets[1].coordx[0]
    y = headline_y - 3 * font_example
    if right_examples:
        color = right_examples[-1].color
    else:
        color = colors[0]
    points = Text_to_print(font_example, [width - x, y], 0, str(score[0]), color)
    points.draw_text("center")


def update_answer():
    """Functions for drawing the right answer"""
    x = (buckets[3].coordx[0] - buckets[1].coordx[0]) / 2 + buckets[1].coordx[0]
    y = headline_y - 3 * font_example
    if right_examples:
        color = right_examples[-1].color
    else:
        color = colors[0]
    answer_text = Text_to_print(font_example, [x, y], 0, str(results[-1]), color)
    answer_text.draw_text("center")


def screen_game_over():
    """
    Generates text objects for game over screen, adds them to the list and
    calls the json file processing function
    """
    math_game = "M A T H  G A M E"
    headline = Text_to_print(
                2 * font_example,
                [width / 2, 2 * height / 3],
                0, math_game, colors[3])
    text = "YOUR SCORE WAS " + str(score[0])
    text_end = Text_to_print(
                font_example, [width / 2, height / 2], 0, text, colors[0])
    text1 = "Do you want to play again  (Y/N)?"
    decision = Text_to_print(
                font_example,
                [width / 2, 50],
                0, text1, colors[0])
    end_texts.extend([text_end, decision, headline])
    json_processing()


def json_processing():
    """
    Json file processing function
    Calls a function that determines if a json file is already created.
    If no - new json file is created and results are saved.
    If json file is already created - file is loaded and max score is checked
    """
    if is_json_here("data_in_json.txt"):
        with open("data_in_json.txt", encoding="utf-8") as fileToRead:
            json_data = json.load(fileToRead)
            check_max_score(json_data)
        with open("data_in_json.txt", "w", encoding="utf-8") as file_name:
            json.dump(json_data, file_name, ensure_ascii=False, indent=2)

    else:
        data = {
            "".join(name): str(score[0])
        }
        with open("data_in_json.txt", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        if score[0] > 500:
            evaluation_good = Text_to_print(
                              font_example,
                              [width / 2, height / 2 - 2 * font_example],
                              0, "Good job", colors[0])
            end_texts.append(evaluation_good)
        else:
            evaluation_bad = Text_to_print(
                             font_example,
                             [width / 2, height / 2 - 2 * font_example],
                             0, "I think you can do better", colors[0])
            end_texts.append(evaluation_bad)


def is_json_here(file_name):
    """Checks whether a json file is created"""
    return os.path.exists(file_name)


def is_same_key(data):
    """Returns whether the player has already played this game"""
    for keys in data:
        if keys == "".join(name):
            return True
    return False


def check_max_score(data):
    """
    Checks and evaluates score. Creates objects with results and adds them to
    the list
    """
    if is_same_key(data):
        if better_than_before(data):
            for keys in data:
                data[keys] = int(data[keys])
            max_key = max(data, key=data.get)
            if "".join(name) == max_key:
                congrats1 = Text_to_print(
                            font_example,
                            [width / 2, height / 2 - 4 * font_example],
                            0, "Wow! Now you have the best score of all!",
                            colors[4])
                end_texts.append(congrats1)
            else:
                almost = Text_to_print(
                            font_example,
                            [width / 2, height / 2 - 4 * font_example],
                            0, "Great job! But... " + max_key +
                            "is still better with score " +
                            str(data[max_key]), colors[0])
                end_texts.append(almost)

    else:
        data["".join(name)] = str(score[0])
        for keys in data:
            data[keys] = int(data[keys])
        max_key = max(data, key=data.get)
        if "".join(name) == max_key:
            congrats1 = Text_to_print(
                        font_example,
                        [width / 2, height / 2 - 4 * font_example],
                        0, "Wow! Now you have the best score of all!",
                        colors[4])
            end_texts.append(congrats1)
        else:
            not_great = Text_to_print(
                        font_example,
                        [width / 2, height / 2 - 4 * font_example],
                        0, max_key + "is still better with score " +
                        str(data[max_key]), colors[0])
            end_texts.append(not_great)


def better_than_before(data):
    """
    Evaluates whether the player has a better result than before. If user is
    better than before new result will be saved. Creates object with result
    and adds it to the list
    """
    for keys in data:
        data[keys] = int(data[keys])
    if data["".join(name)] < score[0]:
        congrats = Text_to_print(
                   font_example,
                   [width / 2, height / 2 - 2 * font_example],
                   0, "Super! You did better than before!", colors[0])
        end_texts.append(congrats)
        data["".join(name)] = str(score[0])
        return True
    else:
        loser = Text_to_print(
                font_example,
                [width / 2, height / 2 - 2 * font_example],
                0, "Oh no! You were worse than before!", colors[0])
        end_texts.append(loser)
        return False


def new_game():
    """Function for preparing a new game"""
    global speed

    reset()
    objects.clear()
    end_texts.clear()
    used_x_objects.clear()
    speed = 100
    score[0] = 0
    results.clear()
    generate_object()


def reset():
    """Clears lists for answer, numbers, right answers and operation"""
    answer.clear()
    numbers.clear()
    right_answers.clear()
    operation.clear()


def start_game():
    """Calls functions to start the game"""
    generate_buckets()
    generate_rectangle_answer()
    generate_rectangle_score()
    generate_headlines()
    generate_div_line()
    starter_coord()
    update_starter()
    generate_object()


@window.event
def on_draw():
    """
    Window push handler
    Function for drawing all objects. They are divided according to in which
    part of the game they should be drawn
    """

    if main:
        window.clear()
        for text in main_texts:
            text.draw_text("center")
        for question in main_questions:
            question.draw_text("right")
        for possibility in possibilities:
            possibility.draw_text("left")
        if name:
            user_name()
            name_user[-1].draw_text("left")
        if difficulty:
            chosen = Text_to_print(font_example,
                                   [350, 2 * height / 3 - 8 * font_example],
                                   0, str(difficulty[-1]), colors[0])
            chosen.draw_text("left")
        if not main:
            window.clear()

    elif game_over:
        window.clear()
        for text in end_texts:
            text.draw_text("center")

    else:
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        for i in range(len(objects)):
            objects[i].draw_text("left")

        del buckets[12:16]
        update_starter()
        for j in range(len(headlines)):
            headlines[j].draw_text("center")

        for k in range(len(buckets)):
            buckets[k].draw_bucket()

        for l in range(len(rectangles)):
            rectangles[l].draw_rectangle()

        update_score()

        if results:
            update_answer()


@window.event
def on_text(text):
    """
    Function for detecting typed characters. Adds them to the list name.
    Calls function on_draw for rendering
    """
    if main and "\n" not in name:
        name.append(text)
        on_draw()


@window.event
def on_key_press(symbol, modifiers):
    """
    Main screen - if user presses key backspace - the last character in name
    is deleted. If there is only one character - the list is cleared. After
    pressing enter user can choose difficulty. If difficulty is chosen game
    can be started by pressing space bar.
    Game running - if enter is not in the list, key is added to the list. User
    can add numbers from num_pad, minus and enter
    Game over - Y for new game or N for exit
    """
    global game_over
    global main

    if main:
        if "\n" not in name:
            if symbol == key.BACKSPACE:
                if len(name) > 1:
                    del name[-1]
                else:
                    name.clear()

        if symbol == key.ENTER:
            name.append("\n")

        if "\n" in name:
            if symbol == key.NUM_1:
                difficulty.append(1)
            if symbol == key.NUM_2:
                difficulty.append(2)
            if symbol == key.NUM_3:
                difficulty.append(3)

        if difficulty:
            if symbol == key.SPACE:
                main = False
                start_game()

    if game_over:
        if symbol == key.Y:
            new_game()
            game_over = False
        if symbol == key.N:
            window.close()

    if not main and "ENTER" not in answer and not game_over:
        if symbol == key.NUM_0:
            answer.append(0)
        if symbol == key.NUM_1:
            answer.append(1)
        if symbol == key.NUM_2:
            answer.append(2)
        if symbol == key.NUM_3:
            answer.append(3)
        if symbol == key.NUM_4:
            answer.append(4)
        if symbol == key.NUM_5:
            answer.append(5)
        if symbol == key.NUM_6:
            answer.append(6)
        if symbol == key.NUM_7:
            answer.append(7)
        if symbol == key.NUM_8:
            answer.append(8)
        if symbol == key.NUM_9:
            answer.append(9)
        if symbol == key.NUM_SUBTRACT:
            answer.append("-")
        if symbol == key.ENTER or symbol == key.RETURN:
            answer.append("ENTER")


def update(dt):
    """
    Function for game update
    Starter moves to the left and to the right. It has set the max x coord
    User answer correct - the counter is substracted to keep the result
    displayed for a while
    No answer - the example falls down acoording to possible y coord
    Enter in answer - evaluates if answer is correct. If yes - score  and speed
    are increased, if no - score and speed are decreased. Sound is played.
    Function checks whether the game is not over
    After evaluation generates new object

    """
    global answer_correct
    global counter
    global game_over
    global speed
    global starter_speed
    global main

    if not main:
        starter_position[0] += starter_speed * dt
        if starter_position[0] > max_x[0]:
            starter_position[0] = max_x[0]
            starter_speed = - abs(speed)
        if starter_position[0] < min_x[0]:
            starter_position[0] = min_x[0]
            starter_speed = abs(speed)

        if answer_correct is True:
            counter -= 1
            if(counter == 0):
                answer_correct = False
                reset()
                del objects[-1]
                generate_object()

        else:
            objects[-1].coord[-1] -= objects[-1].speed * dt
            if objects[-1].coord[1] < possible_y_objects[-1] + font_example:
                find_y_coord(used_x_objects.count(objects[-1].coord[0]))
                if used_x_objects.count(objects[-1].coord[0]) == 3:
                    game_over = True
                    screen_game_over()
                used_x_objects.append(objects[-1].coord[0])
                objects[-1].speed = 0

            if "ENTER" in answer:
                if check_answer(numbers[0], numbers[1], answer, operation):
                    results.append(get_result(numbers[0], numbers[1], operation))
                    right_examples.append(objects[-1])
                    objects[-1].speed = 0
                    if answer_correct is False:
                        counter = 50
                    answer_correct = True
                    right_sound.play()
                    int_answer = string_to_int(answer)
                    objects[-1].text = "-* " + str(int_answer) + " *-"
                    if operation[-1] in operations[:2]:
                        score[0] += 5
                    else:
                        score[0] += 10
                    if speed < 200:
                        speed += 2
                else:
                    find_y_coord(used_x_objects.count(objects[-1].coord[0]))
                    objects[-1].speed = 0
                    if used_x_objects.count(objects[-1].coord[0]) == 3:
                        game_over = True
                        screen_game_over()
                    used_x_objects.append(objects[-1].coord[0])
                    wrong_sound.play()
                    if score[0] > 0:
                        score[0] -= 1
                    speed -= 1
                answer.clear()

        # pokud poslední objekt ze seznamu dopadl, vytvoř nový
        if objects[-1].coord[1] in possible_y_objects and objects[-1].speed == 0:
            result = get_result(numbers[0], numbers[1], operation)
            objects[-1].text = objects[-1].text + str(result)
            results.append(objects[-1].text)
            reset()
            generate_object()


def tick(dt):
    """
    Calls function update after the start of the game
    """
    if not main:
        update(dt)


main_screen()

pyglet.clock.schedule(tick)

pyglet.app.run()
