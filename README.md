# 1. What is it for

This is a custom demo template to create a voice over video with the voice, sound template, and text of your choice. You can copy the URL of the video from YouTube that you would like to overlay as a parameter. 

For example: 

```video = "URL"```
```voice = "voice of your choice"```
```speed = 110 - choose the voice speed```
```soundTemplate = "sound design of your choice"```
```masteringPreset = "heavyducking" - Ducking temporarily lowers the volume of the specified audio anytime a second audio signal is specified.```

Once you've rendered your python script you will receive a magic link in your terminal which you can use to share your audio file with the world. 

# 2. How it works

First we create an audio file with the chosen text, voice, mastering presets and sound template.
Then with the downloaded video, we overlay the created audio onto video. 
The final video is then created and downloaded into your directory as overlayAudio.mp4 

# 3. How to run - instructions:

In your local install [FFMPEG](https://www.ffmpeg.org/download.html)
Then open your code editor and install the following packages: 
1. ```pip3 -r requirements.txt```
2. Get your API_KEY from [API.audio console](https://console.api.audio/)
3. Add .env file to your project root directory and add your API_KEY=****************************
4. Make sure that you added all the values to the variables (voice, speed, video, soundTemplate) (For more voices and sound templates visit our [Voice & Sound library](https://library.api.audio/voices)
5. To render your python script: Open your terminal at your project and type in: python3 main.py
6. Your files will be saved in your project directory
7. Find your magic shareable link printed out in your terminal with your audio URL and share it!
8. Your voice over has now been created as overlayAudio.mp4
