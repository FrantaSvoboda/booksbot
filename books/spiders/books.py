# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'http://lidovajidelna.cz/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'quantity': quote.css('section.menu h3::text').get(),
                'food': quote.css('td.name::text').get(),
                'price': quote.css('td.price::text').get(),
                'quantity': quote.css('td.quantity::text').get(),
            }