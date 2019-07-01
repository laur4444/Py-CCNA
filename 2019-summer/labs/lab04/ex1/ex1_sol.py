CSV_FILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    with open(CSV_FILE, "r") as f:
        data = []
        columns = f.readline()
        columns = columns.strip('\n')
        features = columns.split(',')
        for line in f:
            line = line.strip('\n')
            values = line.split(',')
            dictionary = dict(zip(features, values))
            data.append(dictionary)
    return data

print(parse_file(CSV_FILE))
