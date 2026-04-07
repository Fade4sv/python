from smartphone import Smartphone
# 1. первый вариант, как хотел реализовать
# tel1 = Smartphone("iphone 13", "pro", "+7 909 222 01 89")
# tel2 = Smartphone("iphone 14", "pro", "+7 909 222 83 65")
# tel3 = Smartphone("iphone 15", "pro", "+7 909 222 99 99")
# catalog = [tel1, tel2, tel3]
# print(tel1.mark, tel1.model, "-", tel1.number)
# print(tel2.mark, tel2.model, "-", tel2.number)
# print(tel3.mark, tel3.model, "-", tel3.number)
# 2. второй вариант как подсказывали в подготовке к домашке
catalog = [Smartphone("iphone 13", "pro", "+7 909 222 01 89"),
           Smartphone("iphone 14", "pro", "+7 909 222 83 65"),
           Smartphone("iphone 15", "pro", "+7 909 222 99 99")]
for smartphone in catalog:
    print(f"{smartphone.mark} {smartphone.model} - {smartphone.number}")
