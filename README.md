# automation-examples
This project was created as an effort to exemplify selenium-based test automation on two distinct websites.

## Setup
1. Go to [Python download](https://www.python.org/downloads/) website.
2. Download [Python 3.6.4](https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe).
3. After the installation, open a cmd window.
4. Type in: **pip3 install -r *"<path_to_requirements>"*** pointing towards this project's requirements.txt file.
5. At the end of the installation, close the cmd.

## Running the scripts
1. Open a cmd and type in: **cd <path_to_project>/tests**
2. To run the tests use: 
    - **python wikipedia_selenium.py** or, 
    - **python travelex_selenium.py** or,
    - **python api_calls.py**
3. Wait for the results :)

## Important notes
The following tests _are supposed to_ fail:
1. **wikipedia_selenium.py**
    - test_01_check_title: 
        -   The test is case-sensitive.
2. **api_calls.py**
    - test_03_check_delete: 
        -   The call returns OK code but does not delete entry.
    - test_03_check_no_content: 
        -   The call returns OK code when it should return No Content code.
        
        
The following tests _may_ fail:
1. **wikipedia_selenium.py**
    - test_04_check_result_content: 
        -   Depending on what the wikipedia may suggest, the entry may or may not have a ToC.
