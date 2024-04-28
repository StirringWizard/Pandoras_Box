import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_to_csv_file(file_path, new_data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)

# Example usage:
file_path = 'test.csv'

# Reading from the CSV file
# existing_data = read_csv_file(file_path)
# print("Existing data:")
# for row in existing_data:
#     print(row)

# Writing new data to the CSV file
new_data = ['John', 'Doe', '30']
write_to_csv_file(file_path, new_data)
print("\nNew data written to the file.")

# Reading from the CSV file again to verify the changes
updated_data = read_csv_file(file_path)
print("\nUpdated data:")
for row in updated_data:
    print(row)
