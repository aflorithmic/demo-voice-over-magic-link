# Python v3.10.2
import os
from dotenv import load_dotenv

import youtube_dl  # version 2021.12.17
import apiaudio  # version 0.16.0
import requests  # version 2.27.1

load_dotenv()
API_KEY = os.getenv("API_KEY")
apiaudio.api_key = API_KEY


def get_magic_link(url):
    """
    Takes an api.audio url and returns a magic link.
    The magic link is an API.audio feature which allows you to share the audio you created
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
    }
    payload = {"url": url}
    response = requests.post(
        "https://v1.api.audio/url/share", json=payload, headers=headers
    )
    print("👉 COPY AND SHARE YOUR AUDIO LINK🥳 ", response.text)


def apiaudio_create(scriptname, message, voice, speed, soundTemplate, masteringPreset):
    """
    Takes a script name and a text and creates a mastered audio reading your text and names it as the script name.
    It uses Script, Speech and Mastering features from API.audio sdk.
    """
    script = apiaudio.Script().create(
        scriptText=message,
        scriptName=scriptname,
        moduleName="cyber-guru",
        projectName="cyber-guru",
    )
    print(script)

    sectionProperties = {
        "intro": {"endAt": 10, "justify": "centre"},
        "main": {"endAt": 20, "justify": "centre"},
        "main1": {"endAt": 30, "justify": "centre"},
        "outro": {"endAt": 42, "justify": "flex-start"},
    }

    response = apiaudio.Speech().create(
        scriptId=script.get("scriptId"),
        voice=voice,
        speed=speed,
        silence_padding=(1000 * 2),
    )

    response_mastering = apiaudio.Mastering().create(
        scriptId=script.get("scriptId"),
        soundTemplate=soundTemplate,
        sectionProperties=sectionProperties,
        masteringPreset=masteringPreset,
    )

    print("This is the response from mastering", response)
    response = apiaudio.Mastering().download(
        scriptId=script.get("scriptId"), destination="."
    )
    return response_mastering.get("url")


def my_hook(d):
    """
    Gives you the status of your Youtube video being downloaded
    """
    if d["status"] == "finished":
        print("Done downloading, now converting...")


def downloadyoutube(url):
    """
    Downloads your video from Youtube and saves it into your current directory as downloadedVideo.mp4
    """
    ydl_opts = {
        "format": "best",
        "outtmpl": "downloadedVideo.mp4",
        "noplaylist": True,
        "nooverwrites": True,
        "progress_hooks": [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def combine_audio(audio):
    """
    Combines a video called downloadedVideo.mp4 with the audio named as the argument.
    Creates a file in the root folder named overlayAudio.mp4.
    """
    os.system(
        f'ffmpeg -i downloadedVideo.mp4 -i {audio} -filter_complex "[0:a]volume=0[a0]; [1:a]volume=0.9[a1]; [a0][a1]amix=duration=longest[a]" -map 0:v -map "[a]" -c:v copy overlayAudio.mp4'
    )


def download_create(text, voice, speed, soundTemplate, masteringPreset, video):
    """
    Main function. Downloads the video from YouTube. Creates an audio and merges video and audio in a video called overlayAudio.mp4
    """
    downloadyoutube(video)
    response = apiaudio_create(
        "audio", text, voice, speed, soundTemplate, masteringPreset
    )
    combine_audio("audio.mp3")
    get_magic_link(response)


text = """
        <<soundSegment::intro>>
        <<sectionName::intro>>

        Elisabetta. è stata la prima appena 2 anni fa, e poi. Paolo, Erika, Francesca. 

        <<soundSegment::main>>
        <<sectionName::main>>

        E tutti gli altri. Oltre un milione di lezioni erogate. 

        <<soundSegment::main>>
        <<sectionName::main1>>

       Creando negli utenti un livello adeguato di cyber consapevolezza. E riducendo concretamente il rischio di subire attacchi cyber. 
        
        <<soundSegment::outro>>
        <<sectionName::outro>>
         Cyber Guru. Aiutiamo ogni giorno persone e organizzazioni ad aumentare la loro sicurezza. Per saperne di più visita cyber guru punto I T.
        """

video = "https://www.youtube.com/watch?v=WRrOrjYQXuE"
voice = "diego"
speed = 110
soundTemplate = "cityechoes"
masteringPreset = "heavyducking"

download_create(text, voice, speed, soundTemplate, masteringPreset, video)
