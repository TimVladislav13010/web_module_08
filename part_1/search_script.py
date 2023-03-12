from models import Authors, Quotes


def name(user_name: str) -> str:
    """
    name: Steve Martin — знайти та повернути список всіх цитат автора Steve Martin.
    :param user_name:
    :return:
    """
    authors = Authors.objects()

    for author in authors:

        if author.fullname in user_name:
            quotes = Quotes.objects()

            for quote in quotes:
                if author.id.__str__() in quote.author.id.__str__():
                    return quote.quote


def tag(user_tag: str):
    pass


def tags(user_tags: str):
    pass


def exits(_):
    exit()


def handler_command(user_inp):
    command = {
        "name": name,
        "tag": tag,
        "tags": tags,
        "exit": exits
    }

    result = user_inp.split(": ")

    if result[0] in command.keys():
        result = command[result[0]](" ".join(result[1:]))

    return result


def main():
    while True:
        try:
            user_inp = input(f"Enter command: value...")

            result = handler_command(user_inp)

            print(result)

        except KeyboardInterrupt as er:
            print(er)
            exit()


if __name__ == "__main__":
    main()
