import json

FILE_PATH = "users.json"


def load_file():
    """
        Load user data from a JSON file.

        Returns:
            list[dict]: A list of user records, where each user is represented
            as a dictionary containing keys such as 'id', 'name', 'age',
            and 'email'.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
    """
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def filter_users_by_name(name):
    """
        Filter users by their name (case-insensitive) and print matching
        records.

        Args:
            name (str): The name to search for.

        Returns:
            None

        Notes:
            - Matching is case-insensitive.
            - Results are printed directly to stdout.
            - If no users match, nothing is printed.
    """
    users = load_file()

    filtered_users = [user for user in users if
                      user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(f"Id: {user['id']}\n"
              f"Name: {user['name']}\n"
              f"Age: {user['age']}\n"
              f"Email: {user['email']}\n")


def filter_users_by_age(age):
    """
        Filter users by their age and print matching records.

        Args:
            age (int | str): The age to search for. If provided as a string,
                it will be converted to an integer.

        Returns:
            None

        Raises:
            ValueError: If the provided age cannot be converted to an integer.

        Notes:
            - Results are printed directly to stdout.
            - If no users match, nothing is printed.
    """
    users = load_file()

    filtered_users = [user for user in users if
                      user["age"] == int(age)]

    for user in filtered_users:
        print(f"Id: {user['id']}\n"
              f"Name: {user['name']}\n"
              f"Age: {user['age']}\n"
              f"Email: {user['email']}\n")


def filter_users_by_email(email):
    """
        Filter users by their email address (case-insensitive) and print
        matches.

        Args:
            email (str): The email address to search for.

        Returns:
            None

        Notes:
            - Matching is case-insensitive.
            - Results are printed directly to stdout.
            - If no users match, nothing is printed.
    """
    users = load_file()

    filtered_users = [user for user in users if
                      user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(f"Id: {user['id']}\n"
              f"Name: {user['name']}\n"
              f"Age: {user['age']}\n"
              f"Email: {user['email']}\n")


def main():
    """
    Run the command-line interface for filtering user records.

    Prompts the user to choose a filtering criterion ('name', 'age',
    or 'email'),
    collects the corresponding input, and invokes the appropriate filtering
    function to display matching users.

    Returns:
        None

    Notes:
        - User input is normalized using stripping and lowercasing where
        applicable.
        - Output is printed directly to standard output.
        - If an unsupported option is provided, an informational message is
        shown.
    """
    filter_option = input(
        "What would you like to filter by? ('name' or 'age' or 'email'"
        " is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter email to search: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
