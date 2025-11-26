from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/assignWithCsv")
def assignWithCsv():
    with open("soldiers.csv", "a") as text:
        reader = csv.reader(text.splitlines())
        rows = [row for row in reader]
        columns = rows[0]
        rows = rows[1:]




def readcsv(csvfile_name):
    with open(csvfile_name) as csvfile:
        file = csv.reader(csvfile, delimiter = ",")
        skiprows = 1
        for i in range(skiprows):
            _ = next(file)
            for z in file:
                z[:2] = map(int, z[:2])
                z[2:] = map(float, z[2:])
                print(z[:2])
        return






if __name__ == "__main__":