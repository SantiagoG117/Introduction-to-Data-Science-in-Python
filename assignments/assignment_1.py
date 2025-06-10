import re
from pathlib import Path


def names():
    names = []

    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # Split the words by spaces, commas and dots
    words = re.split(r'[ ,\.]+', simple_string)

    pattern = r'^[A-Z][a-z]*'

    names = [word for word in words if re.match(pattern, word)]

    return names


names()

# The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class.
# Create a regex to generate a list of just those students who received a B in the course.


def grades():
    # List to store all the grades equal to B
    students = []

    # Create the path for accessing the file
    path = Path('./grades.txt')

    # Get the content of the file in a text format
    content = path.read_text()

    # Extract each student in the txt file and store it into a list
    lines = content.splitlines()

    # Define a regex pattern to match lines ending with ": B"
    pattern = r':\sB$'

    # Add the students with a grade equal to B to the students list
    # list comprehenssion syntax [expression for item in items if condition]
    students = [line.split(':')[0]
                for line in lines if re.search(pattern, line.strip())]

    return students


# Logdata file records the acces a user makes when visiting a webpage. Each line of the log has the following items:
#     a host
#     a user_name (sometimes the user name is missing. In this case use '-' as the value for user_name)
#     the time a request was made
#     the HTTP request type
# Convert the data in logdata.txt into a list of dictionaries

def logs():
    # Create the list of dictionaries
    logs_list = []

    # Access the data and store it in a list of strings
    logs_lines = Path('./logdata.txt').read_text().splitlines()

    # Regular expressions:
    host_pattern = r'^(.*?)\s-\s'
    user_name_pattern = r'-\s(.*?|\-)\s\['
    time_pattern = r'\[(.*?)\]'
    request_pattern = r'"(.*?)"'

    # Iterate over the logs_lines and store each log as a dictionary inside the logs_list
    for log in logs_lines:
        log_entry = {
            'host': re.search(host_pattern, log).group(1),
            'user_name': re.search(user_name_pattern, log).group(1),
            'time': re.search(time_pattern, log).group(1),
            'request': re.search(request_pattern, log).group(1)
        }
        logs_list.append(log_entry)
    return logs_list


logs()
