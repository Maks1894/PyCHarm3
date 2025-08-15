import sys
import csv
import os

def read_csv(input_file):
    fail_path = os.path.join('danne', input_file)
    with open(fail_path,  newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
def validate_coordinates (data, row, col):
    if  row  < 0 or row >= len(data):
            print("Podano bledny numer wiersza")
            return False
    if col < 0 or col >= len(data[0]):
        print("Podano bledny numer kolumny")
        return False
    return True
def modifa_data(data, row, col, value):
    if validate_coordinates(data, row, col):
        data[row][col] = value
        return data

def write_csv(data, output_file):
    fail_path = os.path.join('danne', output_file)
    with open(fail_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main ():

    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        changes = sys.argv[3:]
        data = read_csv(input_file)
        for change in changes:
            parts = change.split(',')
            if len(parts) == 3:
                col_str, row_str, value = parts
                col = int(col_str)
                row = int(row_str)
                data = modifa_data(data, row, col, value)

            else:
                print(f" niprawidlo podane danny{change}, podaj danne w formacie \"kolumna,wiersz,wartość\" ")
        write_csv(data, output_file)
        print(f'Plik {input_file} zostal zmodyfikowany:')
        output_file_path = os.path.join('danne', output_file)
        with open(output_file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
        print(f" Plik został pomyślnie zapisany jako '{output_file}'.")
    else: print("Podaj poprawna sciezke do uruchomienia pliku: python reader.py <plik_wejsciowy> <plik_wyjsciowy> [<zmiana_1> <zmiana_2> ...]")


if __name__ == "__main__":
    main()