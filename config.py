import argparse

# Set Base Directory

basedir='__Tacotron2/'

# # Set Inference Arguments

parser = argparse.ArgumentParser(prog = 'ProgramName', description = 'What the program does',epilog = 'Text at the bottom of help')
args = parser.parse_args()
args.tacotron2=f"""models/checkpoint_Tacotron2_910.pt"""
args.vocoder='univnet'
# args.vocoder='WaveGlow'
# args.waveglow=f"""models/checkpoint_WaveGlow_700.pt"""
args.wn_channels=256
args.univnet=f"""models/univ_c32_0829.pt"""
args.univnet_config=f"""{basedir}univnet/config/config_bs24.yaml"""
args.upload_to_s3=False
args.fp16=False
args.cpu=True
args.include_warmup=False
args.use_ground_truth_mels=False
args.log_file=None
args.output_audio_vector=True

# Set Audio Parameters for Tacotron2

args.sampling_rate=22050
args.stft_hop_length=256
args.max_wav_value=32768.0
args.filter_length=1024
args.hop_length=256
args.win_length=1024
args.mel_fmin=0
args.mel_fmax=8000