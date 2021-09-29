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


def createBadge(
    leftText: str = "Hello",
    rightText: str = "World",
    link: str = "https://github.com/SoftwareSystemsLaboratory/",
    logo: str = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAD0lEQVQI12P4zwAD/xkYAA/+Af8iHnLUAAAAAElFTkSuQmCC",
    leftColor: str = "maroon",
    rightColor: str = "gold",
    title: str = "SSL Metrics Badge",
) -> str:
    return badge(
        left_text=leftText,
        right_text=rightText,
        whole_link=link,
        logo=logo,
        left_color=leftColor,
        right_color=rightColor,
        embed_logo=True,
        whole_title=title,
    )


def main() -> None:
    args: Namespace = getArgs()

    if args.graph[-4::] != ".svg":
        print("Invalid graph file extension. File must end in .svg")
        quit(1)

    if args.output[-4::] != ".svg":
        print("Invalid output file extension. File must end in .svg")
        quit(2)

    badge: str = createBadge()
    with open(file=args.output, mode="w") as svg:
        svg.write(badge)
        svg.close()


if __name__ == "__main__":
    main()
