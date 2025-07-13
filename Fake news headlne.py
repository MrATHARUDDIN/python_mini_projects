import random as rn

List_of_name = ["Elon Musk", "Mr. Bean", "Taylor Swift", "The Rock", "CatGPT"]
List_of_work = ["riding a pig", "dancing with aliens", "selling ice cream", "wearing a chicken suit", "singing opera"]
List_of_location = ["Times Square", "the Moon", "a haunted house", "a pizza shop", "underwater city"]

name = rn.choice(List_of_name)
work = rn.choice(List_of_work)
location = rn.choice(List_of_location)

final_news = f"{name} was spotted {work} at {location}!"

print(final_news)
