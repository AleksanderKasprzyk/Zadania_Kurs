import sys

try:
    input_file, output_file, variables = sys.argv[1], sys.argv[2], sys.argv[3:]
except:
    print("Error wrong values. ")
    exit()

operation_list = []
with open('input.csv', mode='r+') as file_stream:

    input_date = file_stream.read()
    input_date = input_date.split("\n")
    for element in input_date:
        element = element.split(",")
        operation_list.append(element)

for operation in variables:

    try:
        row, column, value = operation.split(",")
        row = int(row)
        column = int(column)
        operation_list[row][column] = value
    except ValueError:
        print(f"Error: wrong row ({row}) or column ({column}). Only numbers. ")
        sys.exit(1)

with open('output.csv', mode="w") as file_stream:
    #output_file = file_stream.write(f"{input_date} \n")
    for line in operation_list:
        file_stream.write(",".join(line) + "\n")
        print(",".join(line))

#python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
