import pandas

cpark = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")

colors = cpark["Primary Fur Color"]

gray_color = colors[colors == "Gray"]
cinnamon_color = colors[colors == "Cinnamon"]
black_color = colors[colors == "Black"]

black_count = black_color.count()
gray_count = gray_color.count()
cinnamon_count = cinnamon_color.count()


count = [gray_count, cinnamon_count, black_count]

dictionary = {
    "The Colors": ["Gray", "Cinnamon", "Black"],
     "The Count": [gray_count, cinnamon_count, black_count]
}

new_csv = pandas.DataFrame(dictionary)
new_csv.to_csv("my_file.csv")

# for i in cpark["Gray"]

# gray = color["Gray"]
# print(gray)
#
# for thing in thelist: