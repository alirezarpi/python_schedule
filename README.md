# python_schedule
Call a Function in specific date and time with celery (example)

## Notes
**Note:** Given Date is in Jalali format
**Note:** This is a example so you should NOT use it on your own projects, You know that.
**Note:** You can change functions to do what ever you want in [tasks.py](https://github.com/alirezarpi/python_schedule/blob/master/python_schedule/python_schedule/tasks.py) file.

## Running it

**Before Running it** you should start celery from project directory:

`celery -A python_schedule worker -l info`

And After that:

`python3 manage.py runserver`
