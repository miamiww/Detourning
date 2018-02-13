from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://foxnews.com')

#multi line string
script = '''

var elements = document.querySelectorAll("h1,h2,h3,h4,p,lie,a");

for(var i = 0 ; i < elements.length; i++){
    elements[i].textContent = "lol";
}
'''

driver.execute_script(script, "something else")

driver.save_screenshot('loll.png')
driver.quit()
