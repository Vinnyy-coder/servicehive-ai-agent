import csv
import os


def save_lead(name, email):
    file_path = "leads.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Email"])

        writer.writerow([name, email])

