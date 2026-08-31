import random
import typing


def gen_event() -> typing.Generator:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["move", "run", "eat", "sleep", "grab",
               "release", "use", "swim", "climb"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list) -> typing.Generator:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


def main():
    print("=== Game Data Stream Processor ===")

    generator = gen_event()

    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events = []

    for i in range(10):
        events.append(next(generator))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
