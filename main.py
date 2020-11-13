from flask import Flask, render_template, request, redirect, send_file
from scrapping import extract_wwr, extract_stackoverflow, extract_remoteok
import os
import csv

os.system("clear")

app =Flask("SearchRemoteJob")

db = {}
word = ""

@app.after_request
def add_header(rqst):
    rqst.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    rqst.headers["Pragma"] = "no-cache"
    rqst.headers["Expires"] = "0"
    rqst.headers['Cache-Control'] = 'public, max-age=0'
    return rqst

@app.route("/")
def home():
  # extract_remoteok("python")
  return render_template("home.html")

@app.route('/search')
def result():
  word = request.args.get('word')
  word = str(word).lower()
  fromDB = db.get(word)
  if fromDB:
    jobs = fromDB
  else:
    jobs = []
    jobs.extend(extract_remoteok(word))
    jobs.extend(extract_stackoverflow(word))
    # jobs.extend(extract_wwr(word))
    db[word] = jobs
  leng = len(jobs)
  print(jobs)
  return render_template("result.html",jobs=jobs,word=word,leng = leng)

@app.route('/export')
def export_csv():
  word = request.args.get('word')
  word = str(word).lower()
  file = open(f"{word}.csv",mode="w",encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "link"])
  jobs = db.get(word)
  for job in jobs:
    writer.writerow(list(job.values()))
  return send_file(f"{word}.csv",
                     mimetype='text/csv',
                     attachment_filename=f"{word}.csv",
                     as_attachment=True)

app.run(host = "localhost")

