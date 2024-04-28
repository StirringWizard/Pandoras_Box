import csv


# Read data from CSV 
    #opens file at file_path in read mode and stores it in file 
    #creates reader object to read data from CSV file 
    #stores csv data in list 
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file: 
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


# Write data to a CSV file at file_path 
    #opens file at file_path in write mode and stores it in file 
    #creates writer object to write data to CSV 
    #writes new_data to CSV file. each element of new_data is a row
def write_to_csv_file(file_path, new_data):
    with open(file_path, 'w', newline='') as file: 
        writer = csv.writer(file)
        writer.writerow(new_data)
    
# Appends data to a CSV file at file_path
    #This adds new_data to CSV, cant remove any data 
    #opens dile at file_path in append mode and stores it in dfile 
    #creates writer object to write data to CSV 
    #writes new_data to CSV file. each element of new_data is a row
def append_to_csv_file(file_path, new_data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)



# # Example usage:
# file_path = 'test.csv'

# # Reading from the CSV file
# existing_data = read_csv_file(file_path)
# print("Existing data:")
# for row in existing_data:
#     print(row)

# # Writing new data to the CSV file
# new_data = ['eli', 'doge', '0']
# append_to_csv_file(file_path, new_data)
# print("\nNew data written to the file.")

# # Reading from the CSV file again to verify the changes
# updated_data = read_csv_file(file_path)
# print("\nUpdated data:")
# for row in updated_data:
#     print(row)
