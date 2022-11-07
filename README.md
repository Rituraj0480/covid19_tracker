# covid19_tracker
Django web app for tracking global status of Covid-19.

### Update: Vaccine Slot Availability for Covid-19 using CoWIN API has been added.

The Indian Government had blocked the API for crawlers and servers outside of India. Further, these APIs are subject to a rate limit of 100 API calls per 5 minutes per IP. Therefore, if you want to run the Vaccine Slot Availability tool, you have to run it on local server with Indian IP address.

## Setup

The first thing to do is to clone the repository:

```sh
git clone https://github.com/Rituraj0480/covid19_tracker.git
cd covid19_tracker
```

Create a virtual environment to install dependencies in and activate it:

```sh
python -m venv myvenv
myvenv\Scripts\activate
```

Then install the dependencies:

```sh
pip install django
pip install requests
```

Once `pip` has finished downloading the dependencies:
```sh
python manage.py runserver
```
