from datetime import datetime, date
from scanner import scan
from daily_charts import daily_charts
from results_charts import results_charts

now = datetime.now()
with open("last_update.txt") as f:
    last_update = f.read()
    f.close()

def update():
    scan() 
    daily_charts()
    results_charts()
    f = open("last_update.txt", "w")
    f.write(str(datetime.now()).split(" ")[0])
    f.close()
    print("Update complete")


if str(now) > str(last_update) + " 22:59:00":
    update()
else:
    print("last update: {}".format(str(last_update)))