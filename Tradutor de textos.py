from translate import Translator
s = Translator(from_lang="portuguese",
    to_lang = "English")
res = s.translate("Olá pessoal")
print(res)
