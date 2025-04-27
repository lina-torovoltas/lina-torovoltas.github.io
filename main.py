import random
from flask import Flask, render_template, send_file, Response

app = Flask(__name__)

def render_page(template_name: str):
    try:
        body = render_template(template_name)
    except Exception:
        body = render_template("404.html")
        return render_template("pattern.html", body=body), 404
    return render_template("pattern.html", body=body)

def get_random_quote():
    try:
        with open("templates/quotes.txt", "r", encoding="utf-8") as f:
            quotes = f.read().strip().split("\n%\n")
        return random.choice(quotes).strip() if quotes else ""
    except FileNotFoundError:
        return "# :("

@app.route("/")
def index():
    return render_page("pages/index.html")

@app.route("/<page>")
def pg(page):
    if page == "sitemap.xml":
        return send_file('templates/sitemap.xml', mimetype='application/xml')
    
    if page == "robots.txt":
        try:
            with open("templates/robots.txt", "r", encoding="utf-8") as f:
                robots_content = f.read().strip()
        except FileNotFoundError:
            robots_content = "User-agent: *\nDisallow: /"

        quote = get_random_quote()
        response_text = f"{quote}\n\n{robots_content}"
        return Response(response_text, mimetype="text/plain")
    
    return render_page(f"pages/{page}.html")

if __name__ == '__main__':
    app.run()