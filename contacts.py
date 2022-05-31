contacts = {
    "number":4,
    "students":
        [
            {"name":"Naturo Uzumaki", "email": "iloveramen@example.com"},
            {"name":"Sakura Haruno", "email": "shannaro@example.com"},
            {"name":"Sasuke Uchiha", "email": "chidori@example.com"},
            {"name":"Hatake Kakashi", "email": "sorryimlate@example.com"}
        ]
}

for student in contacts["students"]:
    print(student["email"])