import falcon
import json
import asyncio
from wsgiref import simple_server
from search import wordCount


class Things:
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(req.stream.read())


        resp.body = json.dumps(sarch(data))


def sarch(data):
    urls = data['urls']
    word = data['word']
    output = {}
    output['word'] = word

    urllist = []
    for url in urls:
        object = get_url_object(url, word)
        urllist.append(object)
    output['urls'] = urllist

    return output


def get_url_object(url, word):
    txturl = url['url']
    occurrences = wordCount(txturl, word)
    return {'url': txturl, 'occurrences': occurrences}


app = falcon.API()
app.add_route('/search', Things())

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000

    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s:%s" % (host, port))
    httpd.serve_forever()
