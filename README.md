# Shift Bid Awards System
## Overview
This project is designed to assign employees to shift bid awards based on their seniority and preferred shift choices. The assignment process considers seniority levels and aims to allocate each employee their most preferred shift, provided it is available based on the choices of more senior employees.

Employees submit their shift preferences through a web form, and the application processes these requests according to seniority, outputting the awarded shifts to a CSV file.

### Features
Allows employees to submit their shift choices online.
Automatically assigns shifts based on seniority order.
Generates a shift_awards.csv file with the awarded shifts and days.
### Project Structure
- **app.py:** Main Flask application file for handling web submissions and processing shifts.
- **templates/index.html:** HTML template for the web form interface.
- **templates/success.html:** HTML template that provides confirmation feedback to employees after they successfully submit their shift choices through the web form.
- **data/:** Folder containing CSV files (bids_table.csv, choices_table.csv, employee_table.csv, seniority_table.csv, shift_awards.csv).
- **shift_assignment.py:** Python script containing the main logic for shift assignment.
- **Getting Seniority Table from Unordered Employee Table.ipynb:** Jupyter notebook for generating seniority_table.csv from the employee_table.csv, calculating seniority based on employee hire dates.
- **README.md:** Project documentation.
### Prerequisites
Python 3.7 or higher
Flask
Pandas
### requirements.txt File
The requirements.txt file lists all necessary dependencies for this project:


Copy code
Flask==2.0.3
Jinja2==3.0.3
pandas==1.3.3
Each package is pinned to a specific version to avoid compatibility issues:

* Flask: Web framework used to handle form submissions.
* Jinja2: Templating engine for rendering HTML in Flask.
* Pandas: For data manipulation and CSV processing.
To install dependencies from this file, run:
```
bash

pip install -r requirements.txt
```
### Setup Instructions
Clone the repository:
```
bash

git clone https://github.com/shum05/shift-bid-awards.git
cd shift-bid-awards
```
Install dependencies:
```
bash

pip install -r requirements.txt
```
Run the application:
```
bash

python app.py
```
Open a browser and go to http://127.0.0.1:5000 to access the form for submitting shift choices. Upon submission, awarded shifts will be saved to data/shift_awards.csv.

### Usage
Employees submit their shift choices using the web form.
The application processes the requests based on seniority.
The resulting shift awards are saved to shift_awards.csv in the data directory.
### Output
The shift_awards.csv file will contain:

first_name: Employee's first name
last_name: Employee's last name
Monday to Sunday: Assigned shifts for each day
### Example Output
### Example Output

| first_name | last_name | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|------------|-----------|--------|---------|-----------|----------|--------|----------|--------|
| John       | Smith     | MO     | MO      | MO        | MO       | MO     | MO       | Off    |
| Jane       | Johnson   | MO     | Off     | Off       | MO       | MO     | MO       | MO     |
| Michael    | Williams  | MO     | MO      | Off       | Off      | MO     | MO       | MO     |

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request.

### Acknowledgments
Thanks to Flask, Jinja2, and pandas for the tools used in this project.