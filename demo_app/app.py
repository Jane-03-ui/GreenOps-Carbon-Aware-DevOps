from flask import Flask, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            todos.append(task)
        return redirect(url_for("home"))

    html = """
    <html>
    <head>
        <title>GreenOps To-Do App</title>
        <style>
            body {
                font-family: Arial;
                background: #0E1117;
                color: white;
                text-align: center;
                padding: 40px;
            }
            input {
                padding: 10px;
                width: 250px;
                border-radius: 8px;
                border: none;
            }
            button {
                padding: 10px 15px;
                background: #00FFAA;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
            li {
                margin: 10px;
            }
        </style>
    </head>
    <body>
        <h1>🌱 GreenOps Deployed To-Do App</h1>
        <p>Deployed using carbon-aware pipeline</p>

        <form method="POST">
            <input name="task" placeholder="Enter a task" required>
            <button type="submit">Add</button>
        </form>

        <h2>Tasks</h2>
        <ul>
    """

    for task in todos:
        html += f"<li>✅ {task}</li>"

    html += """
        </ul>
    </body>
    </html>
    """

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
