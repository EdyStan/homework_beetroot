import sqlite3
from person import BusDriver, Student, Patient, Person

conn = sqlite3.connect('persons.db')

c = conn.cursor()

# c.execute("""CREATE TABLE persons (
#             name text,
#             age text,
#             gender integer
#             )""")


def insert_pers(pers):
    with conn:
        c.execute(f"""INSERT INTO persons VALUES (:name, :age, :gender)""",
                  {'name': pers.name, 'age': pers.age, 'gender': pers.gender})


def get_pers_by_gender(gender):
    c.execute("SELECT * FROM persons WHERE gender = :gender", {'gender': gender})
    return c.fetchall()


def remove_emp(pers):
    with conn:
        c.execute("""DELETE from persons WHERE name = :name AND age = :age""",
                  {'name': pers.name, 'age': pers.age})


pers_1 = Patient('John', 19, 'male')
pers_2 = BusDriver('Jane', 30, 'female')
pers_3 = Student('Billy', 13, 'male')

insert_pers(pers_1)
insert_pers(pers_2)
insert_pers(pers_3)

persons = get_pers_by_gender('male')
print(persons)

remove_emp(pers_1)

persons = get_pers_by_gender('male')
print(persons)

conn.close()
