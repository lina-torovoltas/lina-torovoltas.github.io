from flask import Flask, render_template

app = Flask(__name__)

def renderPage(dir: str):
    try:    
        body = render_template(dir)
    except: 
        body = None

    if body: 
        return render_template(f"{dir}")
    else:    
        return render_template("404.html")

@app.route("/")
def index():
    return renderPage("pages/index.html")

@app.route("/<page>")
def pg(page):
    return renderPage(f"pages/{page}.html")

if __name__ == '__main__':
    app.run()