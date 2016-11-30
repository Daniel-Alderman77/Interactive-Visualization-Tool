import glob
import cPickle
import os
import requests
from requests.exceptions import ReadTimeout, ConnectionError, HTTPError
import sys

from RESTClient import RESTClient
from FaultDetection import FaultDetection

host_url = None

# Store command line argument as host_url
if sys.argv > 1:
    try:
        host_url = sys.argv[1]
    except:
        host_url = 'http://127.0.0.1:5000/'

        pass
else:
    print "No command line arguments entered"


class WebServiceClient:

    def __init__(self):
        self.name = self
        self.ping = ""

    @staticmethod
    def get_local_file_count():
        file_count = (len(glob.glob1("data_store", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("data_store", "*.xml")

        return {'Number of files': file_count,
                'List of files': list_of_files}

    @staticmethod
    def get_remote_file_count(index):
        rest_client = RESTClient()

        try:
            if rest_client.read_datafile(index):
                print "Connection is successful"

                number_of_remote_files = rest_client.get_number_of_files()

                return number_of_remote_files

        except Exception as e:
            print(e)
            print "Server is unavailable"
            pass

    def check_transfer(self, index):
        try:
            number_of_files = self.get_local_file_count()["Number of files"]

            print("Number of local files: %s" % number_of_files)

            if index == (number_of_files - 1):
                print "File has been transferred"

                return True
            else:
                print "File has not been transferred"

                return False

        except Exception as e:
            print(e)
            print "File cannot be transferred"
            pass

    def calculate_ping(self):
        fault_detection = FaultDetection()

        pickle_name = 'visualizer_cache/latency_data.p'

        directory = 'visualizer_cache'

        try:
            session = requests.Session()

            request = session.get(host_url)

            self.ping = request.elapsed

            print 'Ping = ', self.ping

            # Check with pickle exists
            if os.path.isfile(pickle_name):
                # If the pickle exists delete ut
                os.remove(pickle_name)

                # And create new pickle file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(self.ping, pickle)

            else:
                # If visualizer_cache doesnt't exist create it
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Pickle data to a new file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(self.ping, pickle)

        except HTTPError as error:
            print error
            fault_detection.http_error(error)

        except ReadTimeout:
            print "Connection has timed out"
            fault_detection.late_timing_fault()

            self.ping = "ReadTimeout"

            # Check with pickle exists
            if os.path.isfile(pickle_name):
                # If the pickle exists delete ut
                os.remove(pickle_name)

                # And create new pickle file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(self.ping, pickle)

            else:
                # If visualizer_cache doesnt't exist create it
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Pickle data to a new file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(self.ping, pickle)

        except ConnectionError:
            print "Failed to establish connection to Server"
            fault_detection.connection_error()

            self.ping = "ConnectionError"

            # Check with pickle exists
            if os.path.isfile(pickle_name):
                # If the pickle exists delete ut
                os.remove(pickle_name)

                # And create new pickle file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(self.ping, pickle)

            else:
                # If visualizer_cache doesnt't exist create it
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Pickle data to a new file
                with open(pickle_name, 'wb') as pickle:
                    cPickle.dump(self.ping, pickle)
