from playsound import playsound
print("Music List \n 1.sample \n 2.sample2 \n 3.sample3")
order = input('enter the music  name :')
if "sample" in order :
    playsound('sample.mp3')
elif"sample2" in order:
    playsound('sample2.mp3')
elif "sample3.mp3" in order:
    playsound('sample3.mp3')
else:
    print("entered wrong choice re run program")