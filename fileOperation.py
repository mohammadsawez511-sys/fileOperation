
import os

class InvalidGenderException(Exception):
    def __str__(self):
        return "Please enter M for male and F for female"


class InvalidmarksException(Exception):
    def __str__(self):
        return "Compulsorily enter 3 subject marks"


class fileoperation:

    def __init__(self, n, file_name):
        os.chdir("D:\\fileOperations")
        self.n = n
        self.file_name = file_name

    def writeData(self):
        Allstudent = []

        try:
            for i in range(self.n):

                r = int(input("Enter roll number: "))
                name = input("Enter name: ")
                gender = input("Enter M for male and F for female: ").upper()

                if gender not in ("M", "F"):
                    raise InvalidGenderException()

                marks = list(map(int, input("Enter 3 subject marks: ").split()))

                if len(marks) != 3:
                    raise InvalidmarksException()

                total = sum(marks)
                percentage = round(total / len(marks), 2)

                student = [r, name, gender, marks, total, percentage]
                Allstudent.append(student)

            with open(self.file_name, "w") as f1:

                for i in Allstudent:
                    for data in i:
                        if isinstance(data, list):
                            for x in data:
                                f1.write(str(x) + "  ")
                        else:
                            f1.write(str(data) + "  ")

                    f1.write("\n")

            print("ALL THE DATA IS SUCCESSFULLY ADDED INTO FILE")

        except ValueError:
            print("Enter roll number or marks in integer form!")

        except InvalidGenderException as e:
            print(e)

        except InvalidmarksException as e:
            print(e)

        except FileNotFoundError:
            print("File may be not present!")

        except Exception as e:
            print(e)

    def backupData(self):
        try:
            with open(self.file_name, "r") as f1:
                with open("backup.txt", "w") as f2:
                    f2.write(f1.read())

            print("File backup created!")

        except FileNotFoundError:
            print("File may be not present!")

        except Exception as e:
            print(e)

    def addNewstudent(self):
        try:
            print("\nEnter new data")

            r = int(input("Enter roll number: "))
            name = input("Enter name: ")
            gender = input("Enter M for male and F for female: ").upper()

            if gender not in ("M", "F"):
                raise InvalidGenderException()

            marks = list(map(int, input("Enter 3 subject marks: ").split()))

            if len(marks) != 3:
                raise InvalidmarksException()

            total = sum(marks)
            percentage = round(total / len(marks), 2)

            with open(self.file_name, "a") as f3:
                f3.write(f"{r} {name} {gender} ")

                for x in marks:
                    f3.write(str(x) + " ")

                f3.write(f"{total} {percentage}\n")

            print("New student data added successfully!")

        except ValueError:
            print("Enter roll number or marks in integer form!")

        except InvalidGenderException as e:
            print(e)

        except InvalidmarksException as e:
            print(e)

        except FileNotFoundError:
            print("File may be not present!")

        except Exception as e:
            print(e)


f1 = fileoperation(2, "student.txt")

f1.writeData()
f1.backupData()
f1.addNewstudent()
