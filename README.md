# Task

Create Vagrantfile and ansible playbook for setting up backend and frontend applications.

So I should be able to run `vagrant up`
And vagrant should
1) create virtual server
2) provision it (using ansible playbook) with everything needed for
`frontend` and `backend`
3) frontend should be available on port 80, path `/app`
4) backend should be available on port 80, path `/api`

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