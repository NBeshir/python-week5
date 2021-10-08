def linear_search_dict(my_dict, target):

    for key in my_dict.keys():
        if my_dict[key] == target:
            print('Found at key', key)
            return key

    print('Target is not in the dictionary')

    return -1


linear_search_dict({"red": 5, "blue": 3, "yellow": 12, "green": 7}, 5)
linear_search_dict({"red": 5, "blue": 3, "yellow": 12, "green": 7}, 3)
linear_search_dict({"red": 5, "blue": 3, "yellow": 12, "green": 7}, 8)
