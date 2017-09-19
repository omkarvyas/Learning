import webbrowser
import time

total_breaks = 3
break_count = 0

print("This Program started on" + time.ctime())
while(break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=o8_vxD_Yk2M")
    break_count = break_count +1
print "Good bye!"

    

