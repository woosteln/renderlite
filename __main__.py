from weasyprint import HTML, CSS
from bottle import request, run, post, get, response
import time
from io import BytesIO


base_css = CSS(string='@page { size: 1024px 480px; margin: 20px } body { background: #FFF; }')
stylesheets = [base_css]

def render_png(html):
    global stylesheets
    now = time.time()
    png = HTML(string=html)\
        .write_png(stylesheets=stylesheets)
    elapsed = time.time() - now
    print(elapsed)
    return png

@post('/css')
def css():
    global stylesheets
    css = request.body.read().decode('UTF-8')
    stylesheets = [base_css,CSS(string=css)]
    return

@post('/render')
def render():
    html = request.body.read().decode('UTF-8')
    png = render_png(html)
    pngBytes = BytesIO(png)
    response.set_header('Content-type','image/png')
    pngBytes.seek(0)
    return pngBytes.read()

run(host='localhost', port=8082)