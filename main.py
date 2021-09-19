from selenium import webdriver

WebDriverEXE = "chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(executable_path=WebDriverEXE,options=option)
url = "https://books.toscrape.com/"
driver.get(url)

# loop on the books pages
pagesURLs = driver.find_elements_by_css_selector("#default > div > div > div > aside > div.side_categories > ul > li > ul > li > a")
pagesArray = []
for pageURL in pagesURLs:
    pagesArray.append(pageURL.get_attribute("href"))
driver.close()

# loop on the books pages to get their names and URLs
for page in pagesArray:

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path=WebDriverEXE,options=option)
    driver.get(page)

    books = driver.find_elements_by_xpath("//article[@class='product_pod']/h3/a")
    for book in books:
        print(book.get_attribute("text") + " - " + book.get_attribute("href"))

    driver.close()



