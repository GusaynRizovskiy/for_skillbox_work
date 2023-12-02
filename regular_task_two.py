import re
text = "How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?"
print("Список всех упоминаний шаблона: ", re.findall(r"\\wwood\+\?",text))