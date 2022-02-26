from .app import *
from functools import partial,wraps

def lookup_req_ctx(name=None):
    assert not callable(name),"must be non-callable"
    minimal = ReactApp(name)
    return minimal.get_app()

def setCounter(new):
    global counter
    counter = new

class LocalProxy:
    def __init__(self,parts,opt_type:bool=False) -> None:
        self.parts = parts
        self.opt_type = opt_type
        assert self.opt_type is not None

session = LocalProxy(
    partial(lookup_req_ctx,"session")
)
request = LocalProxy(
    partial(lookup_req_ctx,"request")
)

counter:int = 0