from functools import wraps
from typing import Optional, List
import traceback

def data_extractor(data: dict, *args):
    """
        Util function to extract data from a given dict
        Use case:
            Query Param and Body of request contains dict,
            instead of writing
            x = request_body.get('x')
            y = request_body.get('y')
            z = request_body.get('z')

            we can simply write
            x,y,z = data_extractor(request_body, 'x', 'y', 'z')

            DRY and elegant 
    """
    return [data.get(arg) for arg in args]


def standard_response(response_data: dict, has_error_occured=False, error_message=None):
    """
        Util function to prepare the standard response given a payload.
        Useful to frontend for parsing.
    """
    return {
        "payload": response_data,
        "has_error_occured": has_error_occured,
        "error_message": error_message
    }



class GenericRequestException(Exception):
    status_code: Optional[int] = None
    payload: dict = {}



def handle_exceptions(request_method, *exceptions: List[GenericRequestException]):
    # TODO make it more generic
    """
        Util function to handle exceptions that occur within a function
        With this, you just need define all the exceptions once at the beginning of function
        This decorator will catch any exception raised at any level of call stack.
        If it is handled exception, it will raise.
        
        How it works

        Instead of writing all the below code:

        def view(request):
            try:
                do something
            except HandledException as e:
                print(...)

            except HandledException2 as e"
                print(...)
            except Exception as e:
                print(traceback.format_exc())

        
        We can simply write

        @handle_exception(HandledException, HandledException2)
        def view(request):
            do domething

    """
    @wraps(handle_exceptions)
    def handle_exceptions_inner(*args, **kwargs):
        try:
            request_method(*args, **kwargs)
        except Exception as e:
            if type(e) in exceptions:
                return e
            print(traceback.format_exc())
    return handle_exceptions_inner
            