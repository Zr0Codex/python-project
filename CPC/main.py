import glob
import datetime
import csv

# Path env for Prod and Staging
path_import_data = "/home/tontrakan/app/project/python-project/CPC/data_import/"
path_export_data = "/home/tontrakan/app/project/python-project/CPC/data_export/"

# Path env for Dev
# path_import_data = "./data_import/"
# path_export_data = "./data_export/"
print('ton')

def processingfiles():
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    today = datetime.datetime.today().strftime('%Y%m%d')
    fileNameToday = path_import_data + 'Banner_csv_' + today
    dictionary = []
    #print("file name today: "+fileNameToday)
    #print('importing data from: '+fileNameToday)
    try:
        for files in glob.glob(path_import_data + "*.csv"):
            filnameExtendes = files[:-11]
            #print("file name extended" + filnameExtendes)
            #print("files:"+ files)
            if (filnameExtendes == fileNameToday):
                print('importing data from: '+files)
                with open(files, 'r') as csvfile:
                    msgreader = csv.reader(csvfile)
                    for row in msgreader:
                        row[2] = str(row[2]).replace(',', ';')
                        if "##" in row[0]:
                            row[0] = str(row[0]).replace(
                                '"## RECSentity.id"', 'RECSentity.id')
                        if '0' not in row:
                            dictionary.append(row)
                filename = path_export_data + files[58:]
                #print(filename)
                with open(filename, "wt") as writerE:
                    print('exporting data to: '+filename)
                    wrtier = csv.writer(
                        writerE, delimiter=',', quotechar="'")
                    wrtier.writerows(dictionary)
                    writerE.close()
                filenameEnd = path_export_data + files[58:-4] + '.end'
                filenamewriter = open(filenameEnd, "w")
                filenamewriter.write('end')
                filenamewriter.close
            # else:
            #     print('could not found' + fileNameToday)
    except Exception as e:
        print(e)
        pass


processingfiles()
