import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# We don't want to open the webpage in a real browser, but in a headless browser.
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

# Now we use the driver to render the JavaScript webpage.
driver.get("http://quotes.toscrape.com/js/")
# page_source stores the HTML markup of the webpage, not the JavaScript code.
page_source = driver.page_source

# And we can then parse the rendered HTML markup as usual.
tree = html.fromstring(page_source)
quotes = tree.xpath('//div[@class="quote"]')

for quote in quotes:
    author = quote.xpath('./span/small[@class="author"]/text()')
    text = quote.xpath('./span[@class="text"]/text()')
    print(f"{author[0]}: {text[0]}")

