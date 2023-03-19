import timeit

import redis
from redis_lru import RedisLRU

from models import Authors, Quotes


"""
Search script in a cloud database Atlas MongoDB.

start -> in terminal: py search_script.py

reid_lru caching is implemented

commands: 
    name: Steve Martin — знайти та повернути список всіх цитат автора Steve Martin;
    tag:life — знайти та повернути список цитат для тега life;
    tags:life,live — знайти та повернути список цитат, де є теги life або live (примітка: без пробілів між тегами life, live);
    exit — завершити виконання скрипту;
"""


client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
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
    return f"No matches."


@cache
def tag(user_tag: str) -> list | str:
    """
    tag:life — знайти та повернути список цитат для тега life;
    :param user_tag:
    :return:
    """
    result = list()

    quotes = Quotes.objects()

    for quote in quotes:
        for value in quote.tags:
            if value in user_tag:
                result.append(quote.quote)

    if len(result) == 0:
        return f"No matches."

    return result


@cache
def tags(user_tags: str):
    """
    tags:life,live — знайти та повернути список цитат, де є теги life або live (примітка: без пробілів між тегами life, live);
    :param user_tags:
    :return:
    """
    tags_ = user_tags.split(",")
    result = set()

    for tag_ in tags_:
        tags_ = tag(tag_)
        if "No matches." in tags_:
            continue
        for value in tags_:
            result.add(value)

    return list(result)


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
            start = timeit.default_timer()
            result = handler_command(user_inp)

            print(result)
            print(f"Time: {timeit.default_timer() - start}")

        except KeyboardInterrupt as er:
            print(er)
            exit()


if __name__ == "__main__":
    main()
