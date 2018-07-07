from pathlib import Path

ELEMENTS = {'do_you_mean': 'searchdidyoumean',  # class
            'suggestion': 'mw-search-DYM-suggestion',  # id
            'search_result': 'mw-search-results',  # class
            'list_item': 'li',  # tag
            'first_result': '//*[@id="mw-content-text"]/div/ul/li[1]/div[1]/a',  # xpath
            'title': 'firstHeading',  # id
            'toc': 'toc'  # id
            }

PATHS = {'chromedriver': str(Path().absolute().parent) + r'\artifacts\chromedriver.exe'
         }
