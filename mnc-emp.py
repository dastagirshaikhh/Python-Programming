import csv
import random


def generate_age():
    return random.randint(22, 60)


def generate_monthly_income():
    return random.randint(4000, 10000)


random_names = [f"Person_{i}" for i in range(1, 101)]

job_titles = ["Jr Developer", "Sr Developer", "Tester"]
roles = [random.choice(job_titles) for _ in range(100)]

unique_ids = [f"ID{i}" for i in range(1, 101)]  # Generate unique IDs dynamically

ages = [generate_age() for _ in range(100)]  # Generate 100 ages
incomes = [
    generate_monthly_income() for _ in range(100)
]  # Generate 100 monthly incomes

data = [
    {"Name": name, "ID": uid, "Job Title": role, "Age": age, "Monthly Income": income}
    for name, uid, role, age, income in zip(
        random_names, unique_ids, roles, ages, incomes
    )
]

csv_file = "EmployeeData.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["Name", "ID", "Job Title", "Age", "Monthly Income"]
    )

    writer.writeheader()

    writer.writerows(data)


print(f"CSV file '{csv_file}' created successfully.")
