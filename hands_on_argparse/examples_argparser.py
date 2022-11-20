'''
-----Examples of argparse-----

main source: https://docs.python.org/fr/3/howto/argparse.html
to go further: https://docs.python.org/fr/3/library/argparse.html#module-argparse
'''
# remark : you shall delete the comments once you have understood.

run_example = 1

if run_example == 0:
    # import the package
    import argparse
    # create an instance of ArgumentParser that will grab the arguments
    # following the file in command line
    # description argument will be displayed when "python3 examples_argparser.py -h" is called
    parser = argparse.ArgumentParser(
        description="example 0 of argparse (change run_example variable to change the example)")
    # add a first argument to grab.
    # it is a positional argument expected in the command line each time we call the script.
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    # add a second argument to grab.
    # it is an optional argument that can be set or not.
    # an other version, action = "store_true" would set verbosity to True
    # whenever it is called and False by default.
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="increase output verbosity")
    # put the arguments "verbosity" and "square" in the namespace
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity >= 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity >= 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)


elif run_example == 1:
    import argparse
    parser = argparse.ArgumentParser(
        description="example 1 of argparse (change run_example variable to change the example)")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    answer = args.x**args.y
    if args.verbosity >= 2:
        print(f"Running '{__file__}'")
    if args.verbosity >= 1:
        print(f"{args.x}^{args.y} == ", end="")
    print(answer)

else:
    import argparse

    parser = argparse.ArgumentParser(
        description="example 2 of argparse (change run_example variable to change the example)")
    # this line impede -v and -q from being used together
    # it adds the information that they are exclusive [-v | -q] when -h is typed.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x**args.y

    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.x} to the power {args.y} equals {answer}")
    else:
        print(f"{args.x}^{args.y} == {answer}")
