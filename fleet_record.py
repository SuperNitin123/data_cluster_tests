# Evaluating pandas data Frame & series statistics

import pandas as pd

fleet_data = {
    "brands": ['Suzuki', 'Toyota', 'Ford', 'Honda', 'Hyundai'],
    'numbers': [4, 7, 2, 4, 5]
}
fleet_record = pd.DataFrame(fleet_data)

# Displaying fleet details
print(fleet_record)

# demonstrating series
employees = ['Nitin','Amir','Sunil']

employee_details = pd.Series(employees,index=['a','b','c'])
print(employee_details)