import analyze
import results
from gooey import Gooey, GooeyParser

@Gooey
def __main__():
    
    # Creates GOOEY interface
    parser = GooeyParser(description="Analyze Chrome River Data")
   # parser.add_argument('Directory', help="Select Folder to Process", widget='DirChooser') 
    parser.add_argument('rawdata', help='File to Process', widget='FileChooser')
    parser.add_argument('outputDir', help='Select Output Directory', widget='DirChooser')
    parser.add_argument('outputFile', help="Output File Name", widget='Textarea')
    parser.add_argument('RRC', help='RRC', widget='Textarea', default='all')
    # parser.add_argument('username', help="Username", widget='CommandField')
    # parser.add_argument('password', help="***********", widget='PasswordField')



    args = parser.parse_args()

    # if len(sys.argv) > 1:
    #     print('if block')
    #     RRC = sys.argv[0]
    #     efsDf = efsERs.ERLookUp(args.username, args.password, RRC)
    #     expenseLines = analyze.expenseLines(args.rawdata, RRC)
        

    
       
    
    analyze.expenseLines(args.rawdata, args.outputDir, args.outputFile, args.RRC)
        
      

    

__main__()