from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to Flask!"
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"
@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        return {"message": "Data received", "data": data}
    return {"message": "Send a POST request with JSON data"}
@app.route('/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return {"message": f"Item {item_id} updated"}
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return {"message": f"Item {item_id} deleted"}
from flask import render_template
@app.route('/welcome/<name>')
def welcome(name):
    return render_template('index.html', name=name)
from flask import Flask, render_template, request
from form import NameForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template('form.html', form=form)
from blueprints.sample import sample_bp
app.register_blueprint(sample_bp, url_prefix='/bp')
@app.errorhandler(404)
def not_found(error):
    return "Page Not Found", 404
@app.errorhandler(500)
def internal_error(error):
    return "Internal Server Error", 500
if __name__ == '__main__':
    app.run(debug=True)