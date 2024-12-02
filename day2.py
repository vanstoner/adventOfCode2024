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

def is_safe(levels):
    """
    Checks if the levels are:
    either increasing or decreasing
    have a difference between adjacent entries of 1-3
    """
    # Check if the list is increasing or decreasing
    is_increasing_or_decreasing = levels == sorted(levels) or levels == sorted(levels, reverse=True)

    # Check for adjacent differences
    diffs_within_range = True
    for i in range(len(levels) - 1):
        diff = abs(levels[i + 1] - levels[i])
        # Check if out of range
        if diff < 1 or diff > 3:  
            diffs_within_range = False
            break

    # Return True only if both conditions are met
    return is_increasing_or_decreasing and diffs_within_range



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
    

