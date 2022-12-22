import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import subprocess

# Function to handle the "Audio" button click
def on_select_audio_button_clicked():
  file = tkinter.filedialog.askopenfilename()
  audio_filename_entry.delete(0, tk.END)
  audio_filename_entry.insert(0, file)
  output_filename = audio_filename_entry.get()

# Function to handle the "Audio" button click
def on_start_audio_button_clicked():
  output_filename = audio_filename_entry.get()
  command = ['ffmpeg', '-i', output_filename, output_filename + '.mp3']

  try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    output_text.insert(tk.END, output.decode('utf-8'))
  except subprocess.CalledProcessError as e:
    output_text.insert(tk.END, e.output.decode('utf-8'))

# Function to handle the "download" button click
def on_download_button_clicked():
  url = url_entry.get()
  output_filename = download_filename_entry.get()
  command = ['youtube-dl', '-o', output_filename, url]
  process = subprocess.Popen(command, stdout=subprocess.PIPE)

  # Iterate over the lines of output and insert them into the text widget
  for line in iter(process.stdout.readline, b''):
    output_text.insert(tk.END, line.decode('utf-8'))
    output_text.see(tk.END)
    output_text.update()

# Function to handle the "Image" button click
def on_image_button_clicked():
  file = tkinter.filedialog.askopenfilename()
  image_filename_entry.delete(0, tk.END)
  image_filename_entry.insert(0, file)

# Function to handle the "MP3" button click
def on_mp3_button_clicked():
  file = tkinter.filedialog.askopenfilename()
  mp3_filename_entry.delete(0, tk.END)
  mp3_filename_entry.insert(0, file)

# Function to handle the "Start" button click
def on_start_button_clicked():
  image_file = image_filename_entry.get()
  audio_file = mp3_filename_entry.get()
  output_file = video_filename_entry.get()
  
  # Create the ffmpeg command
  command = ['ffmpeg', '-loop', '1', '-i', image_file, '-i', audio_file, '-c:v', 'libx264', '-tune', 'stillimage', '-c:a', 'aac', '-b:a', '192k', '-pix_fmt', 'yuv420p', '-shortest', output_file]

  # Run the command and get the output
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()

  # Insert the output into the text widget
  output_text.insert(tk.END, stdout.decode('utf-8'))
  output_text.insert(tk.END, stderr.decode('utf-8'))
  output_text.see(tk.END)
  output_text.update()

  try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    output_text.insert(tk.END, output.decode('utf-8'))
  except subprocess.CalledProcessError as e:
    output_text.insert(tk.END, e.output.decode('utf-8'))

window = tk.Tk()
window.title("Jubilee Video Tool | Jubilee Tabernacle Church")

# Load the image file
image = tk.PhotoImage(file="image.png")

# Create a header label
# header_label = tk.Label(window, text="Jubilee", font=("Helvetica", 16))
# header_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Create a description label
description_label = tk.Label(window, text="Download audio and video\n from various sources, as well\n as manipulate local images,\n audio, and video files!")
description_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Create a label for the image
image_label = tk.Label(window, image=image)
image_label.grid(row=0, column=2, padx=10, pady=10)

# Create a filename entry for the audio button
audio_filename_entry = tk.StringVar()
audio_filename_entry = tk.Entry(window, textvariable=audio_filename_entry, width=50)
audio_filename_entry.insert(0, "output.mp3")
audio_filename_entry.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Create the audio button
select_audio_button = tk.Button(window, text="Select Video", command=on_select_audio_button_clicked)
select_audio_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

# Create the audio button
start_audio_button = tk.Button(window, text="Start Audio Conversion", command=on_start_audio_button_clicked)
start_audio_button.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

# Create a horizontal separator
separator = ttk.Separator(window, orient="horizontal")
separator.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

# Create a filename entry for the download button
download_filename_entry = tk.StringVar()
download_filename_entry = tk.Entry(window, textvariable=download_filename_entry, width=50)
download_filename_entry.insert(0, "output.mp4")
download_filename_entry.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')

# Create the download button
download_button = tk.Button(window, text="Start Video Download", command=on_download_button_clicked)
download_button.grid(row=4, column=1, padx=10, pady=10, sticky='nsew', columnspan=2)

# Create a URL entry field
url_entry = tk.StringVar()
entry = tk.Entry(window, textvariable=url_entry, width=50)
entry.insert(0, "URL")
entry.grid(row=3, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

# Create a horizontal separator
separator = ttk.Separator(window, orient="horizontal")
separator.grid(row=5, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

# Create a filename entry for the image button
image_filename_entry = tk.StringVar()
image_filename_entry = tk.Entry(window, textvariable=image_filename_entry, width=50)
image_filename_entry.insert(0, "image.png")
image_filename_entry.grid(row=6, column=0, padx=10, pady=10, sticky='nsew')

# Create the image button
image_button = tk.Button(window, text="Select Image", command=on_image_button_clicked)
image_button.grid(row=6, column=1, padx=10, pady=10, sticky='nsew', columnspan=2)

# Create a filename entry for the MP3 button
mp3_filename_entry = tk.StringVar()
mp3_filename_entry = tk.Entry(window, textvariable=mp3_filename_entry, width=50)
mp3_filename_entry.insert(0, "audio.mp3")
mp3_filename_entry.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')

# Create the MP3 button
mp3_button = tk.Button(window, text="Select Audio", command=on_mp3_button_clicked)
mp3_button.grid(row=7, column=1, padx=10, pady=10, sticky='nsew', columnspan=2)

# Create a filename entry for the video
video_filename_entry = tk.StringVar()
video_filename_entry = tk.Entry(window, textvariable=video_filename_entry, width=50)
video_filename_entry.insert(0, "video.mp4")
video_filename_entry.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')

# Create the start button
start_button = tk.Button(window, text="Start Image/Audio Conversion", command=on_start_button_clicked)
start_button.grid(row=8, column=1, padx=10, pady=10, sticky='nsew', columnspan=3)

# Create a text widget for output
output_text = tk.Text(window)
output_text.grid(row=9, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

window.mainloop()