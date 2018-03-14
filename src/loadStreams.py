from selenium import webdriver
from creds import username, password

def login() :
    path_to_chromedriver = 'C:/Program Files (x86)/~AssortedPrograms/chromedriver'  # change path as needed
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)

    url = 'https://cs.anu.edu.au/streams/Tutor.php'
    browser.get(url)

    browser.find_element_by_name("Username").clear()
    browser.find_element_by_name("Username").send_keys(username)

    browser.find_element_by_name("Password").clear()
    browser.find_element_by_name("Password").send_keys(password)

    browser.find_element_by_name("TutorLogin").click()