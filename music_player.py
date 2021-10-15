from tkinter import *
from pygame import mixer
import pygame
import datetime
import os
song_index = 3
list_song_title = os.listdir("songs/")
volume = 0.4
current_song_time = 0
ALL_SONGS = len(list_song_title)

def print_global_time():
    time = str(datetime.datetime.now())[:-7]
    label_label.config(text=time)
    win.after(1000, print_global_time)

def print_song_time():
    global current_song_time
    if mixer.music.get_busy() == True:
        current_song_time += 1
    song_time.config(text=str(datetime.timedelta(seconds=current_song_time)))
    win.after(1000, print_song_time)

def play():
    mixer.music.unpause()
    print("음악을 재생합니다.")

def pause():
    mixer.music.pause()
    print("음악을 일시정지합니다.")

def after():
    global song_index
    global current_song_time
    if song_index == ALL_SONGS - 1:
        song_index = 0
    else:
        song_index += 1
    song_title.config(text=list_song_title[song_index])
    mixer.music.load(f"songs/{list_song_title[song_index]}")
    mixer.music.play()
    mixer.music.queue(f"songs/{list_song_title[(song_index + 1) % len(list_song_title)]}")
    song_time.config(text="0:00:00")
    current_song_time = 0
    print("다음 곡으로 넘어갑니다.")

def before():
    global song_index
    global current_song_time
    if song_index == 0:
        song_index = ALL_SONGS - 1
    else:
        song_index -= 1
    song_title.config(text=list_song_title[song_index])
    mixer.music.load(f"songs/{list_song_title[song_index]}")
    mixer.music.play()
    mixer.music.queue(f"songs/{list_song_title[(song_index + 1) % len(list_song_title)]}")
    song_time.config(text="0:00:00")
    current_song_time = 0
    print("이전 곡으로 넘어갑니다.")

def volume_up():
    global volume
    if volume >= 1:
        volume = 1
    else:
        volume = volume + 0.05
    mixer.music.set_volume(volume)

def volume_down():
    global volume
    if volume <= 0:
        volume = 0
    else:
        volume = volume - 0.05
    mixer.music.set_volume(volume)
    
def play_next_music(event):
    global song_index
    song_index = (song_index + 1) % len(list_song_title) # 인덱스 + 1 증가
    mixer.music.load(f"songs/{list_song_title[song_index]}")
    mixer.music.play()

def rewind():
    global current_song_time
    mixer.music.play()
    print("되감기를 눌렀습니다.")

def fast_forward():
    print("빨리 감기를 눌렀습니다.")

# 창 제작 -> 실행
win = Tk()
win.geometry("1280x640") # 크기 변경
win.title("music_player")
mixer.init()
pygame.init()
mixer.music.set_volume(volume)
mixer.music.load(f"songs/{list_song_title[song_index]}")
mixer.music.play()
mixer.music.queue(f"songs/{list_song_title[(song_index + 1) % len(list_song_title)]}")
label_label = Label(win, font=("Times", "30"))
song_time = Label(win, font=("Times", "20"), text="0:00:00")
song_time.pack()
btn_volume_up = Button(win, width=5, text="+", command=volume_up)
btn_volume_up.place(x = 0, y = 100)
btn_volume_up = Button(win, width=5, text="-", command=volume_down)
btn_volume_up.place(x = 0, y = 150)
btn_rewind = Button(win, width=10, text="⏪︎", command=rewind)
btn_rewind.place(x = 370, y = 550)
btn_rewind = Button(win, width=10, text="⏩︎", command=fast_forward)
btn_rewind.place(x = 890, y = 550)
btn1 = Button(win, width = 15, text="음악 재생", command=play)
btn1.place(x = 560, y = 550)
btn2 = Button(win, width = 15, text="일시정지", command=pause)
btn2.place(x = 780, y = 550)
btn3 = Button(win, width = 15, text="다음 곡", command=after)
btn3.place(x = 670, y = 550)
btn4 = Button(win, width = 15, text="이전 곡", command=before)
btn4.place(x = 450, y = 550)
label_label.pack()
song_title = Label(win, font=("맑은 고딕", "25"), text=list_song_title[song_index])
song_title.pack()
print_song_time()
print_global_time()
win.bind('<<music_end>>', play_next_music)
win.mainloop() # 반복문

# 음악 재생 프로그램
# 1. 버튼 : 재생, 일시정지, 다음 곡, 이전 곡 [V]
# 2. 곡의 시간 [V]
# 3. 곡의 이름 [V]
# 4. 영상 썸네일 [보류]
# 5. 현재 시간 [V]
# 6. 불륨 조절 [V]
# 7. 버튼 클릭 시, 각 버튼에 맞는 명령 수행 [V]
# 8. 곡이 끝난 후 자동재생 [V]
# 9. + 10초 -10초 [보류]
# 10. 노래 자동 추가 기능 [V]
# 믹서 init -> music.load -> music.play -> music.pause