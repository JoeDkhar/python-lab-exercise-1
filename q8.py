people = [
    {"name": "John Doe", "age": 30, "bloodgroup": "A+"},
    {"name": "Jane Smith", "age": 25, "bloodgroup": "B-"},
    {"name": "Michael Johnson", "age": 35, "bloodgroup": "O+"},
    {"name": "Emily Brown", "age": 28, "bloodgroup": "AB-"},
    {"name": "David Lee", "age": 40, "bloodgroup": "A-"},
    {"name": "Sarah Kim", "age": 22, "bloodgroup": "B+"},
    {"name": "Daniel Wilson", "age": 32, "bloodgroup": "O-"},
    {"name": "Olivia Carter", "age": 27, "bloodgroup": "AB+"},
    {"name": "Ethan Miller", "age": 38, "bloodgroup": "A+"},
    {"name": "Sophia Davis", "age": 29, "bloodgroup": "B-"}
]
for person in people:
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Blood Group: {person['bloodgroup']}")
    print("-" * 20)