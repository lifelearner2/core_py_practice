import time
"""This program generates the current date and time. 
    The code uses an immutable object - None - so that the time can update each time the function is called"""
def print_current_time(time_value=None):
    if time_value is None:
        time_value = time.ctime()
    print(time_value)

print_current_time()

