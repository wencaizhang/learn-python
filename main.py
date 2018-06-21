# coding:utf8

import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url(): # 如果有新的url
            try:
                new_url = self.urls.get_new_url() # 就取出新的url
                print('正在爬取第', count, '个网页', new_url)
                html_cont = self.downloader.download(new_url) # 然后下载html页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 100:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()
            
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)