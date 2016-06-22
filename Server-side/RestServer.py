import glob

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, static_url_path='')
api = Api(app)


class Hello(Resource):
    def get(self):
        file_count = (len(glob.glob1("static", "*.xml")))

        list_of_files = []
        if file_count > 0:
            list_of_files = glob.glob1("static", "*.xml")

        return {'Number of files': file_count,
                'List of files': list_of_files}

api.add_resource(Hello, '/file_count/')


@app.route('/data/<path:path>')
def get_data(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
