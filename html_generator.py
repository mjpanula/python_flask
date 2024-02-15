def make_body(title, body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>{title}</title>
    </head>
    <body>    
    {body}
    </body>
    </html>
    """

def form():
    return """<form action="/">
  <input type="text" id="fname" name="fname">
  <input type="submit" value="Submit">
</form>
"""