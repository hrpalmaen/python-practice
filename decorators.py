from datetime import datetime

def upper_text(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        execute_function = func(*args, **kwargs).upper()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
        return execute_function
    return wrapper

@upper_text
def message(name):
    return f'{name}, recibiste un mensaje'

print(message('Gohan'))