import falcon
import random

class RandomAPI:
    def on_get(self, req, resp):
        rand_num = random.randint(1, 100)
        body = {
            'number': rand_num,
        }

        resp.status = falcon.HTTP_200
        resp.body = body

api = falcon.API()
api.add_route('/randint', RandomAPI())

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8000, api)
    httpd.serve_forever()