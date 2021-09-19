from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=option)
url = "https://books.toscrape.com/"
driver.get(url)

pagesURLs = driver.find_elements_by_css_selector("#default > div > div > div > aside > div.side_categories > ul > li > ul > li > a")
i = 0
pagesArray = []
for pageURL in pagesURLs:
    pagesArray.append(pageURL.get_attribute("href"))
    print(pagesArray[i])
    i = i + 1
driver.close()


for page in pagesArray:

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path="chromedriver.exe",options=option)
    driver.get(page)

    books = driver.find_elements_by_xpath("//article[@class='product_pod']/h3/a")
    for book in books:
        print(book.get_attribute("text") + " - " + book.get_attribute("href"))

    driver.close()




