def root(title, body):
    # read a file into a string variable
    body_html = open('body.html', 'r').read()
    # replace {title} and {body} from html
    return body_html.format(title=title, body=body) 

form_name = "fname"
def form(form_name):
    form_html = open('form.html', 'r').read() 
    return form_html.format(fname=form_name)

def canvas(canvas_name):
    canvas_html = open('canvas.html', 'r').read()
    return canvas_html.format(canvas_name=canvas_name)