"""
read text form the doucment 
check text for curse wrds. 
use a website for the text to check the profanity.
check each word of the wirtten email against these words.
if profanity is detected put on the warning message

"""
import urllib


def read_text_from_file():
    read_fd = open("C:\\2_WORK\\2_projects\\2_workspace\\repo\\Python\\LearningPy\\some.txt")
    content_of_the_file = read_fd.read();
    print(content_of_the_file)
    read_fd.close()
    check_text_for_profanity(content_of_the_file)
    
def check_text_for_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("This docuemnt does not have curse words!")
    else:
        print("Could not scan the document properly")


read_text_from_file()    
