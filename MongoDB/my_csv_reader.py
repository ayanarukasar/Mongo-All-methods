import csv

class readCSV():
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        # opening the CSV file
        datalist = []
        with open(self.filename, mode='r') as file:
            # reading the CSV file
            csvFile = csv.DictReader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                #print(lines)
                datalist.append(lines)
        return datalist
