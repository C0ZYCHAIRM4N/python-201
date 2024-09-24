# Use a quotes API, e.g. https://api.quotable.io/quotes/random
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://en.wikipedia.org/wiki/Doge_(meme))
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import requests
import json

def fetch_random_quote():
    response = requests.get("https://api.quotable.io/quotes/random")
    if response.status_code == 200:
        quote_data = response.json()[0]
        return quote_data['content']

def convert_to_doge_speech(text):
    words = text.split()
    doge_words = ["such", "much", "very", "so", "wow"]
    doge_speech = " ".join([f"{doge_words[i % len(doge_words)]} {word}" for i, word in enumerate(words)])
    return doge_speech

def fetch_doge_image_url():
    response = requests.get("http://shibe.online/api/shibes?count=1")
    if response.status_code == 200:
        image_url = response.json()[0]
        return image_url

def create_html(doged_quote, doge_image_url):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Doge Quote</title>
    </head>
    <body>
        <h1>Doge Quote</h1>
        <img src="{doge_image_url}" alt="Doge Image">
        <p>{doged_quote}</p>
    </body>
    </html>
    """
    with open("doge_quote.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    quote = fetch_random_quote()
    doged_quote = convert_to_doge_speech(quote)
    doge_image_url = fetch_doge_image_url()
    create_html(doged_quote, doge_image_url)
    print("HTML file created: doge_quote.html")