from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def realnews(headline):
    driver = webdriver.Chrome()

    driver.get('https://nytimes.com')
    try:
        driver.execute_script('document.querySelector("#welc_supercontainer").style.display="none";')
    except:
        pass
    driver.execute_script('''
        var headers = document.querySelectorAll("h2")
        for (var i = 0; i < headers.length; i++){
            headers[i].textContent = arguments[0];
        }

    ''', headline)


    outname =  headline + '.png'

    driver.save_screenshot('static/' + outname)
    driver.quit()
    return outname

def realnews_headless(headline):
    outname = 'static/' + headline + '.png'
    if os.path.exists(outname):
        return outname
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get('https://nytimes.com')
    try:
        driver.execute_script('document.querySelector("#welc_supercontainer").style.display="none";')
    except:
        pass
    driver.execute_script('''
        var headers = document.querySelectorAll("h2")
        for (var i = 0; i < headers.length; i++){
            headers[i].textContent = arguments[0];
        }

    ''', headline)

    driver.save_screenshot(outname)
    driver.quit()
    return outname

if __name__ == '__main__':
    import sys
    realnews(sys.argv[1])
