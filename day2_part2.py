import requests

def get_input(url, session_cookie):
    """
    Fetch input data from the given URL using a session cookie.
    Returns the input data as a string or None.
    """
    cookies = {'session': session_cookie}
    try:
        response = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            return response.text
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def is_sorted_with_one_removed(levels):
    """
    Checks if the list is sorted (increasing or decreasing)
    when one element is removed.
    """
    for i in range(len(levels)):
        temp_levels = levels[:i] + levels[i+1:]  # Remove one element
        if temp_levels == sorted(temp_levels) or temp_levels == sorted(temp_levels, reverse=True):
            return True
    return False

def is_safe(levels):
    """
    Checks if the levels are safe based on the rules:
    - Either increasing or decreasing with one removal allowed
    - Differences between adjacent entries are 1-3 with one failure allowed
    """
    # Check if levels are sorted or can become sorted with one removal
    is_increasing_or_decreasing = levels == sorted(levels) or levels == sorted(levels, reverse=True) or is_sorted_with_one_removed(levels)

    # Check for adjacent differences, allowing one failure
    bad_level_count = 0
    for i in range(len(levels) - 1):
        diff = abs(levels[i + 1] - levels[i])
        if diff < 1 or diff > 3:  # Difference out of range
            bad_level_count += 1
            if bad_level_count > 1:  # More than one failure
                return False

    # Safe if both conditions are met
    return is_increasing_or_decreasing


# URL and session cookie for fetching input
url = "https://adventofcode.com/2024/day/2/input"
session_cookie = '53616c7465645f5f75699d0c2c1f625078478ebaba0655d6020dd19cbde82438d1be79967f2c0c081e0d0b858f2860abe29311c98d1aca0fce79f487de0bf840'

# Load input data into an array
input_data = get_input(url, session_cookie)
if input_data:
    input_array = input_data.strip().split('\n')  # Split text into lines
    print("Input data loaded into array:")
    print(input_array)
    safe_levels = 0
    for report  in input_array:
        levels = list(map(int, report.split()))
        if is_safe(levels):
          safe_levels += 1

    print(safe_levels)
    

