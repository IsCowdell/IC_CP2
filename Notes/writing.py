#with open("Notes/reading.txt" ,'r+') as file:
    #content = file.read()
    #content += "\n I wrote on my file"
    #file.write(content)


#with open("Notes/writing.txt" ,'a') as file:
   # file.write("\nI wrote on my filer")
#print("code end")

#writing to csv
import csv

with open("Notes\\sample.csv",'a',newline = '') as csv_file:
    fieldname = ['username','color']
    writer = csv.DictWriter(csv_file,fieldnames=fieldname)

    writer.writerow({'username' : 'jacob' ,'color' : 'oranage'})
    writer.writerow({'username' : 'fugey' ,'color' : 'yellow'})
    writer.writerow({'username' : 'dounge' ,'color' : 'pink'})
    writer.writerow({'username' : 'yellow' ,'color' : 'red'})
    writer.writerow({'username' : 'tacob' ,'color' : 'blue'})

print("code is done")


#writing and read to csv
import csv

with open("Notes\\sample.csv",'r+',newline = '') as csv_file:
    fieldname = ['username','color']
    reader = csv.reader(csv_file)
    for line in reader:
        print(f"{fieldname[0]}, {line[0]}color {line[1]}")
    writer = csv.DictWriter(csv_file,fieldnames=fieldname)

    writer.writerow({'username' : 'jacob' , 'color' : 'oranage'})
    writer.writerow({'username' : 'fugey' , 'color' : 'yellow'})
    writer.writerow({'username' : 'dounge', 'color' : 'pink'})
    writer.writerow({'username' : 'yellow', 'color' : 'red'})
    writer.writerow({'username' : 'tacob', 'color' : 'blue'})

print("code is done")


