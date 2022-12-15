from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import shutil

# I didn't add an icon,but you can add one if you want to
root = Tk()
root.title("Youtube Downloader")
canvas = Canvas(root,
                width=500,
                height=500
                )
canvas.pack()
# Functions


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_mp4file():
    # Get user path
    get_link = link_field.get()
    # Get selected path
    user_path = path_label.cget("text")
    root.title("Downloading...")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # Move file to selected directory
    shutil.move(mp4_video, user_path)
    messagebox.showinfo("Info!", "Download Completed")
    root.title("Youtube Downloader")


def download_mp3file():
    get_link = str(link_field.get())
    user_path = path_label.cget("text")
    root.title("Downloading")
    mp3_video = YouTube(get_link).streams.filter(only_audio=True).first()
    output = mp3_video.download(output_path=user_path)
    base, ext = os.path.splitext(output)
    new_file = base + '.mp3'
    os.rename(output, new_file)
    messagebox.showinfo("Info!", "Download Completed")
    root.title("Youtube Downloader")


# Download Buttons
download_mp4btn = Button(root,
                         text="Download Mp4",
                         font=("Arial", 15),
                         bg="red",
                         fg="white",
                         command=download_mp4file
                         )

download_mp3btn = Button(root,
                         text="Download Mp3",
                         font=("Arial", 15),
                         bg="red",
                         fg="white",
                         command=download_mp3file
                         )

# Link Field
link_field = Entry(root,
                   width=40,
                   font=("Arial", 15)
                   )

link_label = Label(root,
                   text="Enter The Download Link",
                   font=("Arial", 15)
                   )

# Select Path For Saving Files
path_label = Label(root,
                   text="Select Path For Download",
                   font=("Arial", 15),
                   fg="green"
                   )
select_btn = Button(root,
                    text="Select Path",
                    bg="red",
                    fg="#fff",
                    padx=22,
                    pady=5,
                    font=("Arial", 15),
                    command=select_path
                    )

canvas.create_window(250,
                     280,
                     window=path_label
                     )

canvas.create_window(250,
                     330,
                     window=select_btn
                     )

canvas.create_window(250,
                     170,
                     window=link_label
                     )

canvas.create_window(250,
                     220,
                     window=link_field
                     )

canvas.create_window(100,
                     390,
                     window=download_mp4btn
                     )

canvas.create_window(400,
                     390,
                     window=download_mp3btn
                     )

root.mainloop()
