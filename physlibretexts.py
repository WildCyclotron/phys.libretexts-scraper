from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

options = Options()
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


driver = webdriver.Chrome(options=options)




def search(query,page):
    
    """Scrapes the search query page and returns the results in json format.
    
    
    Parameters 
    ------------
    query: The query you want to search for.
    page: The page number for which you want the results.
        Every page returns 11 results. 
          
          
    """
    driver.get(f'https://phys.libretexts.org/Special:Search?qid=&fpid=230&fpth=&query={query}&type=wiki')
    clicks = page
    while clicks>1:
        showMoreButton = driver.find_element_by_xpath('//*[@id="mt-search-spblls-component"]/div[2]/div/button')
        showMoreButton.click()
        clicks -= 1
        time.sleep(2)

    output = []
    start = (page-1)* 11
    stop = start + 12
    for i in range(start+1,stop):
        content = driver.find_element_by_xpath(f'//*[@id="search-results"]/li[{i}]/div/div[2]/div[2]/span[1]').text
    
        path = f'//*[@id="search-results"]/li[{i}]/div/div[1]/a'
        for a in driver.find_elements_by_xpath(path):
            title = a.get_attribute('title')
            link = a.get_attribute('href')
            result = {
            "title":title,
            "link":link,
            "content":content
            }
            output.append(result)
    output_json = {
        "results":output
    }
    driver.close()
    return json.dumps(output_json)



