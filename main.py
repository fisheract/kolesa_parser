import scrapy


def clean_price(text):
    digits = [symbol for symbol in text if symbol.isdigit()]
    cleaned_text = ''.join(digits)
    if not cleaned_text:
        return None
    return int(cleaned_text)


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://kolesa.kz/mototehnika/motocikly/suzuki/?year[from]=2002']

    def parse(self, response):
        for motorcycle in response.css('.a-info-top'):
            link = motorcycle.css('span.a-el-info-title')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()
            raw_price = motorcycle.css('span.price::text').get()
            price = raw_price and clean_price(raw_price) or None
            motorcycle.css('.pictures-list::atr(srcset)')
            yield {
                'title': title,
                'href': href,
                'price': price,
            }

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)