from twisted.logger import Logger
from twisted.internet import task
from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy_scrapper.pccomponentes.spiders.search import Search
log = Logger()

if __name__ == "__main__":
    def run_crawl():
        log.info('Searching pccomponentes')
        runner = CrawlerRunner()
        runner.crawl(Search)

    l = task.LoopingCall(run_crawl)
    l.start(60)

    reactor.run()
