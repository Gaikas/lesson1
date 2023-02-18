import sqlite3
conn = sqlite3.connect("conference.db")
curs = conn.cursor()
table1 = """CREATE TABLE IF NOT EXISTS CONFERENCE(
            Название TEXT,
            Дата TEXT,
            Место TEXT,
            Организаторы TEXT,
            Спонсоры TEXT,
            Количество_дней INTEGER,
            Количество_участников INTEGER,
            Количество_докладчиков INTEGER);"""
table2 = """CREATE TABLE IF NOT EXISTS STAFF(
            ФИО TEXT,
            Ученая_степень TEXT,
            Научное_направление TEXT,
            Место_работы TEXT,
            Кафедра TEXT,
            Должность TEXT,
            Страна TEXT,
            Город TEXT,
            Адрес TEXT,
            Рабочий_телефон INTEGER,
            Email TEXT);"""
table3 = """CREATE TABLE IF NOT EXISTS PARTICIPANTS(
            Докладчик_или_участник TEXT,
            Рассылка_приглашения_дата TEXT,
            Поступление_заявки_дата TEXT,
            Тема_доклада TEXT,
            Отметка_о_поступлении_тезисов TEXT,
            Приезд_дата TEXT,
            Потребность_в_гостинице TEXT,
            Отъезд_дата TEXT);"""
curs.execute(table1)
conn.commit()
curs.execute(table2)
conn.commit()
curs.execute(table3)
conn.commit()

zap7 = """DELETE FROM CONFERENCE WHERE Количество_дней = 1;"""
curs.execute(zap7)
conn.commit()
zap8 = """DELETE FROM CONFERENCE WHERE Место = 'Минск' ;"""
curs.execute(zap8)
conn.commit()
zap9 = """UPDATE CONFERENCE SET Место = 'Париж' WHERE Место = 'Казань';"""
curs.execute(zap9)
conn.commit()
zap10 = """UPDATE CONFERENCE SET Дата = '15.07.2023';"""
curs.execute(zap10)
conn.commit()
zap11 = """UPDATE CONFERENCE SET Спонсоры = 'ИП Пупкин З.В.' WHERE Название = 'Технологии21';"""
curs.execute(zap11)
conn.commit()


# zap4 = """SELECT * FROM CONFERENCE;"""
# curs.execute(zap4)
# vyb4 = curs.fetchall()
# print(vyb4)
# zap5 = """SELECT * FROM STAFF;"""
# curs.execute(zap5)
# vyb5 = curs.fetchall()
# print(vyb5)
# zap6 = """SELECT * FROM PARTICIPANTS;"""
# curs.execute(zap6)
# vyb6 = curs.fetchall()
# print(vyb6)
# zap7 = """SELECT * FROM PARTICIPANTS WHERE Докладчик_или_участник="Докладчик";"""
# curs.execute(zap7)
# vyb7 = curs.fetchall()
# print(vyb7)


