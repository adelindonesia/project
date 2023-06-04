from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import web_scraping

scheduler = BlockingScheduler()
scheduler.add_job(web_scraping, 'interval', hours=2)
scheduler.start()