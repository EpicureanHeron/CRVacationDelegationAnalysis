import pandas as pd
import datetime
import pprint

def expenseLines(fileName, outputDir, outputFile, RRC):

    print('opening workbook...')

    data = pd.read_excel(fileName)

    # if len(args) > 0:
    #     data.rename(columns={'RRC Code': 'RRC'}, inplace = True)
    #     data = data.query('RRC == "%s"' % (args[0]))
    #     data.rename(columns={'RRC': 'RRC Code'}, inplace = True)

    if RRC != 'all':

        filteredByRRC = data.query('RRC == "%s"' % RRC)

    else:

        filteredByRRC = data
    # creats the summary tab

    print('finished analysis...')


    outfile = outputDir + "\\" + outputFile + '.xlsx'

    print(outfile)
        
    writer = pd.ExcelWriter(outfile, engine='openpyxl')

    df = pd.DataFrame(filteredByRRC)

    df.to_excel(writer)

    writer.save()
    

