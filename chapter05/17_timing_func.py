import time 

def get_time(num):
    start_time = time.time()
    # some calsulations ...
    result = sum(range(num))
    end_time = time.time()

    print(f"functions took {end_time - start_time} seconds to run!")


def main():
    print(get_time(1_000_000))

if __name__ == "__main__":
    main() 