import csv
class Highschool:
    def __init__(self, SIIR_code, SIRUES_code, name = '?', locality = '?', region = '?'):
        
        self.SIIR_code       = SIIR_code
        self.SIRUES_code     = SIRUES_code
        self.name            = name.lower()
        self.locality        = locality.lower()
        self.region          = region

    def __str__(self):
        return str(self.SIIR_code + ' ' + self.SIRUES_code + ' ' + self.name + ' ' + self.locality
                     + ' ' + self.region)


def create_dictionary(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)
        line_index = 0
        highschools = {}
        for row in reader:
            current_highschool = Highschool(row[0], row[1], row[3], row[5], row[16])
            highschools[row[0]] = current_highschool
            line_index += 1
            
    return highschools

if __name__ == "__main__":
    csv_file = r'/home/sebastian/Dropbox/Facultate/BacStats/BAC_2019_statistics/data/2019/unitati_scolare_2019.csv'
    highschools = create_dictionary(csv_file)