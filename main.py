"""
Flask Web Application.

This module sets up a basic Flask web application with routes
to render index and menu pages, and a redirect route.
"""

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Menu items data
menu_items = [
    {
        "name": "Маргарита",
        "description": "Традиційна піца з томатним соусом і сиром",
        "price": 10.99
    },
    {
        "name": "Пепероні",
        "description": "Піца з пепероні та сиром",
        "price": 12.99
    },
]


@app.route('/')
@app.route('/index')
def index():
    """Render the index page."""
    return render_template('index.html')


@app.route('/menu')
def menu():
    """Render the menu page with the list of menu items."""
    return render_template('menu.html', menu_items=menu_items)


@app.route('/redirect_menu')
def redirect_menu():
    """Redirect to the menu page."""
    return redirect(url_for('menu'))


if __name__ == '__main__':
    # Start the Flask app in debug mode
    app.run(debug=True)
