import requests, os
from flask import Flask, render_template, request
from scrapper import extract_subreddit

os.system("clear")


subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")

@app.route('/')
def home():
  return render_template("home.html",subreddits=subreddits)

@app.route('/read')
def read():
  read_arr = []
  for subreddit in subreddits:
    isOn = request.args.get(subreddit)
    if isOn:
      read_arr.append(subreddit)
      #extract_subreddit(subreddit)
  reddits = extract_subreddit(read_arr)
  print(reddits)
  return render_template("read.html",read_arr=read_arr,reddits = reddits)

app.run(host="0.0.0.0")