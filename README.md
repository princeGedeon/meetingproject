"# meetingproject" 

- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


/admin --> pour aller sur la age admin

### Whisper
1) Installer ffmpeg

    -- on Ubuntu or Debian
    **sudo apt update && sudo apt install ffmpeg**
    
    -- on Windows using Chocolatey (https://chocolatey.org/)
    **choco install ffmpeg**
    
    -- on Windows using Scoop (https://scoop.sh/)
    **scoop install ffmpeg**
2) pip install git+https://github.com/openai/whisper.git 
