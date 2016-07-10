from FileHandler import ReadData
from RESTClient import RESTClient


class Startup:

    def __init__(self):
        self.name = self

    def __call__(self):

        read_data = ReadData()
        memory_data = read_data.parse_xml('data_store/data.xml')

        rest_client = RESTClient()
        rest_client()

        total_memory = int(memory_data[0])
        print total_memory

startup = Startup()
startup()
