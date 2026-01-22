from bs4 import BeautifulSoup
#lxml If html.parser is not working than use lxml parser

with open("website.html") as file:
    contents =file.read()

#Create class called beautiful soup so that we can use it as a object
#Passing the content which we need to parse and the language in which its written
soup = BeautifulSoup(contents, "html.parser")
#Once beautiful soup has made sence of our data than the soup becomes entire html code and can
#be used like a python object to get hold of any data
#for example
print(soup.title.string)
#Different methods give diff output so just explore

#Here if i wanted to find all the anchor tags, all para than use findAll() nethod
#searching by name for all the anchor tags we can do similar with para's and lot more
anchor_tags= soup.find_all(name="a")
print(anchor_tags)
#Now if i only need the text than will  have to loop and use getText method
for tag in anchor_tags:
    print(tag.getText())
#if inside the anchor tag i want to add hold of the values which href contain i can use
for tag in anchor_tags:
    print(tag.get("href"))

#Setting constraints if we want a particular H1 with a particular ID, here i am using id also
heading=soup.find(name='h1', id='name')

#Now similar to CSS where we can get hold of a particular value, we can do similar i soup as well
company_url=soup.select_one(selector="p a")
#Above the selector works in a similar way as CSS selector
print(company_url)
#Now similarly as select_one was giving the first occurence now selects giving all the values
#which matches the condition
#selecting class with header
soup.select(".heading")

