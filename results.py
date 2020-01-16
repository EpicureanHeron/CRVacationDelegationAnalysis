import pandas as pd 
import datetime

def createExcel(dataDict, outputDir, outputFile):
#def createExcel(dataDict):
    
    df = pd.DataFrame(dataDict)

    # df.to_excel('output.xlsx')
    print('creating output document...')
 
    outputFile = outputDir + "\\" + outputFile + '.xlsx'
    print(outputFile)
    writer = pd.ExcelWriter(outputFile, engine='openpyxl')




    for RRC in dataDict:
        print('working on %s' %(RRC))
        # creates an empty data frame
        df = pd.DataFrame(columns=['Date Stamp','EFS ERs', 'CR ERs','CR ER Delegate Created', 'Minnesota', 'Domestic', 'International', 
        'Non-Travel', 'Staff', 'Faculty', 'Student', 'Per Diem and Mileage', 'Travel Card Spend', 'Out of Pocket', 'Unallowable'])

        for monthYearSelection in dataDict[RRC]:
            # if no data exists for the month, skip it
            
                
                # the following lines exist in order to make sure the values exist even if they are zero
            if 'Student' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['Student'] = 0

            if 'Faculty' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['Faculty'] = 0

            if 'Staff' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['Staff'] = 0
            
            if 'International' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['International'] = 0
            
            if 'Domestic' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['Domestic'] = 0

            if 'Non Travel' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['Non Travel'] = 0

            if 'Minnesota' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['Minnesota'] = 0

            if 'delegateCreated' not in dataDict[RRC][monthYearSelection]:
                dataDict[RRC][monthYearSelection]['delegateCreated'] = 0

            # loads the monthyearselection as a datetime object

            dateQueryFormat = datetime.datetime.strptime(monthYearSelection, '%m-%Y')
          
            # creates a string out of the date time object formatted to match the EFS dataframe's dats
            reformattedDate = dateQueryFormat.strftime('%m-%y')
         
            # queries the efs dataframe for the RRC
            # queryRRCERs = df2.query('RRC == "%s"' % RRC)
   
            # # queries the efs dataframe's by rrc by date
            # monthRRCERs = queryRRCERs.query('Date == "%s"' % reformattedDate)
      
            # # if no data, create a zero variable

            # if not monthRRCERs.empty :
            #     efsERs = monthRRCERs['Count'].values[0]
            # else:
            #     efsERs = 0

           
            # data adding to the data frame
            dataToAdd = {'Date Stamp': monthYearSelection,
                'EFS ERs': efsERs,
                'CR ERs': dataDict[RRC][monthYearSelection]['reportCount'],
                'CR ER Delegate Created': dataDict[RRC][monthYearSelection]['delegateCreated'],
                'Minnesota': dataDict[RRC][monthYearSelection]['Minnesota'],
                'Domestic': dataDict[RRC][monthYearSelection]['Domestic'],
                'International': dataDict[RRC][monthYearSelection]['International'],
                'Non-Travel': dataDict[RRC][monthYearSelection]['Non Travel'],
                'Faculty': dataDict[RRC][monthYearSelection]['Faculty'],
                'Staff':  dataDict[RRC][monthYearSelection]['Staff'],
                'Student': dataDict[RRC][monthYearSelection]['Student'],
                'Out of Pocket': dataDict[RRC][monthYearSelection]['OOP'],
                'Per Diem and Mileage': dataDict[RRC][monthYearSelection]['perDiemAndMiles'],
                'Travel Card Spend': dataDict[RRC][monthYearSelection]['travelCardSpend'],
                'Unallowable': dataDict[RRC][monthYearSelection]['Unallowable']}

            

            # https://stackoverflow.com/questions/16597265/appending-to-an-empty-dataframe-in-pandas

            # apparently have to write over the data  frame, can't just call df.append(whatever)
            
            df = df.append(dataToAdd, ignore_index=True)      
            # if no data, create a zero variable

          
        # sorts it by the date
        # df['Date Stamp']=pd.to_datetime(df['Date Stamp'], format = '%m-%Y')
        # df = df.sort_values(by=['Date Stamp'])
        # saves the data frame to the open "writer" and to a specific sheet
        df.to_excel(writer, RRC) 

    writer.save()