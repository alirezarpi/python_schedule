from django.shortcuts import render
import jdatetime 
from . import urls
import threading
from django.http import HttpResponse
from .tasks import *
from dateutil import parser
import pytz

def homepage(request):
    return render(request,'getdate.html', {'name' : 'alireza'})

def gotdate(request):
    year  = request.GET['getdateyear']
    month = request.GET['getdatemonth']
    day   = request.GET['getdateday']
    time  = request.GET['gettime']
    order = request.GET['func']
    
    gdateyear = jdatetime.JalaliToGregorian(int(year), int(month), int(day)).gyear
    gdatemonth = jdatetime.JalaliToGregorian(int(year), int(month), int(day)).gmonth
    gdateday = jdatetime.JalaliToGregorian(int(year), int(month), int(day)).gday
    gdate = str(gdateyear) + "-" + str(gdatemonth) + "-" + str(gdateday)
    date = str(year) + '-' + str(month) + '-' + str(day)
    
    print("================================")
    print("Jalali Date: "+ date)
    dateg = (gdate.replace('-', '/'))
    print("Date:        " + str(dateg))
    print("Time:        " + str(time))
    print("Func:        " + str(order))
    print("================================")
    
    # changing timezone to utc
    raw_date = dateg + " " + time + ":00" + " " + "GMT-4:30"
    print(raw_date) 
    dt = parser.parse(raw_date)
    ddt = dt.astimezone (pytz.utc)
    print("UTC TIME: " + str(ddt))
    
    if(order == "1"):
        maincall.apply_async((), eta=ddt) # Call the function in the time
    elif(order == "2"):
        secondcall.apply_async((), eta=ddt)
    elif(order == "3"):
        thirddcall.apply_async((), eta=ddt)
    elif(order == "4"):
        fourthcall.apply_async((), eta=ddt)
    elif(order == "5"):
        fifthcall.apply_async((), eta=ddt)
    elif(order == "6"):
        sixthcall.apply_async((), eta=ddt)
        
    return render(request, 'gotdate.html', {'getdate': date, 'gettime': time})
