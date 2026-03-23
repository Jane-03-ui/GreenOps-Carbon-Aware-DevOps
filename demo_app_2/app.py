from flask import Flask, request, redirect

app = Flask(__name__)

count = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global count

    if request.method == "POST":
        action = request.form.get("action")
        if action == "inc":
            count += 1
        elif action == "dec":
            count -= 1
        return redirect("/")

    return f"""
    <html>
    <head>
        <title>GreenOps Counter App</title>
        <style>
            body {{
                background-color: #0E1117;
                color: white;
                text-align: center;
                font-family: Arial;
            }}
            button {{
                padding: 10px 20px;
                margin: 10px;
                font-size: 18px;
                border-radius: 5px;
                border: none;
                background-color: #00FFAA;
            }}
        </style>
    </head>

    <body>
        <h1>🌱 GreenOps Counter App</h1>
        <h2>Count: {count}</h2>

        <form method="POST">
            <button name="action" value="inc">➕ Increase</button>
            <button name="action" value="dec">➖ Decrease</button>
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
