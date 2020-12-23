import csv

data = ["id,username,email,ip_address", 
        "1,root,root@example.com,192.168.0.1", 
        "2,admin,admin@example.com,192.168.0.2", 
        "3,test_user,test_user@example.com,192.168.0.3", 
        "4,second_user,second_user@example.com,192.168.0.4"]

path = "data.csv"


def csv_write(data, path):
    with open(path, 'w') as csv_file:
       csv_writer = csv.writer(csv_file)
       for line in data:
            csv_writer.writerow(line.split(","))

csv_write(data, path)

def csv_read(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("       ".join(row))

csv_read(path)
