import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from xiaodao.items import XiaodaoItem

class ZixueSpider(Spider):
    print('进入爬虫')
    name = 'zixue'
    current_page = 1

    def start_requests(self):
        url = 'https://www.x6d.com/html/18.html'
        yield Request(url)
    
    def parse(self, response):
        list_selector = response.xpath("//div[@class='info-tit fr']")
        for one_selector in list_selector:
            try:
                title = one_selector.xpath("a/text()").extract_first()
                tag = one_selector.xpath("a/i/text()").extract_first()
                relative_url = one_selector.xpath("a/@href").extract_first()

                # 拼接url
                url = response.urljoin(relative_url)

                # 给item赋值
                item = XiaodaoItem()
                item['title'] = title
                item['tag'] = tag
                item['url'] = url

                # 请求详情页
                yield Request(url, meta={"item": item}, callback=self.parse_detail)
            except Exception as es:
                print(es)
        if self.current_page == 1:
            self.total_page = response.xpath("//*[@id='page']/div/li[9]/span/strong[1]/text()").extract_first()
            self.total_page = int(self.total_page)
        self.current_page+=1
        if self.current_page <= self.total_page:
        # if self.current_page <= 1:
            next_url = "https://www.x6d.com/html/18-%d.html"%(self.current_page)
            yield Request(next_url)
    def parse_detail(self, response):
        aticle = response.xpath("//div[@class='article-content']")
        # baidu = aticle.re(r'<a.*(https://pan.baidu.com.*?)">')
        baidu = aticle.xpath('//a[re:test(@href, "https://pan.baidu.com.*$")]//@href').extract_first()
        baidu_code = aticle.re(r'提取码.*?(\w{4})') and aticle.re(r'提取码.*?(\w{4})')[0]
        tianyi = aticle.xpath('//a[re:test(@href, "https://cloud.189.cn.*$")]//@href').extract_first()
        tianyi_code = aticle.re(r'访问码.*?(\w{4})') and aticle.re(r'访问码.*?(\w{4})')[0]

        item = response.meta['item']
        item['baidu'] = baidu
        item['baidu_code'] = baidu_code
        item['tianyi'] = tianyi
        item['tianyi_code'] = tianyi_code
        yield item
        # print('正则', baidu, baidu_code, tianyi, tianyi_code)