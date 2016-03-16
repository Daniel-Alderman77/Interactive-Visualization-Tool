class ReadData:

    def __init__(self):
        self.name = self

    def ReadData(self, filename):

        data = []

        dataFile = open(filename, 'r')

        for char in dataFile:
            data.append(char)

        print("Number of values in the file:" , len(data))

        dataFile.close()