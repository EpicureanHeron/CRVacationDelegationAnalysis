import pandas as pd
import datetime

def expenseLines(fileName, outputDir, outputFile, RRC):

    print('opening workbook...')

    data = pd.read_excel(fileName)

    ## filters by RRC OR if ALL is left in, grabs everything

    if RRC != 'all':

        filteredByRRC = data.query('RRC == "%s"' % RRC)

    else:

        filteredByRRC = data
    
    ## filters by today's datetime object

    today = datetime.date.today()

    greaterThanToday = filteredByRRC.query('EndDate > "%s"' % today)

    # creats output file


    outfile = outputDir + "\\" + outputFile + '.xlsx'

    print(outfile)
        
    writer = pd.ExcelWriter(outfile, engine='openpyxl')

    df = pd.DataFrame(greaterThanToday)

    df.to_excel(writer)

    writer.save()
    

