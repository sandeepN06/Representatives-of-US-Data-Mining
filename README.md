Steps:

* Initialise the project using  ' scrapy startproject [name] '

* fetch('https://www.house.gov/representatives') -> To check at first whether website can be crawled (We get status code 200 , hence possible)

* Next we name the web crawler

* We next Understand the ideology of what we need to get using clients requirements

* Then move towards inspection of elements using css/xpath selectors

* When we extract the element of particular type we get selector object

* We do all our inspection and testing on scrapy shell so that there wont be any load affecting the website

* We then extract all the items in the required format and prettify them using string comprehension / regular expression

* Then export as a JSON Format using (scrapy crawl webscraper -O output.json) command where webscraper here is the name given to our project
