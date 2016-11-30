import glob
import sys
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, static_url_path='')
api = Api(app)

host_url = None

# Store command line argument as host_url
if sys.argv > 1:
    try:
        host_url = sys.argv[1]
    except:
        pass
else:
    print "No command line arguments entered"


class Server(Resource):
    @staticmethod
    def get():
        file_count = (len(glob.glob1("static", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("static", "*.xml")

        return {'Number of files': file_count,
                'List of files': list_of_files}

api.add_resource(Server, '/file_count/')


@app.route('/data/<path:path>')
def get_data(path):
    return app.send_static_file(path)

# host_url can be specified as a command line argument
# Enabled threading to handle multiple requests
if __name__ == '__main__':
    app.run(host=host_url, threaded=True)
