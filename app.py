# app.py
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Load the seniority data for reference (assuming it’s available locally)
SENIORITY_DATA_PATH = "data/seniority_table.csv"
BIDS_TABLE_PATH = "data/bids_table.csv"

def get_seniority_numbers():
    """ Load seniority numbers from the seniority table """
    seniority_numbers = {}
    with open(SENIORITY_DATA_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            seniority_numbers[row['employee_number']] = row['seniority_number']
    return seniority_numbers

@app.route('/', methods=['GET', 'POST'])
def submit_bid():
    seniority_numbers = get_seniority_numbers()
    if request.method == 'POST':
        # Get form data
        employee_number = request.form['employee_number']
        choices = request.form.getlist('choices')  # Get all choices as a list

        # Determine seniority
        seniority_number = seniority_numbers.get(employee_number)
        if seniority_number is None:
            return "Employee number not found. Please check and try again."

        # Append data to bids_table.csv
        with open(BIDS_TABLE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write employee number, seniority, and choices in sequence
            row = [employee_number, seniority_number] + choices
            writer.writerow(row)

        # Redirect to success page or display message
        return redirect(url_for('success'))
    
    return render_template('form.html')

@app.route('/success')
def success():
    return "Thank you! Your bid choices have been successfully submitted."

if __name__ == '__main__':
    app.run(debug=True)
