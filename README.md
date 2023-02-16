# Shorten Link CLI Tool

This tool shorten links and receives information about total clicks of shorten link.

It uses [bitly.com](https://bitly.com/) API service as a source of information.


## Requirements

 - python3
 - `requests` library
 - `python-dotenv` library


## How to install

Get the source code of this repo:
```
git clone https://github.com/leksuss/bitly.git
```

Open project folder:
```
cd bitly
```

Then install dependencies:
```
# If you would like to install dependencies inside virtual environment, you should create it first.
pip3 install -r requirements.txt
```

## How to setup

This script uses bitly.com API, so you should [register](https://bitly.com/a/sign_up) and [get an API KEY](https://app.bitly.com/settings/api/) for using this script. It looks like `acd3342212d3820c260d78082ea50b79f7609f6e`. You should insert it as a value of `BITLY_API_KEY` in `.env_examle` file. Then rename file to `.env`


## How to use

You can pass as argument any valid link and receive shorten link (like this: `https://bit.ly/3jQdelW`)
Or if you input already shorten bitly link, you will receive count of clicks on this link made.

```
# to get shorten link
python3 bitly.py https://github.com/leksuss/bitly

# to get count of clicks
python3 bitly.py https://bit.ly/3jQdelW
```

## Running example

<img src="https://github.com/leksuss/bitly/blob/master/.github/bitly_example.gif" width="700">

