# DolarGrapher

DolarGrapher is a simple project built using **Nuxt.js** and **Django REST Framework**. It shows the historical price fluctuations of the USD currency in CLP.

## Main requirements

- Pyhton3.6
- NodeJs v10.16.0
- npm 6.9.0

## Setup

1. Clone/download this project.
2. Outside the DolarGrapher folder create and activate a virtual environment.
`$ python3 -m venv ENV`
`$ source ENV/bin/activate`
3. Install dependencies:
`(ENV) $ pip3 install -r DolarGrapher/back/requirements.txt `
`(ENV) $ cd DolarGrapher/front`
`(ENV) $ npm install`

## Configuration

1. Set your hosts addresses for the DRF api by editing the `settings.py` file inside the _DolarGrapher/back/back/_ folder:
`...`
`ALLOWED_HOSTS = ['0.0.0.0']`
`...`
2. Set your Nuxt app '_host_' address and the '_baseURL_' property for axios (just the IP) by editing the `nuxt.config.js` file inside the _DolarGrapher/front_ folder:
`export default {`
`...`
`    server: {`
`        port: 3000,         // default: 3000`
`       host: '0.0.0.0',     // default: localhost`
`    },`
`    axios: {`
`        baseURL: "http://0.0.0.0:8000/back"`
`    },`
`...`
`}`
3. Then, edit the DRF api host information in the python scripts that will populate our SQLite database. The files are `hisUsdSeed.py` and `dailyUpdt.py`, both inside the _DolarGrapher/back_ folder:
`...`
`apiHost = '0.0.0.0'`
`...`
4. Finally, schedule the execution of `dailyUpdt.py` script to be run daily at 00:01:00 by using a tool like cron.

## Usage

- To run the API, write the commands:
`$ source ENV/bin/activate`
`(ENV) $ python DolarGrapher/back/manage.py runserver`

- To gather the historical data and populate the database use the next command after the API is up.
`(ENV) $ python DolarGrapher/back/hisUsdSeed.py`

- To run the web app, use the commands:
`$ cd DolarGrapher/front`
`$ npm run dev`

- Now you can visit 'http://0.0.0.0:3000' on your browser!
