#IC 1st 

#PRINTS ALL OF CONTENTwhile True:
import csv
while True:
    try:
            with open("Notes/reading.txt", "r") as file:
                content = file.read()
                print(content)

    except:
            print("that file can't be found")

    else:
            print("my code worked")
            break


while True:
    try:
            with open("Notes/reading.txt", "r") as file:
                for line in line:
                    print(f"hello{line.strip()}")

    except:
            print("that file can't be found")

    else:
            print("my code worked")
            break
while True:
    try:
            with open("Notes\sample.csv", mode = "r") as csv_file:
                    content = csv.reader(csv_file)
                    headers = next(content)
                    rows = []
                    for line in content:
                        rows.append({headers[0]: line[0], headers[1]: line[1]})
    except:
        print("can't find the Csv")
    else:
        print("code ends")
        break