from argparse import ArgumentParser, Namespace

from pybadges import badge


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics Badges", usage="Generate custom SVG metrics badges"
    )

    parser.add_argument(
        "--left-text",
        required=True,
        type=str,
        help="Text to go on the left side of the badge",
    )
    parser.add_argument(
        "--graph",
        required=True,
        type=str,
        help="The graph SVG file to be converted into a badge",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=str,
        help="The output filename of the badge. NOTE: Must end in .svg",
    )

    return parser.parse_args()

def createBadge(leftText: str)   ->  str:
    badge(left_text=leftText, right_text="", left_link="", right_link="", whole_link="", logo="", left_color="", right_color="", measurer="", embed_logo=True, whole_title="", left_title="", right_title="")

def main()  ->  None:
    args: Namespace = getArgs()

    if args.graph[-4::] != ".svg":
        print("Invalid graph file extension. File must end in .svg")
        quit(1)

    if args.output[-4::] != ".svg":
        print("Invalid output file extension. File must end in .svg")
        quit(2)

if __name__ == "__main__":
    main()
