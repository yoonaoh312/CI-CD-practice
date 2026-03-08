from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!doctype html>
<html>
<head><title>Welcome to my docker container</title></head>
<body>
<h2>What is your name?</h2>
<form method="POST">
    <input type="text" name="username" placeholder="Enter your name" required>
    <button type="submit">Submit</button>
</form>
{% if name %}
    <p>Hello! Nice to meet you {{ name }}! Welcome to my Docker container!</p>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def greet():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(html_template, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)