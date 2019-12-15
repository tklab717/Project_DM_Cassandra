import os
import glob
import csv

def get_file_path_list(filepath):
    """
    This function provides the list of file path in provided directory.
    
    Args:
        filepath:the place which has csv data for reading
    Return:
        file_path_list: all data in the directory provided
    """
    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root,'*'))
    
    return file_path_list

def get_full_data(file_path_list):
    """
    This function provides full data in the directory that implied by file_path_list.
    Args:
        file_path_list: the list of the file path which include all files for reading
    Return:
        full_data_rows_list: All data that are used for creating new data file.
    """
    full_data_rows_list =[]
    for f in file_path_list:
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
            for line in csvreader:
                full_data_rows_list.append(line)

    return full_data_rows_list

def create_new_file(full_data_rows_list, create_file_name):
    """
    This function creates new files by using all data in the full_data_rows_list.
    Args:
        full_data_rows_list: all data that are used for creating one file.
    Return:
        None
    """
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
    with open(create_file_name, 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect = 'myDialect')
        writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length',\
                        'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

def check(create_file_name):
    """
    This function provides checking the number of data that the created file include.
    Args:
        create_file_name:file name for checking
    Return:
        None
    """
    with open(create_file_name, 'r', encoding = 'utf8') as f:
        print("dataNum" + ":" + str(sum(1 for line in f)))
    
    
def main():
    """
    This is main function.
    
    Args:
        None
    Returns:
        None
    """
    
    filepath = os.getcwd() + '/event_data'
    create_file_name = 'event_datafile_new.csv'
    
    file_path_list = get_file_path_list(filepath)
    full_data_rows_list = get_full_data(file_path_list)
    create_new_file(full_data_rows_list, create_file_name)
    check(create_file_name)
    
if __name__ == "__main__":
    main()