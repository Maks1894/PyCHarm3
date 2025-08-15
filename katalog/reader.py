import sys
import csv
import os

def main ():
    if len(sys.argv) < 3:
        print("Podaj poprawna sciezke do uruchomienia pliku: python reader.py <plik_wejsciowy> <plik_wyjsciowy> [<zmiana_1> <zmiana_2> ...]")
        return
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        changes = sys.argv[3:]
        modified_data = read_and_modify_csv(input_file, changes)
        write_csv(output_file, modified_data)
        print(f'Plik {input_file} zostal zmodyfikowany:')
        output_file_path = os.path.join('katalog', output_file)
        with open(output_file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
        print(f" Plik został pomyślnie zapisany jako '{output_file}'.")

def read_and_modify_csv(input_file, changes):
    full_path = os.path.join('katalog', input_file)
    with open(full_path,  newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    for change in changes:
        parts = change.split(',')
        if len(parts) == 3:
            col_str, row_str, value = parts
            col = int(col_str)
            row = int(row_str)
            if 0 <= row < len(data) and 0 <= col < len(data[row]):
                data[row][col] = value
            else:
                print(f"podales danne kloumny{col} i wiersza {row} po za zakresem  dannych tablicy z pliku in.csv")
        else:
            print(f" niprawidlo podane danny{change}, podaj danne w formacie \"kolumna,wiersz,wartość\" ")

    return data
def write_csv(output_file, data):
    full_path = os.path.join('katalog', output_file)
    with open(full_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
if __name__== "__main__":
    main()