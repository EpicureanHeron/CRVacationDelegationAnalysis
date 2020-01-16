import pandas as pd
import datetime
import pprint

def expenseLines(fileName, outputDir, outputFile):

    print('opening workbook...')

    data = pd.read_excel(fileName)

    # if len(args) > 0:
    #     data.rename(columns={'RRC Code': 'RRC'}, inplace = True)
    #     data = data.query('RRC == "%s"' % (args[0]))
    #     data.rename(columns={'RRC': 'RRC Code'}, inplace = True)

    results = []
    
    dayLimit = 60

    print('Beginning analysis...')

    # creats the summary tab


    for index, row in data.iterrows():
        tripEndOver = False
        transactionOver = False
        #parsed rows
        # header
        transDate = row['Date']
        tripEnd = row['TripEnd']
        date = row['Export Date']
        submitDate = row['Date Submitted']

        # line information 

        travelCard = row['IsFirmPaid (Yes/No)']

        # data pulled on 1/13/2020 had unsubmitted reports with an exported date of 1/1/1900, this excludes any of those


        if date != datetime.datetime(1900, 1, 1):
            # exclude transactions related to travel card
            if travelCard == 'No':

                tripEndDateDiff = submitDate - tripEnd

                transactionDateDiff = submitDate - transDate

                # checks to see if CR ER exceeds the 60 day limit based on the trip end date and submission date
                if tripEndDateDiff > pd.Timedelta(value=dayLimit, unit='d'):

                    tripEndOver = True

                    print('Trip end date: %s, submission date: %s, difference: %s ' % (tripEnd, submitDate, tripEndDateDiff))


                if transactionDateDiff > pd.Timedelta(value=dayLimit, unit='d'):

                    transactionOver = True

                    print('Transaction Date: %s, submission date: %s, difference: %s ' % (transDate, submitDate, transactionDateDiff))


        if tripEndOver or transactionOver == True:
            new_row = row
            new_row["Trip End"] = tripEndOver
            new_row["Transaction Date"] = transactionOver
            # new_row['Trip End Days Over'] = datetime.datetime(tripEndDateDiff
            # new_row['Transaction Days Over'] = datetime(transactionDateDiff)
            # new_row.append(("Trip End", tripEndOver))
            # new_row.append(("Transaction Date", transactionOver))


            results.append(new_row)
    
    print('finished analysis...')


    outfile = outputDir + "\\" + outputFile + '.xlsx'

    print(outfile)
        
    writer = pd.ExcelWriter(outfile, engine='openpyxl')

    df = pd.DataFrame(results)

    df.to_excel(writer)

    writer.save()
    

