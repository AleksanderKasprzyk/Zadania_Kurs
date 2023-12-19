import sys
import json
import csv

class FileModifier:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes

    def read_file(self):
        raise NotImplementedError("Subclasses must implement the read_file method")

    def apply_changes(self):
        raise NotImplementedError("Subclasses must implement the apply_changes method")

    def display_contents(self):
        raise NotImplementedError("Subclasses must implement the display_contents method")

    def write_file(self):
        raise NotImplementedError("Subclasses must implement the write_file method")

class CsvFileModifier(FileModifier):
    def read_file(self):
        with open(self.input_file, 'r') as f:
            reader = csv.reader(f)
            self.data = [row for row in reader]

    def apply_changes(self):
        for change in self.changes:
            x, y, value = change.split(',')
            x, y = int(x), int(y)
            self.data[y][x] = value

    def display_contents(self):
        for row in self.data:
            print(','.join(row))

    def write_file(self):
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)

class JsonFileModifier(FileModifier):
    def read_file(self):
        with open(self.input_file, 'r') as f:
            self.data = json.load(f)

    def apply_changes(self):
        for change in self.changes:
            x, y, value = change.split(',')
            x, y = int(x), int(y)
            self.data[y][x] = value

    def display_contents(self):
        print(json.dumps(self.data, indent=4))

    def write_file(self):
        with open(self.output_file, 'w') as f:
            json.dump(self.data, f, indent=4)

class TxtFileModifier(FileModifier):
    def read_file(self):
        with open(self.input_file, 'r') as f:
            self.data = [line.rstrip('\n') for line in f]

    def apply_changes(self):
        for change in self.changes:
            x, y, value = change.split(',')
            x, y = int(x), int(y)
            line = self.data[y]
            line = line[:x] + value + line[x + len(value):]
            self.data[y] = line

    def display_contents(self):
        for line in self.data:
            print(line)

    def write_file(self):
        with open(self.output_file, 'w') as f:
            f.write('\n'.join(self.data))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python reader.py <input_file> <output_file> <change_1> <change_2> .... <change_n>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    file_extension = input_file.split('.')[-1]

    if file_extension == 'csv':
        modifier = CsvFileModifier(input_file, output_file, changes)
    elif file_extension == 'json':
        modifier = JsonFileModifier(input_file, output_file, changes)
    elif file_extension == 'txt':
        modifier = TxtFileModifier(input_file, output_file, changes)
    else:
        print("Unsupported file format.")
        sys.exit(1)

    modifier.read_file()
    modifier.apply_changes()
    modifier.display_contents()
    modifier.write_file()