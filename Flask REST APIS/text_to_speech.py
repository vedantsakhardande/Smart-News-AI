# import os, boto3

# defaultRegion = 'ap-south-1'
# defaultUrl = 'https://polly.ap-south-1.amazonaws.com'

# def connectToPolly(regionName=defaultRegion, endpointUrl=defaultUrl):
#     return boto3.client('polly', region_name=regionName, endpoint_url=endpointUrl)

# def speak(polly, text, format='mp3', voice='Brian'):
#     resp = polly.synthesize_speech(OutputFormat=format, Text=text, VoiceId=voice)
#     soundfile = open('/tmp/sound.mp3', 'w')
#     soundBytes = resp['AudioStream'].read()
#     soundfile.write(soundBytes)
#     soundfile.close()
#     os.system('afplay /tmp/sound.mp3')  # Works only on Mac OS, sorry
#     os.remove('/tmp/sound.mp3')

# polly = connectToPolly()
# speak(polly, "Hello world, I'm Polly. Or Brian. Or anyone you want, really.")

import subprocess
import codecs

f = codecs.open("story.txt", encoding='utf-8')

cnt = 0
file_names = ''

for line in f:
    rendered = ''
    line = line.replace('"', '\\"')
    command = 'aws polly synthesize-speech --text-type ssml --output-format "mp3" --voice-id "Salli" --text "{0}" {1}'

    if '\r\n' == line:
        #A pause after a paragraph
        rendered = '<speak><break time= "2s"/></speak>'
    else:
        #A pause after a sentence
        rendered = '<speak><amazon:effect name=\\"drc\\">' + line.strip() + '<break time=\\"1s\\"/></amazon:effect></speak>'
    
    file_name = ' polly_out{0}.mp3'.format(u''.join(str(cnt)).encode('utf-8'))
    cnt += 1
    command = command.format(rendered.encode('utf-8'), file_name)
    file_names += file_name
    print(command)
    subprocess.call(command, shell=True)

print(file_names)
execute_command = 'cat ' + file_names + '>result.mp3'
subprocess.call(execute_command, shell=True)

execute_command = 'rm ' + file_names
print("Removing temporary files: " + execute_command)
subprocess.call(execute_command, shell=True)
