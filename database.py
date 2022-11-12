import datetime


class Today:
    """
    Класс, отвечающий за формирование актуальной даты.
    :return: today_lst (список с текущим днем и месяцем)
    """
    @classmethod
    def update_date(cls):
        today = datetime.datetime.now()
        today_str = today.strftime("%d-%m-%y")
        today_lst = today_str.split("-")
        return today_lst


day = Today.update_date()[0]
mounth = Today.update_date()[1]


#Приписка usually означает, что это стандартное расписание на этот день недели.
monday_usually = ["2. Информатика - лаб. раб. ", "3. Информатика - лаб. раб"]

tuesday_usually = [
    "1. Физика - лаб. раб.",
    "2. Высшмат - практика",
    "3. Ин.Яз - практика",
    "4. Элективные дисциплины по физической культуре и спорту - практика",
    "5. Час куратора",
]

wednesday_usually = [
    "2. ОТЦ - практика",
    "3. Физика - практика",
    "4. Высшмат - практика",
    "5. Инженерная и компьютерная графика - лаб. раб.",
]

thursday_usually = ["3. Информатика - практика"]

friday_usually = [
    "2. Элективные дисциплины по физической культуре и спорту",
    "3. Высшмат - лекция",
    "4. ОТЦ - лекция",
]

saturday_usually = ["1. Информатика - лекция", "2. Информатика - лекция"]


# Приписка actually означает, что расписание на этот день недели может изменяться в зависимости от дня/месяца.
# Всего дней в неделе, когда расписание может измениться, четыре: понедельник, вторник, среда, пятница. К ним
# добавляется приписка actually. Эти же списки выводятся в словаре raspisanie_dict.

# Понедельник
monday_actually = []
if (
    mounth == "11"
    or mounth == "12"
    and (
        day == "07" or day == "21" or day == "05" or day == "19"
    )
):
    for i in monday_usually:
        monday_actually.append(i)

else:
    monday_actually = monday_usually[2::]
    if len(mondaay) == 0:
        mondaay.append("Ура! Пар нет.")

# Вторник
tuesday_actually = []
if mounth == "10" or mounth == "11":
    for i in tuesday_usually:
        tuesday_actually.append(i)

elif mounth == "12":
    tuesday[3] = "Инженерная и компьютерная графика - лаб. раб"
    for i in tuesday_usually:
        tuesday_actually.append(i)

else:
    for i in tuesday_usually[1::]:
        tuesday_actually.append(i)


# Среда
wednesday_actually = []
if mounth == "11" and (
    day == "16" or day == "23" or day == "30"
):
    wednesday_usually[1] == "Физическая культура и спорт - практика"
    for i in wednesday_usually:
        wednesday_actually.append(i)
else:
    for i in wednesday_usually:
        wednesday_actually.append(i)

# Пятница
friday_actually = []
if day == "11" and mounth == "11":
    friday[0] = "Физика - лекция"
    for i in friday_usually:
        friday_actually.append(i)
else:
    friday_actually = friday_usually

# Словарь с расписанием. Если на конце actually - расписание в этот день недели может меняться.
# Если на конце usually - расписание в этот день недели всегда одно и то же.
raspisanie_dict = {
    "понедельник": monday_actually,
    "вторник": tuesday_actually,
    "среда": wednesday_actually,
    "четверг": thursday_usually,
    "пятница": friday_actually,
    "суббота": saturday_usually
}


