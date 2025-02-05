from flask import Flask, render_template_string, request, redirect, url_for # type: ignore

app = Flask(__name__)


menu = [
    {'id': 1, 'name': 'Pasta', 'price': 12.99},
    {'id': 2, 'name': 'Pizza', 'price': 9.99},
    {'id': 3, 'name': 'Salad', 'price': 7.99}
]


template = """
<!doctype html>
<html>
<head>
    <title>Hotel Menu</title>
</head>
<body>
    <h1>Hotel Menu</h1>
    <ul>
        {% for item in menu %}
            <li>
                {{ item['name'] }} - ${{ item['price'] }}
                <!-- Add Remove Button -->
                <form method="POST" action="{{ url_for('remove_item', item_id=item['id']) }}" style="display:inline;">
                    <input type="submit" value="Remove">
                </form>
            </li>
        {% endfor %}
    </ul>

    <h2>Add New Item</h2>
    <form method="POST" action="{{ url_for('add_item') }}">
        Name: <input type="text" name="name" required><br>
        Price: <input type="number" step="0.01" name="price" required><br>
        <input type="submit" value="Add Item">
    </form>
</body>
</html>
"""

@app.route('/')
def menu_display():
    return render_template_string(template, menu=menu)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    price = float(request.form['price'])
    new_id = max(item['id'] for item in menu) + 1 if menu else 1
    menu.append({'id': new_id, 'name': name, 'price': price})
    return redirect(url_for('menu_display'))
@app.route('/remove/<int:item_id>', methods=['POST'])
def remove_item(item_id):
    global menu
    menu = [item for item in menu if item['id'] != item_id]  
    return redirect(url_for('menu_display'))

if __name__ == '__main__':
    app.run(debug=True)