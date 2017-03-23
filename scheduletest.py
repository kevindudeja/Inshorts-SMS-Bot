import schedule
import time

def job(t):
    print "I'm working...", t
    return

print "Testing"
#schedule.every(1).seconds.do(job, 'Its time')
schedule.every().day.at("03:33").do(job,' ')

while True:
    schedule.run_pending()
    time.sleep(5) # wait one minute