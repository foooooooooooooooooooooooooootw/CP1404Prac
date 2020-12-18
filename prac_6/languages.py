from prac_6.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)

language_list = []
language_list.append(ruby)
language_list.append(python)
language_list.append(visual_basic)

print("The dynamically typed languages are:")
for language in language_list:
    if language.is_dynamic():
        print(repr(language.name).replace("'", ""))