import tkinter as tk
import tkinter.filedialog
import subprocess

def on_audio_button_clicked():
  file = tkinter.filedialog.askopenfilename()
  output_filename = audio_filename_entry.get()
  command = ['ffmpeg', '-i', file, output_filename]

  try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    output_text.insert(tk.END, output.decode('utf-8'))
  except subprocess.CalledProcessError as e:
    output_text.insert(tk.END, e.output.decode('utf-8'))

def on_youtube_button_clicked():
  url = url_entry.get()
  output_filename = youtube_filename_entry.get()
  command = ['youtube-dl', '-o', output_filename, url]
  process = subprocess.Popen(command, stdout=subprocess.PIPE)

  # Iterate over the lines of output and insert them into the text widget
  for line in iter(process.stdout.readline, b''):
    output_text.insert(tk.END, line.decode('utf-8'))
    output_text.see(tk.END)
    output_text.update()

window = tk.Tk()
window.title("Jubilee Video Tool | Jubilee Tabernacle Church")

image = tk.PhotoImage(file="image.png")

header_label = tk.Label(window, text="Jubilee", font=("Helvetica", 16))
header_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

image_label = tk.Label(window, image=image)
image_label.grid(row=0, column=1, padx=10, pady=10)

description_label = tk.Label(window, text="Let's you to download audio\n and video from various sources, as well\n as manipulate local images, audio, and video files!")
description_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Create a filename entry for the audio button
audio_filename_entry = tk.StringVar()
audio_filename_entry = tk.Entry(window, textvariable=audio_filename_entry, width=50)
audio_filename_entry.insert(0, "output.mp3")
audio_filename_entry.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

# Create the audio button
audio_button = tk.Button(window, text="Audio", command=on_audio_button_clicked)
audio_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

# Create a filename entry for the YouTube button
youtube_filename_entry = tk.StringVar()
youtube_filename_entry = tk.Entry(window, textvariable=youtube_filename_entry, width=50)
youtube_filename_entry.insert(0, "output.mp4")
youtube_filename_entry.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

# Create the YouTube button
youtube_button = tk.Button(window, text="YouTube", command=on_youtube_button_clicked)
youtube_button.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

# Create the URL entry
url_entry = tk.StringVar()
entry = tk.Entry(window, textvariable=url_entry, width=50)
entry.insert(0, "URL")
entry.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')

# Create the output text widget
output_text = tk.Text(window)
output_text.grid(row=5, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

window.mainloop()