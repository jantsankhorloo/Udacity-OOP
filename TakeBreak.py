import time
import webbrowser

total_break = 3
break_count = 0

print ("This program started on"+time.ctime())
while breal_count < total_break:
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=Doy20_RHH9w&feature=share")
    break_count += 1
    
#Additional useful material:
#http://pymotw.com/2/webbrowser/
#http://stackoverflow.com/questions/15472707/make-python-program-wait
