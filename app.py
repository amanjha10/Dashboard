from flask import Flask, render_template

app = Flask(__name__)

# # Sample data list
# fire_data_list = [
#     {"address": "Dhapakhel, Lalitpur", "contact": "9822316753"},
#     # Add more data dictionaries as needed
# ]
address="Dhapakhel, Lalitpur"
@app.route('/')
def index():
    return render_template('index.html',address=address)

if __name__ == '__main__':
    app.run(debug=True)
