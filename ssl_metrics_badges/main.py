from argparse import ArgumentParser, Namespace

from pybadges import badge


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics Badges", usage="Generate custom SVG metrics badges"
    )

    parser.add_argument(
        "-l",
        "--left-side",
        required=True,
        type=str,
        help="Text to go on the left side of the badge",
    )
    parser.add_argument(
        "-s",
        "--svg",
        required=True,
        type=str,
        help="The SVG file to be converted into a badge",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=str,
        help="The output filename of the badge. NOTE: Must end in .svg",
    )

    return parser.parse_args()

def main()  ->  None:
    args: Namespace = getArgs()

    if args.output[-4::] != ".svg":
        print("Invalid output file extension. File must end in .svg")
        quit(1)

if __name__ == "__main__":
    main()
