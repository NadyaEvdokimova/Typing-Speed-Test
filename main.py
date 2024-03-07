from tkinter import *
from time import perf_counter
import random

window = Tk()
window.title("Typing speed test")
window.minsize(width=500, height=500)
game_try = 0
new_window = None


# Create new window after pushing the button "try again"
def create_window():
    global new_window, name_label, info_label, go_button
    if not new_window:
        window.destroy()
    else:
        new_window.destroy()
    new_window = Tk()
    new_window.title("Typing speed test")
    new_window.minsize(width=500, height=500)
    name_label = Label(text='Typing speed test', font=("Goudy Stout", 20, "normal"))
    name_label.pack()
    info_label = Label(text="Push start and print the words below...", font=("Tahoma", 14, "normal"))
    info_label.pack()
    go_button = Button(text="Start", command=game, font=("Goudy Stout", 14, "normal"), state='normal')
    go_button.pack()


# Game function
def game():
    # Check result if button clicked
    def result_check():
        result = user_input.get("1.0", END).strip().split(" ")
        words_number = 0
        end = perf_counter()
        time = round((end - start), 2)
        for position in range(len(result)):
            if result[position] == word_for_type[position]:
                words_number += 1
        speed_label = Label(text=f'Your speed is {time}s per {words_number} correct words',
                            font=("Goudy Stout", 14, "normal"), fg='green', wraplength=300)
        speed_label.pack()

    # Check result if enter clicked
    def result_check_enter(event):
        result = user_input.get("1.0", END).strip().split(" ")
        words_number = 0
        end = perf_counter()
        time = round((end - start), 2)
        for position in range(len(result)):
            if result[position] == word_for_type[position]:
                words_number += 1
        speed_label = Label(text=f'Your speed is {time}s per {words_number} correct words',
                            font=("Goudy Stout", 14, "normal"), fg='green', wraplength=300)
        speed_label.pack()


    words_list = ['read', 'country', 'number', 'said', 'first', 'down', 'same', 'than', 'through', 'began', 'between',
                  'while', 'follow', 'came', 'small', 'very', 'at', 'think', 'has', 'soon', 'then', 'food', 'far',
                  'all', 'some', 'so', 'me', 'same', 'list', 'something', 'must', 'may', 'help', 'oil', 'down',
                  'country', 'time', 'young', 'family', 'another', 'hard', 'family', 'to', 'open', 'air', 'keep',
                  'first', 'not', 'both', 'back', 'night', 'many', 'tree', 'me', 'side', 'get', 'she', 'fire', 'come',
                  'never', 'now', 'letter', 'open', 'man', 'your', 'below', 'along', 'ask', 'oil', 'her', 'come',
                  'world', 'any', 'mile', 'still', 'both', 'far', 'your', 'other', 'hand', 'by', 'another',
                  'sometimes', 'than', 'back', 'try', 'light', 'work', 'face', 'life', 'almost', 'part', 'have',
                  'change', 'go', 'ask', 'last', 'without', 'move', 'got', 'from', 'new', 'never', 'he', 'it', 'seem',
                  'long', 'seem', 'up', 'over', 'big', 'together', 'long', 'you', 'who',
                  'began', 'she', 'right', 'read', 'over', 'seem', 'come', 'family', 'did', 'said', 'line',
                  'try', 'over', 'need', 'example', 'food', 'country', 'from', 'another', 'be', 'white', 'on', 'part',
                  'any', 'long', 'with', 'went', 'will', 'left', 'add', 'write', 'hard', 'now', 'sun', 'is', 'letter',
                  'cut', 'more', 'sometimes', 'my', 'city', 'land', 'left', 'ask', 'plant', 'something', 'so', 'soon',
                  'the', 'he', 'why', 'walk', 'say', 'you', 'want', 'place', 'her', 'man', 'also', 'use', 'in', 'try',
                  'been', 'almost', 'different'
    ]
    # Choose a random word for testing from the list of words
    word_for_type = []
    while len(word_for_type) < 20:
        word = random.randint(0, (len(words_list)-1))
        word_for_type.append(words_list[word])

    text = " ".join(word_for_type)
    go_button.config(state='disabled')
    word_label = Label(text=text, font=("Tahoma", 14, "normal"), wraplength=300)
    word_label.pack()
    user_input = Text(width=50, height=5, font=("Tahoma", 14, "normal"))
    user_input.pack()
    user_input.focus_set()
    done_button = Button(text="Done", command=result_check, font=("Goudy Stout", 14, "normal"))
    done_button.pack()
    if not new_window:
        window.bind("<Return>", result_check_enter)
    else:
        new_window.bind("<Return>", result_check_enter)
    again_button = Button(text="Try again", command=create_window, font=("Goudy Stout", 14, "normal"))
    again_button.pack()
    # Time start point
    start = perf_counter()


# Starting info
name_label = Label(text='Typing speed test', font=("Goudy Stout", 20, "normal"))
name_label.pack()
info_label = Label(text="Push start and print the word below...", font=("Tahoma", 14, "normal"))
info_label.pack()
go_button = Button(text="Start", command=game, font=("Goudy Stout", 14, "normal"), state='normal')
go_button.pack()

window.mainloop()
