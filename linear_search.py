def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print(x)
            return x
    print("target is not on the list")
    return -1


linear_search([8, 5, 2, 9, 0, 1], 6)
