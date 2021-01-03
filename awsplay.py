import boto3
import playsound
import os
polly_client = boto3.client('polly')


def play_sound(text):
    response = polly_client.synthesize_speech(VoiceId='Emma', OutputFormat='mp3', Text=text)
    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()

    playsound.playsound("speech.mp3", True)

play_sound("If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals.")

