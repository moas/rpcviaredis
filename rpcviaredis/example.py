from urllib import request

from rpcviaredis.models import Response
from rpcviaredis.server import ServerRPC
from rpcviaredis.transport import *


class DummyServer(ServerRPC):

    def sum(self, x, y):
        return Response(response=x+y, exception=None, reason=None, return_code=200)

    def naive_div(self, x, y):
        return Response(response=x/y, exception=None, reason=None, return_code=200)

    def multiplication(self, x, y):
        return Response(response=x*y, exception=None, reason=None, return_code=200)


if __name__ == "__main__":
    import redis

    r = redis.StrictRedis(db=2)
    s = DummyServer(r, 'test-rpc', transport_klass=JSONTransport)
    try:
        s.start()
    except KeyboardInterrupt:
        pass
    finally:
        s.stop()
