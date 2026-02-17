from collections import Counter 

def count_with_dict_comprehension(my_list):
    frequency_dict = {item : my_list.count(item) for item in set(my_list)}
    return frequency_dict

def count_with_manoual_loop(my_list):
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict.keys():
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1 
        
    print(frequency_dict)    

def count_with_get_method(my_list):
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    print(frequency_dict)

def counter_with_counter(my_list):
    frequency_dict = Counter(my_list)   
    sorted_freq_dict = frequency_dict.most_common()
    #sorted_freq_dict = dict(frequency_dict.most_common()) # If we want to have dictionary like the others
    print(sorted_freq_dict) 

def main():
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]

    print(count_with_dict_comprehension(my_list))
    count_with_manoual_loop(my_list)
    count_with_get_method(my_list)
    counter_with_counter(my_list)


if __name__ == "__main__":
    main()         