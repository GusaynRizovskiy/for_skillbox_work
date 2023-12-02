import re
text = "Even if they are djinns, I will get djinns that can outdjinn them."
patter_one = r"[aeyuoiAIEYUO]\w{0,}"
print(re.findall(patter_one,text))
result_2 = re.findall(r"\b[^aAeEiIoOuUyY\W]\w*", text)
print("Слова на любой символ, кроме гласной:", result_2)
