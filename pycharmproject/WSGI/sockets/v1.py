import socketserver

#
# class Handler(socketserver.BaseRequestHandler):
#
#     def handle(self) -> None:
#         super().handle()
#
#         r = self.request
#         data = r.recv(1024)
#         print(data)
#
# server = socketserver.ThreadingTCPServer(("127.0.0.1",9999),Handler)
#
# server.serve_forever()

from io import StringIO

s = StringIO()



from wsgiref.simple_server import make_server,demo_app



ws = make_server("127.0.0.1",9999,demo_app)
ws.serve_forever()

