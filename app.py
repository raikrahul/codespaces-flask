from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Flask Wikipedia Viewer")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    if query:
        api_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={query}"
        response = requests.get(api_url)
        data = response.json()
        search_results = data.get("query", {}).get("search", [])
        return render_template("search_results.html", query=query, results=search_results)
    return "No search query provided."



@app.route("/random_article")
def random_article():
    api_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnlimit=1"
    response = requests.get(api_url)
    data = response.json()
    random_article = data["query"]["random"][0]
    return render_template("random_article.html", title=random_article['title'], url=f"https://en.wikipedia.org/wiki/{random_article['title']}")











if __name__ == "__main__":
    app.run(debug=True)
