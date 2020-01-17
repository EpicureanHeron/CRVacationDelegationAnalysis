import analyze
from gooey import Gooey, GooeyParser

@Gooey
def __main__():
    
    # Creates GOOEY interface
    parser = GooeyParser(description="Analyze Chrome River Data")
    parser.add_argument('rawdata', help='File to Process', widget='FileChooser')
    parser.add_argument('outputDir', help='Select Output Directory', widget='DirChooser')
    parser.add_argument('outputFile', help="Output File Name", widget='Textarea')
    parser.add_argument('RRC', help='Enter a single RRC OR leave default value in', widget='Textarea', default='all')

    args = parser.parse_args()

    analyze.expenseLines(args.rawdata, args.outputDir, args.outputFile, args.RRC)
        
      

    

__main__()