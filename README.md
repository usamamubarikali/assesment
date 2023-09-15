
# Set-up
1. Pull down the Assesment repo.
```
$ git clone https://github.com/usamamubarikali/assesment.git
```
2. Paste the .env file inside the backend folder

3. Build the development image once you are inside the backend folder.
```
$ docker build -f Dockerfile
```

4. Run the development image.
```
$ docker-compose up -d
```

5. To run the frontend go inside the frontend folder and run.
```
$ npm install
```

6. Once the dependancies are installed run server by.
```
$ npm start
```

