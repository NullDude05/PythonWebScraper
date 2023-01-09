import singletonwrapper as stw

test = stw.SingletonCaseWrapper()


test.Search("bowling balls", "name", "q")
test.Click("name", "btnK")
test.Click("link_text", "Shopping")
results = test.GetContentClass('EI11Pd Hb793d', 'h3')
print(results)
# results = []
# content = driver.page_source
# soup = BeautifulSoup(content, features="html.parser")
# print(soup)

# def searchtopic(search_name):
#     search_box = driver.find_element("name", "q")
#     search_box.send_keys(search_name)


# def main():
#     searchtopic("Bowling Balls")


