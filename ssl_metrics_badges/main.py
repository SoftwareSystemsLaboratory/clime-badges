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

    return parser.parse_args()
