def list_sum(some_list):
    if not some_list:
        return 0
    return some_list[0] + list_sum(some_list[1:])
