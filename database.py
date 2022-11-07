import datetime


monday = ['2. Информатика - лаб. раб. ', '3. Информатика - лаб. раб']

tuesday = ['1. Физика - лаб. раб.', '2. Высшмат - практика',
        '3. Ин.Яз - практика', '4. Элективные дисциплины по физической культуре и спорту - практика', '5. Час куратора']

wednesday = ['2. ОТЦ - практика', '3. Физика - практика',
          '4. Высшмат - практика', '5. Инженерная и компьютерная графика - лаб. раб.']

thursday = ['3. Информатика - практика']

friday = ["2. Элективные дисциплины по физической культуре и спорту", '3. Высшмат - лекция', '4. ОТЦ - лекция']

saturday = ['1. Информатика - лекция', '2. Информатика - лекция']

#Формирование даты
class Today:
    today = datetime.datetime.now()
    today_str = today.strftime("%d-%m-%y")
    today_lst = today_str.split("-")
    day = today_lst[0]
    mounth = today_lst[1]

#Понедельник
mondaay = []
if Today.day == "07" or Today.day == "21":
    if Today.mounth == "11":
        for i in monday:
            mondaay.append(i)

elif Today.day == "05" or Today.day == "19":
    if Today.mounth == "12":
        for i in monday:
            mondaay.append(i)

else:
    mondaay = monday[2::]
    if len(mondaay) == 0:
        mondaay.append("Ура! Пар нет.")

#Вторник
tuesdaay = []
if Today.mounth == "10" or Today.mounth == "11":
    for i in tuesday:
        tuesdaay.append(i)
elif Today.mounth == "12":
    tuesday[3] = "Инженерная и компьютерная графика - лаб. раб"
    for i in tuesday:
        tuesdaay.append(i)
else:
    for i in tuesday[1::]:
        tuesdaay.append(i)
    
#Среда
wednesdaay = []
if Today.day == "16" or Today.day == "23" or Today.day == "30":
    if Today.mounth == "11":
        wednesday[1] == "Физическая культура и спорт - практика"
        for i in wednesday:
            wednesdaay.append(i)
else:
    for i in wednesday:
        wednesdaay.append(i)

#Пятница
fridaay = []
if Today.day == "11" and Today.mounth == "11":
    friday[0] = "Физика - лекция"
    for i in friday:
        fridaay.append(i)
else:
    fridaay = friday
