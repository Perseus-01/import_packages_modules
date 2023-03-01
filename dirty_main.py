from datetime import datetime, date, time

from application.salary import *
from application.db.people import *

def current_date():
    current_datetime = datetime.now().date()
    print(current_datetime)

current_date()

if __name__ == '__main__':
    calculate_salary()
    get_employees()