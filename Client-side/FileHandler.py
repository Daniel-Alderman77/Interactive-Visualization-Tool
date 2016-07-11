from lxml import etree


class ReadData:

    def __init__(self):
        self.name = self

    def parse_memory_data(self, filename):
        total_memory = None
        task1 = None
        task2 = None

        root = etree.parse(filename)

        log_node = root.find('.//LOG-NODE')
        log_node_contents = log_node.getchildren()
        for content in log_node_contents:
            if content.get('Name') == 'Memory':
                total_memory = content.get('Value')

        print("Total Memory: %s" % total_memory)

        actions = root.findall('.//LOG-ACTION')

        log_action_contents = actions[0].getchildren()
        for content in log_action_contents:
            if content.get('Name') == 'Memory_Allocated':
                task1 = content.get('Value')

        print("Task 1 Memory: %s" % task1)

        log_action_contents = actions[1].getchildren()
        for content in log_action_contents:
            if content.get('Name') == 'Memory_Allocated':
                task2 = content.get('Value')

        print("Task 2 Memory: %s" % task2)

        return [total_memory, task1, task2]
