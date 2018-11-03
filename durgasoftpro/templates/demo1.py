q=input('enter your qualification')
y=input('enter your passd out year')
p=input('enter your percentage')
if q=="btech" or q=="be":
    if y=="2017" or y=="2018":
        if  p>o and p<35:
            print('you not eligible')
        elif p>=60 and p<=75:
            print('you come to next week')
        elif p>=75 and p<=85:
            print('you come to tomorrow')
        elif p>85 and p<=100:
            print('you come to today only')
        else:
            print('you entered invalid percentage')
    else :
        print('you are not a fresher')
else:
    print('sorry, this is only for be and betch students only ')





