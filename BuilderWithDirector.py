# ============================
# PRODUCT CLASS
# ============================
class HttpRequest:
    def __init__(self):
        self._url = None
        self._method = None
        self._headers = {}
        self._body = None
        self._timeout = 30
        self._retries = 3

    def __str__(self):
        return (
            f"HTTP Request [\n"
            f"  URL     : {self._url}\n"
            f"  Method  : {self._method}\n"
            f"  Headers : {self._headers}\n"
            f"  Body    : {self._body}\n"
            f"  Timeout : {self._timeout}s\n"
            f"  Retries : {self._retries}\n"
            f"]"
        )


# ============================
# BUILDER CLASS
# ============================
class HttpRequestBuilder:
    def __init__(self):
        self._request = HttpRequest()

    def set_url(self, url: str):
        self._request._url = url
        return self

    def set_method(self, method: str):
        self._request._method = method
        return self

    def add_header(self, key: str, value: str):
        self._request._headers[key] = value
        return self

    def set_body(self, body: str):
        self._request._body = body
        return self

    def set_timeout(self, timeout: int):
        self._request._timeout = timeout
        return self

    def set_retries(self, retries: int):
        self._request._retries = retries
        return self

    def build(self):
        if not self._request._url or not self._request._method:
            raise ValueError("URL and Method are mandatory fields!")
        return self._request


# ============================
# DIRECTOR CLASS
# ============================
class HttpRequestDirector:
    """Director class that provides standard/common ways to build HttpRequest"""

    @staticmethod
    def create_simple_get_request(url: str) -> HttpRequest:
        """Creates a basic GET request"""
        return (HttpRequestBuilder()
                .set_url(url)
                .set_method("GET")
                .set_timeout(30)
                .set_retries(3)
                .build())

    @staticmethod
    def create_post_request(url: str, body: str, auth_token: str = None) -> HttpRequest:
        """Creates a POST request with JSON body"""
        builder = (HttpRequestBuilder()
                   .set_url(url)
                   .set_method("POST")
                   .set_body(body)
                   .set_timeout(60)
                   .set_retries(3)
                   .add_header("Content-Type", "application/json"))

        if auth_token:
            builder.add_header("Authorization", f"Bearer {auth_token}")

        return builder.build()

    @staticmethod
    def create_secure_get_request(url: str, auth_token: str) -> HttpRequest:
        """Creates a secure GET request with Authorization"""
        return (HttpRequestBuilder()
                .set_url(url)
                .set_method("GET")
                .add_header("Authorization", f"Bearer {auth_token}")
                .add_header("Accept", "application/json")
                .set_timeout(45)
                .set_retries(5)
                .build())

    @staticmethod
    def create_put_request(url: str, body: str) -> HttpRequest:
        """Creates a PUT request"""
        return (HttpRequestBuilder()
                .set_url(url)
                .set_method("PUT")
                .set_body(body)
                .add_header("Content-Type", "application/json")
                .set_timeout(60)
                .build())


# ============================
# CLIENT USAGE EXAMPLE
# ============================
if __name__ == "__main__":
    print("=== Using Director for Common Requests ===\n")

    # 1. Simple GET Request
    req1 = HttpRequestDirector.create_simple_get_request("https://api.example.com/users")
    print("1. Simple GET Request:")
    print(req1)

    print("\n" + "="*60 + "\n")

    # 2. POST Request with Body
    req2 = HttpRequestDirector.create_post_request(
        url="https://api.example.com/users",
        body='{"name": "Pathak", "city": "Hyderabad"}',
        auth_token="abc123xyz"
    )
    print("2. POST Request:")
    print(req2)

    print("\n" + "="*60 + "\n")

    # 3. Secure GET Request
    req3 = HttpRequestDirector.create_secure_get_request(
        url="https://api.example.com/profile",
        auth_token="secret-token-789"
    )
    print("3. Secure GET Request:")
    print(req3)

    print("\n" + "="*60 + "\n")

    # 4. Direct Builder Usage (for custom requests)
    print("4. Custom Request using Builder directly:")
    custom_req = (HttpRequestBuilder()
                  .set_url("https://api.example.com/upload")
                  .set_method("POST")
                  .add_header("Content-Type", "multipart/form-data")
                  .set_timeout(120)
                  .set_retries(2)
                  .build())
    print(custom_req)