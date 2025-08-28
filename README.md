# About apod-crawler
Simple web crawler designed to scrape NASA's blog "Astronomy Picture of the Day" for pictures, its descriptions and other information.

## Description
This web crawler goes through a selected array of urls from NASA's blog called "Astronomy Picture of the Day" and fetches some information from the daily astronomy media posted: date, title, media (image url or unavailable if video), media type (image or video) and all credits.
The spider downloads and saves crawled pictures in a relative folder "downloads" within the main project folder, then relays collected information using a json format in the terminal.

## Getting Started
### Dependencies
Scrapy

### Executing
cd apod
scrapy crawl apod

## TODO
Other methods for inputting or selecting urls to be scraped