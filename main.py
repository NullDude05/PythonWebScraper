import singletonwrapper as stw
import csv

test = stw.SingletonCaseWrapper()


test.Search("bowling balls", "name", "q")
test.Click("name", "btnK")
test.Click("link_text", "Shopping")
names = test.GetContentClass('EI11Pd Hb793d', 'h3')
prices = test.GetContentText('a8Pemb OFFNJ')

results = []

x = 0
for x in range(len(names)):
    results.append((names[x], prices[x]))
    

print(results)



with open("searchresults.csv", "w") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Name", "Price"])

    for row in results:
        writer.writerow(row)

# results = []
# content = driver.page_source
# soup = BeautifulSoup(content, features="html.parser")
# print(soup)

# def searchtopic(search_name):
#     search_box = driver.find_element("name", "q")
#     search_box.send_keys(search_name)


# def main():
#     searchtopic("Bowling Balls")


