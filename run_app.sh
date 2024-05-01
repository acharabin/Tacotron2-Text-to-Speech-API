sudo fuser -k 5000/tcp
sudo nohup python app.py >> log.txt 2>&1 &
