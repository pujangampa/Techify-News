import requests
from datetime import datetime

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9cdf6d6157c2438b9ebbe601362f85a5"
    news = requests.get(main_url).json()
    articles = news['articles']

    for idx, article in enumerate(articles, start=1):
        title = article.get('title', 'No Title')
        description = article.get('description', 'No Description')
        content = article.get('content', 'No content available')
        published_at = article.get('publishedAt', 'No publish date available')

        # Format the publish date in Indian standard time (IST)
        try:
            published_date = datetime.fromisoformat(published_at[:-1]).strftime("%d-%m-%Y")  # Remove 'Z' at the end
        except ValueError:
            published_date = 'No publish date available'

        print(f"{idx}. Title: {title}")
        print(f"   Description: {description}")
        print(f"   Content: {content}")
        print(f"   Published Date (IST): {published_date}\n")

# Call the function to fetch and display technology news with titles, descriptions, content, and publish dates (only date) in Indian format
news()
