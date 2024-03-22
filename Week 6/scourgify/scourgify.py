import sys
import csv

# def main():
#     if len(sys.argv) == 1 or len(sys.argv) == 2:
#         print("Too few command-line arguments")
#         sys.exit(1)
#     elif len(sys.argv) > 3:
#         print("Too many command-line arguments")
#         sys.exit(1)
#     elif len(sys.argv) == 3:
#         # Check if first file ends in '.csv'
#         try:
#             in_file = sys.argv[1].split(".")
#             out_file = sys.argv[2].split(".")
#             if len(in_file) == 1 or (len(in_file) > 1 and in_file[1] != "csv"):
#                 print(f"Could not read {sys.argv[1]}")
#                 sys.exit(1)
#             if len(out_file) == 1 or (len(out_file) > 1 and out_file[1] != "csv"):
#                 print(f"Could not read {sys.argv[2]}")
#                 sys.exit(1)
#             else:
#                 students = []
#                 with open(sys.argv[1]) as file:
#                     reader = csv.DictReader(file)
#                     for row in reader:
#                         first_last = row["name"].strip("'").split(",")
#                         students.append({"first": first_last[1], "last": first_last[0], "house": row["house"]})

#                 with open(sys.argv[2], "w") as file:
#                     writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
#                     writer.writeheader()
#                     for student in students:
#                         writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})
                

#         except FileNotFoundError:
#             print(f"Could not read {sys.argv[1]}")
#             sys.exit(1)

def scourgify(in_file, out_file):
    students = []
    with open(in_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_last = row["name"].strip().split(",")
            students.append({"first": first_last[1], "last": first_last[0], "house": row["house"]})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow({"first": student["first"].strip(), "last": student["last"], "house": student["house"]})

def main():
    try:
        if len(sys.argv) == 1 or len(sys.argv) == 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            scourgify(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()