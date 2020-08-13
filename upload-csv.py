# coding:utf-8

import sys
import glob
import re
import csv
from twilio.rest import Client
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--account-sid", type=str)
parser.add_argument("--auth-token", type=str)
parser.add_argument("--assistant-sid", type=str)

args = parser.parse_args()
accountSid = args.account_sid
if accountSid == None:
    print('error:please input account sid use --account-sid.')
    sys.exit()

authToken = args.auth_token
if authToken == None:
    print('error:please input auth token use --auth-token.')
    sys.exit()

assistantSid = args.assistant_sid
if assistantSid == None:
    print('error:please input assistant sid use --assistant-sid.')
    sys.exit()

client = Client(accountSid,authToken)

def createTask(assistantSid, taskName):
    task = client.autopilot.assistants(
        assistantSid).tasks.create(unique_name=taskName)
    return task.sid


def uploadSamples(assistantSid, taskSid, csvFilePath):
    csvFile = open(csvFilePath)
    csvData = csv.reader(csvFile)
    for row in csvData:
        client.autopilot.assistants(assistantSid).tasks(taskSid).samples.create(language='en-US', tagged_text=row[0])

def uploadAnswer(assistantSid, taskSid, jsonFilePath):
    jsonFile = open(jsonFilePath)
    jsonObj = json.load(jsonFile)
    client.autopilot.assistants(assistantSid).tasks(taskSid).update(actions=jsonObj)

questionFiles = glob.glob("./upload/questions/*.csv")
for file in questionFiles:
    # ./upload/と.csvを削除
    pattern = './upload/questions/(.+?).csv'
    taskName = next(re.finditer(pattern, file)).groups()[0]
    taskSid = createTask(assistantSid, taskName)
    uploadSamples(assistantSid, taskSid, file)
    answerFileName = './upload/answer/' + taskName + '.json'
    uploadAnswer(assistantSid, taskSid, answerFileName)


