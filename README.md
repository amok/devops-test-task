# Task

Create Vagrantfile and ansible playbook for setting up backend and frontend applications.

So I should be able to run `vagrant up`
And vagrant should

* create virtual server
* provision it (using ansible playbook) with everything needed for
`frontend` and `backend`
* download (f.e. git clone) and deploy `frontend` and `backend` to vagrant box
* frontend should be available on port 80, path `/app`
* backend should be available on port 80, path `/api`

you can provide your ansible playbook and Vagrantfile in any convinient way

# Frontend

It is webpack+react applicaiton

to build

```
cd frontend
npm install
NODE_ENV=production npm run build
```

application will be bundled to `frontend/build` folder as a static assets.

# Backend 

It is python(flask)+postgres app

how to run:

```
cd backend
pip install -r requirements.txt

POSTGRES_HOST=localhost \
POSTGRES_DB=app \
POSTGRES_USER=user \
POSTGRES_PWD=password \
python2 flask_app.py

```

now you should be able to open <host>:5000 and <host>:5000/from-db