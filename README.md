# Tacotron2-Text-to-Speech-API
API developed using the Flask framework to serve inferences from Tacotron2 and Univnet/WaveGlow models generated from input text provided by a client. Infered audio is ouput as a single-dimension vector in list format. After receiving the infered audio, clients can convert the list into an array, normalize the audio over the max wav value (32768) and play. One option to play audio from an array is the sounddevice package in Python. 

## Tacotron2-Text-to-Speech-API
Models are not provided in the repository. AC voice Tacotron2 and Univnet models can be downloaded [here](https://drive.google.com/drive/folders/1Mp3I33caVRm7YkGYd5z3TXNdgIUF10U-) and moved into the models/ directory. As the config.py file already references these models, no adjustment to the config.py file is required for the API to serve inference requests. The API is compatible with other Tacotron2 and Univnet/WaveGlow models. The config.py file must been adjusted to reference the names and directories of new models. 


