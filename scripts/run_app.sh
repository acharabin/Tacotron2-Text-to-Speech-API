sudo fuser -k 5000/tcp
sudo nohup python app.py >> logs/log.txt 2>&1 &
