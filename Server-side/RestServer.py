import glob

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, static_url_path='')
api = Api(app)


class Hello(Resource):
    def get(self):
        file_count = (len(glob.glob1("static", "*.xml")))

        return {'Number of files': file_count}

api.add_resource(Hello, '/file_count/')


@app.route('/data/')
def get_data():
    return app.send_static_file('data.xml')

if __name__ == '__main__':
    app.run(debug=True)
