from functools import wraps

from typing import Any, Optional, Callable


def log(filename: Optional[str] = None) -> Callable:

    '''Автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки'''
    
    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding = "utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding = "utf-8") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
        return wrapper
    return my_decorator


@log()
def my_function(x: int, y: int) -> int:
    '''складывает два значения'''
    return x + y


#print(my_function(1, "2"))
