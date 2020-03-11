lang_dict = {1: "English",
            2: "Spanish",
            3: "Portuguese"
}

def print_language_options(Dict[int, str]):

    for x in lang_options:
        print(str(x) + ": " + lang_options[x])

print_language_options(lang_dict)

def print_language_options(Dict[int, str]):

	for key, value in lang_options.items():
        print(key, value)