# def new_decorator(fn):

#     def wrap_func():
#         print("This is start of function")

#         fn()

#         print("This is end of function")

#     return wrap_func

# @new_decorator
# def middle_fn():
#     print("This is middle of")


# middle_fn()
_MASKING = "*"

def run_with_stringy(fn):

    def wrapper(obj):
        if (isinstance(obj,str)):
            return fn(obj)
        elif isinstance(obj,dict):
            return {key: wrapper(value) for key,value in obj.items()}
        elif isinstance(obj,(tuple,list,set)):
            sequence_kls = type(obj)
            return sequence_kls(wrapper(value) for value in obj)
    return wrapper

@run_with_stringy
def hide_data(content):
    start_point = len(content) //2 
    num_of_asterisks = len(content) // 2 + len(content) % 2
    return content[:start_point] + _MASKING * num_of_asterisks

def main():
    sample_list = [
        {"username": "johndoe", "country": "USA"},  # User information
        ["123-456-7890", "123-456-7891"],  # Social security numbers
        [("johndoe", "janedoe"), ("bobdoe", "marydoe")],  # Couple names
        "secretLaunchCode123",  # Secret launch code
    ]
    source_data = hide_data(sample_list)
    print(source_data)
if __name__ == "__main__":
    main()