# list1 = ["Ядерная физика", "17.02.2023", "Казань", "ООО Лютик", "Банк Приорбанк", 3, 50, 6]
# zap1_1 = """INSERT INTO CONFERENCE VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap1_1, list1)
# conn.commit()
# tupple1 = ("Инновации будущего", "25.03.2023", "Минск", "ОАО Зебра", "Радио Юнистар", 1, 150, 7)
# zap1_2 = """INSERT INTO CONFERENCE VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap1_2, tupple1)
# conn.commit()
# zap1_3 = """INSERT INTO CONFERENCE (Название, Организаторы, Количество_дней) VALUES("Бада-Бум", "ЗАО Роман", 1); """
# curs.execute(zap1_3)
# conn.commit()
# list1_1 = ["Сельхоз будущего", "25.02.2023", "Тбилиси", "ООО МинералАгро", "Банк Белгазпром", 3, 300, 8]
# zap1_4 = """INSERT INTO CONFERENCE VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap1_4, list1_1)
# conn.commit()
# zap1_5 = """INSERT INTO CONFERENCE (Название, Дата, Организаторы) VALUES("Технологии21", "06.03.2023", "ЗАО ЗОВ"); """
# curs.execute(zap1_5)
# conn.commit()
# tupple1_1 = ("Экспо-23", "27.06.2023", "Минск", "ОАО Рубик", "ООО Глобал Сэйлс", 10, 7350, 26)
# zap1_6 = """INSERT INTO CONFERENCE VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap1_6, tupple1_1)
# conn.commit()
#
#
# list2 = ["Иванов Иван Иванович", "Доктор наук", "Физика", "РГСУ", "Прикладных наук",
#          "Профессор", "РБ", "Минск", "ул. Кедышко 18", 173413042, "iviv@mail.ru"]
# zap2_1 = """INSERT INTO STAFF VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap2_1, list2)
# conn.commit()
# tupple2 = ("Петров Петр Петрович", "Доктор наук", "Философия", "БНТУ", None,
#            "Профессор", "РБ", "Минкс", None, 17123456, "bnty@gmail.com")
# zap2_2 = """INSERT INTO STAFF VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap2_2, tupple2)
# conn.commit()
# zap2_3 = """INSERT INTO STAFF (ФИО, Место_работы, Страна, Город)
#             VALUES("Кузьмин Григорий Васильевич", "БГУ", "РБ", "Бобройск"); """
# curs.execute(zap2_3)
# conn.commit()
# list2_1 = ["Кукушкин Генадий Геннадьевчи", "Кондитат", "Биология", None, "Биология", "Помощник преподавателя",
#            "Грузия", "Тбилиси", None, 259874564, "genna@gmail.com"]
# zap2_4 = """INSERT INTO STAFF VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap2_4, list2_1)
# conn.commit()
# zap2_5 = """INSERT INTO STAFF (ФИО, Место_работы, Страна, Email)
#             VALUES("Жидкевич О.А.", "Гарвард", "USA", "garvardcool@gmail.com"); """
# curs.execute(zap2_5)
# conn.commit()
# tupple2_1 = ("Нарейко Галина Геннадьевна", "Доктор наук", None, "БГЭУ", None, "Ученик", "РБ", "Минкс",
#              None, 298762460, "kyky@gmail.com")
# zap2_6 = """INSERT INTO STAFF VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap2_6, tupple2_1)
# conn.commit()
#
#
# list3 = ["Докладик", "05.02.2023", "07.02.2023", "Влияние тли на рожь", "Тезисы есть",
#          "23.02.2023", "Бронь гостиницы", "25.02.2023"]
# zap3_1 = """INSERT INTO PARTICIPANTS VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap3_1, list3)
# conn.commit()
# tupple3 = ("Участник", "15.03.2023", None, None, None, "25.03.2023", "Бронь гостиницы", "26.03.2023")
# zap3_2 = """INSERT INTO PARTICIPANTS VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap3_2, tupple3)
# conn.commit()
# zap3_3 = """INSERT INTO PARTICIPANTS (Докладчик_или_участник, Рассылка_приглашения_дата, Тема_доклада)
#             VALUES("Докладчик", "15.03.2023", "Физика в космосе"); """
# curs.execute(zap3_3)
# conn.commit()
# list3_1 = ["Участкик", "05.02.2023", "07.02.2023", None, None, "26.03.2023", None, "27.03.2023"]
# zap3_4 = """INSERT INTO PARTICIPANTS VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap3_4, list3_1)
# conn.commit()
# zap3_5 = """INSERT INTO PARTICIPANTS (Докладчик_или_участник, Рассылка_приглашения_дата, Приезд_дата)
#             VALUES("Участник", "15.03.2023", "26.03.2023"); """
# curs.execute(zap3_5)
# conn.commit()
# tupple3_1 = ("Докладчик", "13.03.2023", "13.03.2023", "Современное общество", "Тезисы есть",
#              "25.03.2023", "Бронь гостиницы", "26.03.2023")
# zap3_6 = """INSERT INTO PARTICIPANTS VALUES(?, ?, ?, ?, ?, ?, ?, ?); """
# curs.execute(zap3_6, tupple3_1)
# conn.commit()


curs.close()
conn.close()
