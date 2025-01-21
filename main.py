from fasthtml.common import *

app,rt = fast_app(live=True)

@rt('/')
def get(): return Titled("Hello World")
 
