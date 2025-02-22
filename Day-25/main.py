import pandas

full_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = full_data['Primary Fur Color']
new = fur_color.value_counts()
new_data = pandas.DataFrame(new)
new_data.to_csv("squirrels_count.csv")

