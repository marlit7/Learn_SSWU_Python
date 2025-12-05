# --------------------------- Homework_3  ------------------------------------
"""
 Електронне CV
"""
my_data={"ім`я": "Маргарита Литвиненко",
         "адреса": "м.Харків",
         "телефон":"+380667247754",
         "email": "virit9192@gmail.com"}

education = [
    "2009–2014 — Харківський національний університет радіоелектроніки",
    "Факультет телекомунікацій та вимірювальної техніки",
    "Спеціальність: інформаційні мережі зв’язку",
    "Кваліфікація: магістр"
]

skills=["ЄДЕБО",
        "МКР",
        "AzaPro",
        "FossDoc",
        "адміністрування баз даних",
        "навчання користувачів",
        "документообіг"]

experience = (
    "2014 – по теперішній час — Харківський національний автомобільно-дорожній університет",
    "Інженер",
    "Робота з базою ЄДЕБО, оновлення та перевірка даних",
    "Замовлення студентських квитків і дипломів",
    "Робота у внутрішніх інформаційних системах",
    "Навчання співробітників у МКР",
    "Документообіг у FossDoc",
    "Нарахування стипендій у AzaPro",
    "Актуалізація освітніх даних",
    "Взаємодія з факультетами та навчальним відділом"
)

try:
    failename="resume.txt"
    some_file = open(failename, 'w', encoding='utf-8')
    some_file.write("ПЕРСОНАЛЬНІ ДАНІ:\n")
    some_file.close()

    with open(failename, 'a', encoding='utf-8') as file:
        for key, value in my_data.items():
            file.write(f"   {key}: {value}\n")

    some_file = open(failename, 'a', encoding='utf-8')
    some_file.write("\nОСВІТА:\n")
    some_file.close()

    with open(failename, 'a', encoding='utf-8') as file:
        for edu in education:
            file.write(f"  - {edu}\n")

    some_file = open(failename, 'a', encoding='utf-8')
    some_file.write("\nНАВИЧКИ:\n")
    some_file.close()

    with open(failename, 'a', encoding='utf-8') as file:
        file.write("  - " + ", ".join(skills))

    some_file = open(failename, 'a', encoding='utf-8')
    some_file.write("\n\nДОСВІД:\n")
    some_file.close()

    with open(failename, 'a', encoding='utf-8') as file:
        for item in experience:
            file.write(f"  - {item}\n")


except FileNotFoundError:
    print("Помилка: файл не знайдено.")
else:
    print("Резюме створено.")

finally:
    print("Програма завершена.")


