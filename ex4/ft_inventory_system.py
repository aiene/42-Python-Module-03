import sys


def main():
    print("=== Inventory System Analysis ===")

    argc = len(sys.argv)

    if argc == 1:
        print("No items provided")
        return

    inventory: dict[str, int] = {}

    for item in sys.argv[1:]:
        parts = item.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{parts[0]}'")
            continue

        name = parts[0]
        quantity = parts[1]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            inventory[name] = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    if total > 0:
        for item in inventory.keys():
            percentage = (inventory[item] / total) * 100
            print(f"Item {item} represents {percentage:.1f}%")

        most_abundant = item_list[0]
        least_abundant = item_list[0]

        for item in item_list:
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item

            if inventory[item] < inventory[least_abundant]:
                least_abundant = item

        print(
            f"Item most abundant: {most_abundant} "
            f"with quantity {inventory[most_abundant]}"
        )

        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {inventory[least_abundant]}"
        )

    inventory.update({"magic_item": 1})

    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
