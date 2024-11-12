from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle the form submission
        employee_number = request.form.get('employee_number')
        choices = request.form.get('choices')

        # Append to the bids_table.csv file
        with open('data/bids_table.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([employee_number] + choices.split(','))

        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
