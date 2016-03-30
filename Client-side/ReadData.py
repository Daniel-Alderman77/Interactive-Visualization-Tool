from lxml import etree

class ReadData:

    def __init__(self):
        self.name = self

    def ParseXML(self, filename):
        totalMemory = None
        task1 = None
        task2 = None

        root = etree.parse(filename)

        logNode = root.find('.//LOG-NODE')
        logNodeContents = logNode.getchildren()
        for content in logNodeContents:
            if content.get('Name') == 'Memory':
                totalMemory = content.get('Value')

        print("Total Memory: %s" % totalMemory)

        actions = root.findall('.//LOG-ACTION')

        logActionContents = actions[0].getchildren()
        for content in logActionContents:
            if content.get('Name') == 'Memory_Allocated':
                task1 = content.get('Value')

        print("Task 1 Memory: %s" %task1)

        logActionContents = actions[1].getchildren()
        for content in logActionContents:
            if content.get('Name') == 'Memory_Allocated':
                task2 = content.get('Value')

        print("Task 2 Memory: %s" %task2)

        return [totalMemory, task1, task2]