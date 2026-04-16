import json
import sys
from pathlib import Path

DATA_FILE = Path("roomlight_data.json")


def load_data():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    return {"profiles": {}, "rooms": {}}


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def error(message):
    print(f"Error: {message}")
    return 1


def create_profile(data, name, brightness, mode):
    if name in data["profiles"]:
        return error(f"profile '{name}' already exists")

    data["profiles"][name] = {"brightness": brightness, "mode": mode}
    save_data(data)
    print(f"Profile '{name}' created.")
    return 0


def add_room(data, room_number):
    if room_number in data["rooms"]:
        return error(f"room '{room_number}' already exists")

    data["rooms"][room_number] = {"profile": None}
    save_data(data)
    print(f"Room '{room_number}' added.")
    return 0


def apply_profile(data, profile_name):
    if profile_name not in data["profiles"]:
        return error(f"profile '{profile_name}' does not exist")
    if not data["rooms"]:
        return error("no rooms found")

    for room in data["rooms"].values():
        room["profile"] = profile_name

    save_data(data)
    print(f"Profile '{profile_name}' applied to all rooms.")
    return 0


def apply_profile_to_room(data, room_number, profile_name):
    if room_number not in data["rooms"]:
        return error(f"room '{room_number}' does not exist")
    if profile_name not in data["profiles"]:
        return error(f"profile '{profile_name}' does not exist")

    data["rooms"][room_number]["profile"] = profile_name
    save_data(data)
    print(f"Profile '{profile_name}' applied to room '{room_number}'.")
    return 0


def reset_room(data, room_number):
    if room_number not in data["rooms"]:
        return error(f"room '{room_number}' does not exist")

    data["rooms"][room_number]["profile"] = None
    save_data(data)
    print(f"Room '{room_number}' reset.")
    return 0


def show_profiles(data):
    if not data["profiles"]:
        print("No profiles found.")
        return 0

    print("Profiles:")
    for name, profile in sorted(data["profiles"].items()):
        print(f"- {name}: brightness={profile['brightness']}, mode={profile['mode']}")
    return 0


def show_rooms(data):
    if not data["rooms"]:
        print("No rooms found.")
        return 0

    print("Rooms:")
    for room_number, room in sorted(data["rooms"].items()):
        profile_name = room["profile"]
        if not profile_name:
            print(f"- Room {room_number}: no profile assigned")
            continue

        profile = data["profiles"].get(profile_name, {})
        brightness = profile.get("brightness", "?")
        mode = profile.get("mode", "?")
        print(f"- Room {room_number}: profile={profile_name}, brightness={brightness}, mode={mode}")
    return 0


def print_help():
    print("RoomLight CLI")
    print("Commands:")
    print("  create_profile <name> <brightness> <mode>")
    print("  add_room <room_number>")
    print("  apply_profile <profile_name>")
    print("  apply_profile_to_room <room_number> <profile_name>")
    print("  reset_room <room_number>")
    print("  show_profiles")
    print("  show_rooms")


def main():
    args = sys.argv[1:]
    if not args:
        print_help()
        return 1

    command = args[0]
    data = load_data()

    if command == "create_profile":
        if len(args) != 4:
            return error("Usage: create_profile <name> <brightness> <mode>")
        try:
            brightness = int(args[2])
        except ValueError:
            return error("brightness must be an integer")
        return create_profile(data, args[1], brightness, args[3])

    if command == "add_room":
        if len(args) != 2:
            return error("Usage: add_room <room_number>")
        return add_room(data, args[1])

    if command == "apply_profile":
        if len(args) != 2:
            return error("Usage: apply_profile <profile_name>")
        return apply_profile(data, args[1])

    if command == "apply_profile_to_room":
        if len(args) != 3:
            return error("Usage: apply_profile_to_room <room_number> <profile_name>")
        return apply_profile_to_room(data, args[1], args[2])

    if command == "reset_room":
        if len(args) != 2:
            return error("Usage: reset_room <room_number>")
        return reset_room(data, args[1])

    if command == "show_profiles":
        return show_profiles(data)

    if command == "show_rooms":
        return show_rooms(data)

    print_help()
    return error(f"unknown command '{command}'")


if __name__ == "__main__":
    raise SystemExit(main())
