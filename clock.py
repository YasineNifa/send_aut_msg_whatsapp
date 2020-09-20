from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from msg_au import send_msg
sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=2)

sched.start()