from wsgiref.simple_server import make_server

def aplication(env, start_response):
    headers = [('Content-Type','text/plain')]
    
    start_response('200 OK', headers)
    
    return ['Hola desde mi primer servidor en python'.encode('utf-8')]

server = make_server('localhost',3000,aplication)
server.serve_forever()