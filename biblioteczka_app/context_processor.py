from datetime import datetime
import time

def get_date(request):
    #time.sleep(5) blokuje stronę przez 5 sekund...
    return {'date': datetime.now().date()}