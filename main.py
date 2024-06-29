from wsgiref.simple_server import make_server

html="""
<!DOCTYPE HTML>
<html>
    <head>
        <title>Servidor python</title>
    </head>
    <body>
        <h2> Hola mi nombre es calo</h2>
    </body>
</html>
"""

def aplication(env, start_response):
    headers = [('Content-Type','text/html')]
    
    start_response('200 OK', headers)
    
    return [bytes(html,'utf-8')]

server = make_server('localhost',3000,aplication)
server.serve_forever()