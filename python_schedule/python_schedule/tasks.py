import os
from celery import shared_task

@shared_task
def maincall():
        os.system('echo This is first Call > /home/$(echo $USER)/TextTime1')

@shared_task
def secondcall():
        os.system('echo This is second Call > /home/$(echo $USER)/TextTime2')
        
@shared_task
def thirddcall():
        os.system('echo This is third Call > /home/$(echo $USER)/TextTime3')
        
@shared_task
def fourthcall():
        os.system('echo This is fourth Call > /home/$(echo $USER)/TextTime4')

@shared_task
def fifthcall():
        os.system('echo This is fifth Call > /home/$(echo $USER)/TextTime5')

@shared_task
def sixthcall():
        os.system('echo This is sixth Call > /home/$(echo $USER)/TextTime6')
        
