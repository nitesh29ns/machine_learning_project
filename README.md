# machine_learning_project
this is my first machine learning project.


Creating conda environment
'''
conda create -p venv python==3.7 -y
'''
'''
conda activate venv/  --> in command prompt
'''
'''
pip install -r requirements.txt
'''

to check remote url
'''
git remote -v
''' 

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = niteshsharma29.ns@gmail.com
2. HEROKU_API_KEY = 58133a7d-dfbf-4509-a08d-8b532dbc35f9
3. HEROKU_APP_NAME = nitesh-ml-app

BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .
'''
> Note: Image name for docker must be lowercase


To list docker image
'''
docker images
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
'''


To check running container in docker
'''
docker ps
'''

Tos stop docker conatiner
'''
docker stop <container_id>
'''

'''
python setup.py install
'''

to run ipynb file in vscode
'''
pip install ipykernel
'''