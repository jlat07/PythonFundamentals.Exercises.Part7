from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: 'English' , 2: 'Spanish'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?', 2: '?Como te llamas?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: 'Hello', 2: 'Hola'
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print('Please choose language')
    for key, value in lang_options.items():
        print(f'{key}: {value}')


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    return (int(input()))

def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    
    if lang_options.get(lang_choice) is not None:
        return True
    else:
        return False


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    a = name_prompt_options.get(lang_choice)

    return a


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    b = input(name_prompt)

    return b


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    greeting = f'{greetings_options.get(lang_choice)} {name}'
    print(greeting)


def user_admin_selection():
    x = input("1. Admin \n2. User\n")
    return x

def edit_or_add_selection():
    x = input("1. Add Language \n2. Update Greeting\n")
    return x

def edit_or_add(edit_admin):
    if edit_admin == "1":
        admin_start_language(determine_start_place(lang_dict))
    if edit_admin == "2":
        select_lang_change()

def select_lang_change():
    print(lang_dict)
    x = input("What language would you like to edit?\n")
    x = int(x)
    test_lang(x)
    change_name_prompt(x)

def test_lang(x):
    if x in lang_dict == True:
        return x
    elif x in lang_dict == False:
        print("Invalid Option")
        select_lang_change()

def change_name_prompt(lang_in):
    x = input("Please input new name propmt:\n")
    name_prompt_dict[lang_in]=x
    change_greeting_prompt(lang_in)

def change_greeting_prompt(lang_in):
    x = input("Update greeting:\n")
    greetings_dict[lang_in] = x


def determine_start_place(dict):
    for x in dict:
        last = x
    y = x +1
    return y

def admin_start_language(key):
    x = input("Add a language: \n")
    lang_dict[key] = x
    admin_start_name_prompt(determine_start_place(name_prompt_dict))

def admin_start_name_prompt(key):
    x = input("Input your desired name prompt: \n")
    name_prompt_dict[key] = x
    admin_start_greeting(determine_start_place(greetings_dict))

def admin_start_greeting(key):
    x = input("Input desired greeting: \n")
    greetings_dict[key] = x


def user_or_admin(user_admin_pick):
    str(user_admin_pick)
    if user_admin_pick == "1":
        edit_or_add(edit_or_add_selection())
        user_admin_selection()
    if user_admin_pick == "2":
        pass
    else:
        print("Invalid selection, Try again.")
        user_admin_pick




if __name__ == '__main__':
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)