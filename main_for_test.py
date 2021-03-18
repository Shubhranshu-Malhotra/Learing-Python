def add_five(num):
    try:
        if num or num==0: # need to add num==0 else 0 will be considered as False
            return num+5
        else:
            return 'Please enter a number.'
    except (TypeError, ValueError) as err:
        # print(f'Oops!! {err}')
        return err

    

# print(add_five('str'))
