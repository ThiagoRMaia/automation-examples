from pathlib import Path

WIKIPEDIA_ELEMENTS = {'website': 'http://www.wikipedia.org',
                      'do_you_mean': 'searchdidyoumean',  # class
                      'suggestion': 'mw-search-DYM-suggestion',  # id
                      'search_result': 'mw-search-results',  # class
                      'list_item': 'li',  # tag
                      'first_result': '//*[@id="mw-content-text"]/div/ul/li[1]/div[1]/a',  # xpath
                      'title': 'firstHeading',  # id
                      'toc': 'toc'  # id
                      }

TRAVELEX_ELEMENTS = {'website': 'https://www.travelex.co.uk/',
                     'cards': "//*[@class='matchHeights matchTitleHeights simple__animation simple__animation_animate clearfix']",  # xpath
                     'slider': "//*[@class='matchHeights matchTitleHeights simple__animation simple__animation_animate clearfix slick-initialized slick-slider']",  # xpath
                     'dots': 'slick-dots',  # class
                     'dot_item': 'li'  # tag
                     }

API_CALLS = {"comments": {"postId": 1, "id": 1, "name": "id labore ex et quam laborum", "email": "Eliseo@gardner.biz",
                          "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium",
                          "url": 'http://jsonplaceholder.typicode.com/comments/1'}
             }
PATHS = {'chromedriver': str(Path().absolute().parent) + r'\artifacts\chromedriver.exe'
         }
