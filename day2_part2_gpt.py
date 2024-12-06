import requests
import argparse

def get_input(url, session_cookie):
    """
    Fetch input data from the given URL using a session cookie.
    Returns the input data as a string or None.
    """
    cookies = {'session': session_cookie}
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            print("Production input successfully fetched.")
            return response.text
        else:
            print(f"Failed to fetch production data. HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching production data: {e}")
    return None

def is_safe(levels):
    """
    Checks if the levels are safe based on the original rules:
    - Either all increasing or all decreasing
    - Differences between adjacent entries are 1-3
    """
    is_increasing = all(0 < levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    is_decreasing = all(-3 <= levels[i + 1] - levels[i] < 0 for i in range(len(levels) - 1))
    return is_increasing or is_decreasing

def is_safe_with_dampener(levels):
    """
    Checks if the levels are safe after applying the Problem Dampener:
    - Removes one level at a time and checks if the modified report is safe
    """
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe(modified_levels):
            return True

    return False

def process_input_data(input_data):
    """
    Processes input data to determine the number of safe reports.
    """
    input_array = input_data.strip().split('\n')
    safe_count = 0
    for report in input_array:
        levels = list(map(int, report.split()))
        if is_safe_with_dampener(levels):
            safe_count += 1
    return safe_count

def run(mode):
    """
    Runs the program in the given mode: 'test' or 'production'.
    """
    if mode == 'test':
        print("Running in test mode...")
        test_data = """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
        """
        safe_count = process_input_data(test_data)
        print(f"Safe levels count in test mode: {safe_count}")
    elif mode == 'production':
        print("Running in production mode...")
        url = "https://adventofcode.com/2024/day/2/input"
        session_cookie = '53616c7465645f5f75699d0c2c1f625078478ebaba0655d6020dd19cbde82438d1be79967f2c0c081e0d0b858f2860abe29311c98d1aca0fce79f487de0bf840'
        input_data = get_input(url, session_cookie)
        if input_data:
            safe_count = process_input_data(input_data)
            print(f"Safe levels count in production mode: {safe_count}")
        else:
            print("Failed to fetch production data. Exiting.")
    else:
        print("Invalid mode. Use 'test' or 'production'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 2 Solution")
    parser.add_argument(
        "mode",
        choices=["test", "production"],
        help="Mode to run the program: 'test' or 'production'.",
    )
    args = parser.parse_args()
    run(args.mode)

