import logging

def main():
    log_file = 'cf7.log'

    # This is our file handler
    file_handler = logging.FileHandler(log_file, mode='a')

    # Create a list of handler
    handlers = [file_handler]

    # our logger
    logger = logging.getLogger('search-app')

    # We need to create a basic configuration
    logging.basicConfig(
        handlers= handlers,
        level= logging.INFO, # Logging levels: Debug, Info, Warning, Error, Critical
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    )

    my_nums = list(range(10, 90, 10))

    num_to_find = 2.1

    try:
        index = my_nums.index(num_to_find)
        print('Found')
        print(index)
    except ValueError as e:
        logger.error(f"Error occured: {e}", exc_info=True)

if __name__ == "__main__":
    main() 