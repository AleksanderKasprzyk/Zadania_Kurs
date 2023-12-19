import sys
import json
import csv

class Files:
    def __init__(self, input_file, output_file, variables):
        self.input_file = input_file
        self.output_file = output_file
        self.variables = variables

    def read_file(self):
        raise NotImplementedError("Subclasses must implement the read_file method")

    def apply_changes(self):
        raise NotImplementedError("Subclasses must implement the apply_changes method")

    def save_file(self):
        raise NotImplementedError("Subclasses must implement the write_file method")


# operation_list = []


class CsvFile(Files):
    def read_file(self):
        with open(self.input_file, mode='r+') as file_stream:
            input_date = csv.reader(file_stream)
            # input_date = input_date.split("\n")
            self.data = [row for row in input_date]

    def apply_changes(self):
        for element in self.variables:
            try:
                row, column, value = element.split(",")
                row, column = int(row), int(column)
                # operation_list.append(element)
                self.data[row][column] = value
            except ValueError:
                print(f"Error: wrong row ({row}) or column ({column}). Only numbers. ")
                sys.exit(1)

            # row, column, value = operation.split(",")
            # row = int(row)
            # column = int(column)
            # operation_list[row][column] = value

    def save_file(self):
        with open(self.output_file, mode="w") as file_stream:
            writer = csv.writer(file_stream)
            writer.writerows(self.data)
            # output_file = file_stream.write(f"{input_date} \n")
            # for line in operation_list:
                # file_stream.write(",".join(line) + "\n")
                # print(",".join(line))


# python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0


class JsonFile(Files):
    def read_file(self):
        with open(self.input_file, mode='r+') as file_stream:
            self.data = json.load(file_stream)
            # input_date = json.load(file_stream)
            # input_date = input_date.split("\n")
            # for element in input_date:
                # element = element.split(",")
                # operation_list.append(element)

    def apply_changes(self):
        for element in self.variables:
            try:
                row, column, value = element.split(",")
                row, column = int(row), int(column)
                self.data[row][column] = value
            except ValueError:
                print(f"Error: wrong row ({row}) or column ({column}). Only numbers. ")
                sys.exit(1)

    def save_file(self):
        with open(self.output_file, mode='w') as file_stream:
            json.dump(self.data, file_stream)


class TxtFile(Files):
    def read_file(self):
        with open(self.input_file, mode='r+') as file_stream:
            self.data = [line.rstrip('\n') for line in file_stream]

            # input_date = file_stream.read()
            # input_date = input_date.split("\n")
            # for element in input_date:
                # element = element.split(",")
                # operation_list.append(element)

    def apply_changes(self):
        for element in self.variables:
            try:
                row, column, value = element.split(",")
                row, column = int(row), int(column)
                line = self.data[column]
                line = line[:row] + value + line[row + len(value):]
                self.data[column] = line
            except ValueError:
                print(f"Error: wrong row ({row}) or column ({column}). Only numbers. ")
                sys.exit(1)

    # with open('output.csv', mode="w") as file_stream:
        # output_file = file_stream.write(f"{input_date} \n")
        # for line in operation_list:
            # file_stream.write(",".join(line) + "\n")
            # print(",".join(line))

    def save_file(self):
        with open(self.output_file, mode='w') as file_stream:
            file_stream.write('\n'.join(self.data))

if __name__ == "__main__":
    input_file, output_file, variables = sys.argv[1], sys.argv[2], sys.argv[3:]

    file_extension = input_file.split('.')[-1]

    if file_extension == 'csv':
        modifier = CsvFile(input_file, output_file, variables)
    elif file_extension == 'json':
        modifier = JsonFile(input_file, output_file, variables)
    elif file_extension == 'txt':
        modifier = TxtFile(input_file, output_file, variables)
    else:
        print("Unsupported file format.")
        sys.exit(1)

    modifier.read_file()
    modifier.apply_changes()
    modifier.save_file()
