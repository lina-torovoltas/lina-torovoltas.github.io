import random
from flask import Flask, render_template, send_file, Response

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

def get_random_pattern():
    try:
        with open("templates/pattern.txt", "r", encoding="utf-8") as f:
            content = f.read().strip()
        patterns = content.split("\n%\n")
        return random.choice(patterns).strip() if patterns else ""
    except FileNotFoundError:
        return "# No patterns found :("

@app.route("/")
def index():
    return renderPage("pages/index.html")

@app.route("/<page>")
def pg(page):
    if page == "sitemap.xml":
        return send_file('templates/sitemap.xml', mimetype='application/xml')
    elif page == "robots.txt":
        try:
            with open("templates/robots.txt", "r", encoding="utf-8") as f:
                robots_content = f.read().strip()
        except FileNotFoundError:
            robots_content = "User-agent: *\nDisallow: /"

        pattern = get_random_pattern()
        response_text = f"{pattern}\n\n{robots_content}"
        
        return Response(response_text, mimetype="text/plain")
    else:
        return renderPage(f"pages/{page}.html")

if __name__ == '__main__':
    app.run()
