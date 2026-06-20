class HttpRequest:
    def __init__(self):
        self.url = None
        self.method = None
        self.headers = {}
        self.body = None
        self.timeout = 30
        self.retries = 3

    def __repr__(self):
        return f"HttpRequest(url={self.url}, method={self.method}, headers={self.headers}, body={self.body}, timeout={self.timeout}, retries={self.retries})"


class HttpRequestBuilder:
    def __init__(self):
        self.req = HttpRequest()

    def set_url(self, url):
        self.req.url = url
        return self

    def set_method(self, method):
        self.req.method = method
        return self

    def add_header(self, key, value):
        self.req.headers[key] = value
        return self

    def set_body(self, body):
        self.req.body = body
        return self

    def set_timeout(self, timeout):
        self.req.timeout = timeout
        return self

    def build(self):
        if not self.req.url or not self.req.method:
            raise ValueError("method and url are required")
        return self.req


if __name__ == "__main__":
    request = (HttpRequestBuilder()
               .set_url("https://api.example.com/users")
               .set_method("POST")
               .add_header("Content-Type", "application/json")
               .set_body('{"name": "John"}')
               .set_timeout(60)
               .build())
    print(request)
