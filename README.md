# What is?

    It's a regex generator for phone numbers, you can give a list of phone numbers separated by comma and it will return a regular expresion for each number and a global regex to match all numbers in a single regex

# Howto use it?
    It's tested on Python3.

    If you have docker installed, use it.

    There is a Dockerfile with the Python command to execute, modify the numbers list that appears in CMD:
        Ex. CMD [ "python", "/usr/src/regex-generator/src/Controller.py", "111222333,456321321,123987765" ]
    Then execute:
        $ docker build . -t regex-generator && docker run -it regex-generator

    If you don't have docker, execute the file Controller.py giving one argument with the numbers list comma separated:
        Ex: python3 src/Controller.py 111222333,456321321,123987765

