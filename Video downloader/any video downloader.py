from pytube import YouTube

# Prompt the user to enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
https://www.youtube.com/watch?v=PJWemSzExXs
# Create a YouTube object with the provided URL
yt = YouTube(video_url)

# Get available video streams
streams = yt.streams.filter(progressive=True).all()

# Print available quality options
print("Available Quality Options:")
for i, stream in enumerate(streams):
    print(f"{i + 1}. {stream.resolution}")

# Prompt the user to select a quality option
quality_choice = int(input("Enter the number corresponding to the desired quality option: "))
selected_stream = streams[quality_choice - 1]

# Prompt the user to enter the storage location
storage_location = input("Enter the storage location (provide full path): ")

# Print the video title
print("Downloading video:", yt.title)

# Download the video to the specified storage location
selected_stream.download(output_path=storage_location)

print("Video downloaded successfully!")

