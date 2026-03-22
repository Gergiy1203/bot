import asyncio
from pyrogram import Client

api_id = "20368885"
api_hash = "1d499a8be7aad4553d3c2395829292c6"
bot = "8225602323:AAFF0R9Pju3jRaEuWC4n_jyj18VWdb-veZU"

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

        

asyncio.run(main())
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/de/f0/c81e05b613866b76d2d1066490adf1a3dbc4ee9d9c839961c3fc8a6997af/pip-26.0.1-py3-none-any.whl.metadata (Caused by ReadTimeoutError("HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out. (read timeout=15)"))


c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT,
            details TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        details = request.form.get("details")

        if not name or not phone:
            return "Fill required fields"

        conn = sqlite3.connect('orders.db')
        c = conn.cursor()
        c.execute("INSERT INTO orders (name, phone, details) VALUES (?, ?, ?)",
                  (name, phone, details))
        conn.commit()
        conn.close()

        return redirect("/orders")

    return render_template("index.html")


@app.route("/orders")
def orders():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders ORDER BY id DESC")
    data = c.fetchall()
    conn.close()

    return render_template("orders.html", orders=data)


if name == "main":
    init_db()
    app.run(host="0.0.0.0", port=5000)
