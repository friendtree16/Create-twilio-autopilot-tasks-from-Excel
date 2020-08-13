# Create twilio autopilot tasks from Excel

## What is it
This application can create twilio autopilot tasks from Excel.
`separate-to-csv.py` separate to csv and json file from Excel. csv file is used to update samples, and json file used to update actions.
`upload-csv.py` update twilio autopilot tasks from csv and json.

## Supported Python Version
- Python 2.7

## Installation
`pip install -r requirements.txt`

## Usage
### Create upload CSV and json file from Excel
`python separate-to-csv.py <filepath>`

### Upload to twilio autopilot
`python upload-csv.py --account-sid=xxxxxx --auth-token=aaaaa --assistant-sid=bbbbbb`

## 本アプリについて
本アプリケーションはExcelで作成した会話フローを用いてtwilio autopilotのtasksを作成します。
`separate-to-csv.py`はExcelファイルをアップロード用にcsvとjsonに分割させます。csvファイルはsamplesをアップデートするのに使用し、jsonファイルはアクションをアップデートするのに利用します。
`upload-csv.py`は作成したcsvファイルとjsonファイルを使ってtwilio autopilotを更新します。

##  インストール方法
`pip install -r requirements.txt`

## 使い方
### Excelファイルからcsvファイルとjsonファイルを作成
`python separate-to-csv.py <filepath>`

### twilio autopilotに更新をかける
`python upload-csv.py --account-sid=xxxxxx --auth-token=aaaaa --assistant-sid=bbbbbb`