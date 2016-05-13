import cherrypy


class RestServer(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def get(self):
        return cherrypy.session['mystring']

    def put(self, another_string):
        cherrypy.session['mystring'] = another_string

if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.config.update("server.conf")

    cherrypy.quickstart(RestServer(), '/', conf)
