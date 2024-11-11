# shift-bid-awards

## Overview
This project is designed to assign employees to shift bid awards based on their seniority and preferred shift choices. The assignment process takes into account seniority levels and ensures that each employee gets their most preferred shift, provided it is available based on the choices of more senior employees.

## Features
- **Shift Assignment**: Assigns shifts to employees according to their preferences.
- **Seniority-Based Allocation**: Employees are prioritized based on their seniority (employees with lower seniority numbers are assigned first).
- **CSV File Handling**: Takes input from CSV files, processes the assignments, and generates an output CSV file with the assigned shifts for each employee.

## Files
The project consists of the following files:
- **`shift_bid_awards.py`**: The main Python script that processes the shift assignments based on input data.
- **`choices_table.csv`**: Contains the shift preferences for each employee.
- **`bids_table.csv`**: Contains employee shift bids, including their seniority and ranked choices.
- **`seniority_table.csv`**: Lists employees and their corresponding seniority numbers based on hire dates.
- **`employee_table.csv`**: Contains employee details (e.g., employee number, first and last name).
- **`shift_awards.csv`**: The output file generated by the Python script, which contains the assigned shifts for each employee.

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/shum05/shift-bid-awards.git

### Navigate to the project directory:
```
bash

cd shift-bid-awards
```
Make sure you have Python 3.x installed. You can install the required Python dependencies using pip:
```
bash

pip install pandas
```
### Usage
Prepare your input files (choices_table.csv, bids_table.csv, seniority_table.csv, and employee_table.csv) with the appropriate data.

Run the shift_bid_awards.py script:
```
bash

python shift_bid_awards.py
```
The script will process the input files and generate the shift_awards.csv file, which contains the assigned shifts for each employee based on their preferences and seniority.

### Output
The shift_awards.csv file will contain the following columns:

**first_name:** The employee's first name.
**last_name:** The employee's last name.
**Monday:** The shift assigned for Monday.
**Tuesday:** The shift assigned for Tuesday.
**Wednesday:** The shift assigned for Wednesday.
**Thursday:** The shift assigned for Thursday.
**Friday:** The shift assigned for Friday.
**Saturday:** The shift assigned for Saturday.
**Sunday:** The shift assigned for Sunday.

### Example Output
first_name	last_name	Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
John	Smith	MO	MO	MO	MO	MO	MO	Off
Jane	Johnson	MO	Off	Off	MO	MO	MO	MO
Michael	Williams	MO	MO	Off	Off	MO	MO	MO

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request with any improvements or bug fixes.

### Acknowledgments
Thanks to pandas for providing the powerful data manipulation library used to process the shift assignment.
markdown

### Explanation of Sections:
1. **Overview**: Provides a high-level description of the project’s functionality.
2. **Features**: Highlights the key functionalities of the program.
3. **Files**: Lists all files in the repository and briefly explains their purpose.
4. **Installation**: Provides instructions to set up the project on a local machine.
5. **Usage**: Explains how to run the Python script to process the input data and generate the output.
6. **Output**: Describes the structure of the generated `shift_awards.csv` file.
7. **License**: Mentions the project's license (you can update this based on your preference).
8. **Contributing**: Encourages others to contribute to the project.
9. **Acknowledgments**: Credits external tools or libraries used in the project, such as pandas.
