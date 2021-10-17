# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
import re

ext = ()
user_words = ()
file_readed = ""
F_path = ""


def read_template(path):
    """
    This Function Reads the Story textt file.
    """
    global F_path
    F_path = path
    try:
        with open(F_path, "r") as f:
            global file_readed
            file_readed = f.read()
            f.close()
            return (file_readed)
    except NameError:
        raise FileNotFoundError


def parse_template(parse_txt):
    """
    This Function prepares the story textt for user inputs.
    """
    pattern = r"{([A-Za-z0-9\s'-]+)}"
    global ext
    global file_readed
    parse_txt = file_readed
    ext = re.findall(pattern, parse_txt)
    with open(F_path, "r") as File, open("Files/paresed.txt", "w+") as write_:
        for line in File:
            for word in ext:
                line = line.replace(word, "")
            write_.write(line)
        File.close()
        write_.close()
    return (read_template("Files/paresed.txt"), tuple(ext))


def prompt_user(path):
    """
This function stores user inputs.
    """
    print(
        """
Tell us your own story!
    """
    )

    print(
        read_template(path)
    )

    for word in ext:
        user_input_word = input("""Replace "{}" word: > """.format(word))
        global user_words
        user_words += (user_input_word,)


def merge(parsed_text, user_inputs):
    """
This Function Merges users inputs with the story-sets then --> print the users story.
    """
    user_inputs = list(user_inputs)
    with open("Files/paresed.txt", "r") as file, open("Files/user_story_template.txt", "w+") as write_new:
        i = 0
        for line in file:
            for character in line:
                if character == "{":
                    character = user_inputs[i]
                    i += 1
                if character == "}":
                    character = ""
                write_new.write(character)
        file.close()
        write_new.close()

    users_story = (read_template("Files/user_story_template.txt"))
    print(users_story)
    return (users_story)


def welcome():
    """
This function prints out the welcome message & game requierments to users.
    """

    print(
        """
        😁 Welcome to Madlib game 😉!

read the story, then simply input words matching
the description inside same extact order then
the game will give your own version of the story!
    """
    )


if __name__ == "__main__":
    path = "Files/make_me_a_video_game_template.txt"
    parsed_text = read_template("Files/paresed.txt")
    welcome()
    read_template(path)
    parse_template(file_readed)
    prompt_user(path)
    merge(parsed_text, user_words)
