
import csv
import sys

class Data:

    def __init__( self, filename = None ):

        #fields
        self.data = []

        #read in a file if provided
        if ( filename != None ):
            self.file = filename
            self.readData()

    #reads the data from a file
    def readData( self ):

        #read the file lines
        fp = file( self.file, "rU" )
        lines = fp.readlines()
        fp.close()

        #create a csv object
        csvr = csv.reader( lines )

        # loop through the rest of csvr and append each list to raw_data
        for thing in csvr:
            self.data.append( thing )



    # returns the number of raw columns
    def get_num_columns( self ):

        return len( self.data[0] )

    # returns the number of rows
    def get_num_rows( self ):

        return len( self.data )

    # returns a row of raw data with the specified row number
    def get_row( self, rowNum ):

        return self.data[ rowNum ]


    # returns the raw data at the given header, with the given row number
    def get_value( self, rowNum, colNum ):

        return self.data[ rowNum ][ colNum ]

    # sets the value at the given header, with the given row number
    def set_value( self, rowNum, colNum, value ):

        self.data[ rowNum ][ colNum] = value


    def save( self, filename = None ):
        if filename == None:
            filename = self.file

        with open(filename, 'wb') as csvfile:
            writer = csv.writer(csvfile, dialect = 'excel')
            for row in self.data:
                writer.writerow( row )


