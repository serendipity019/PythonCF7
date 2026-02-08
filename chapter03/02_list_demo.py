def print_id(variable_name, variable):
    print(f"id({variable_name}) = {id(variable)}")

def main():
    original_list =[1, 2]
    new_list = original_list

    print_id("original_list", original_list)
    print_id("new_list", new_list)

    print("-" * 20)
    new_list[0] = 100
    print_id("original_list", original_list)
    print_id("new_list", new_list)

    print(original_list)
    print(new_list)

    print("-" * 20)
    temp_list = [100, 2]
    print_id("temp_list", temp_list)

    print_id("original list item 0", original_list[0])
    print_id("temporary list item 0", temp_list[0])

if __name__ == "__main__":
    main()