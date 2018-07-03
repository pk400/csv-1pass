# This script converts the csv file output by the ff-password-exporter tool
# to a csv file that can be imported into 1Password. 1Password currently can
# only import csv files that follow a specific format based on it's type.
# For example, for Login types:
# title,website,username,password,notes,custom field 1,custom field 2
import csv, sys
src_file = sys.argv[1]
dest_file = sys.argv[2]

file_out = open(dest_file, 'w')

with open(src_file, 'rb') as csvfile:
    out = csv.reader(csvfile, delimiter=',')

    # TODO: Add a prompt before writing to file that displays the values in
    # each of the fields. User can make changes to the selected fields within
    # the terminal.

    for row in out:
        title = ''
        if row[0].find('https://') == 1:
            title = row[0].replace('https://', '').replace('.com', '')
        elif row[0].find('http://') == 1:
            title = row[0].replace('htts://', '').replace('.com', '')
        comment = 'Converted from csv-1pass'
        line = title + ',' + row[0] + ',' + row[1] + \
                ',' + row[2] + ',' + comment + ',,\n'
        try:
            file_out.write(line)
        except Exception as e:
            print type(e)
            print str(e)
file_out.close()
