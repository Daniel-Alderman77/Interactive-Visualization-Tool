from xml.dom import minidom

class ReadData:

    def __init__(self):
        self.name = self

    def ParseXML(self, filename):
        xmldoc = minidom.parse(filename)
        itemlist = xmldoc.getElementsByTagName('Property')

        totalMemory = itemlist[3].attributes['Value'].value
        print("Total Memory: %s" %totalMemory)

        task1 = itemlist[12].attributes['Value'].value
        print("Task 1 Memory: %s" %task1)

        task2 = itemlist[22].attributes['Value'].value
        print("Task 2 Memory: %s" %task2)

        return [totalMemory, task1, task2]