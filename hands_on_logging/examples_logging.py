import logging

run_example = 1

if run_example == 1:
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
    logging.debug("message example 1")


elif run_example == 2:
    logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                        format="%(asctime)s-%(levelname)s-%(message)s")
    logging.debug("message example 2")

elif run_example == 3:
    logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                        format="%(asctime)s-%(levelname)s-%(message)s", filemode="w")
    logging.debug("message example 3")
