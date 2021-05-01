<img src="./img/Psych-blog_mood-swings.jpeg" width="2000" />

CONTENTS OF THIS FILE
---------------------

 * Introduction to script
 * Requirements
 * Recommended modules
 * Installation
 * Running the website locally
 * Introduction

INTRODUCTION TO SCRIPT
----------------------
The following script perform a sentiment analysis on data collected from weekly survey of The Knowledge House students's responses. We used NLP with the IBM Watson ML API to make.
* The main purpose of this study is to better serve TKH students by recognizing their mood and help case coordinators address any possible issues based on the mood reported by the API. 

For example some of these students might be happy, stress, angry or upset about a particular part of technical or career class.
* We believe case coordinators get a lot of responses and it might be hard for them to identify and separate those that might need a bit of extra help. We were hoping to create a tone analyzer tool that would parse through the responses and show a “tone” to that response. 

We believe our idea will make it easier for case coordinators to isolate those that need extra help. It would make students feel more heard and perhaps in the future we could add an automized feature that will sent a message to those students that sound upset so that they can schedule an appointment ASAP. Since the classes will be doubling next year, we think this will help take some of that extra workload for case coordinators.

REQUIREMENTS
------------

This module requires the following libraries:

| Library | Description |
| --- | --- |
| [Streamlit](https://streamlit.io/) | Streamlit turns data scripts into shareable web apps in minutes, all in Python, all for free. No front‑end experience required. |
| [Pandas](https://pandas.pydata.org/docs/) | Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. |
| [MatplotLib](https://matplotlib.org/) | Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. |
| [Numpy](https://numpy.org/devdocs/docs/howto_document.html) | NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more. |
| [Urllib](https://docs.python.org/3/library/urllib.html) | URL handling modules. |
| [Requests](https://docs.python-requests.org/en/master/) | Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3. |


INSTALLATION
------------

 1. cd to the directory where requirements.txt is located.
 2. activate your virtualenv
 3. run: pip install -r requirements.txt in your shell.

RUNNING THE WEBSITE LOCALLY
---------------------------

To run the website- run the following code in your shell:
 ```python

streamlit run app.py
 
```

INTRODUCTION
-------------

## About us
| Preview                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [<img src="./img/clariza.jpg" width="1000" />](https://www.linkedin.com/in/clarizamayo/)                                                                                                                                                | Clariza is an Ambitious data science fellow committed to academic excellence. Prepared to implement diverse skill sets, technical proficiencies and new perspectives to leadership personnel. Adaptable and driven with strong work ethic and ability to thrive in team-based or individually motivated settings. At her core, she is a problem solver and experimenter who’s passionate about using sociological and data driven approaches to tackling projects and building meaningful products that help people live better lives. She has worked in Medical billing, consumer and customer service and is now looking to pivot her career path towards Data Science.                                                                                    |
| [<img src="./img/stani.jpg" width="1000" />](https://www.linkedin.com/in/stanislava-hristova/)                                                                                                                                                | Stanislava is a life-long learner with a background in Marketing and a passion for Cybersecurity & Data. Team-focused, resourceful, and detail-oriented with a successful record of over 7 years of client-facing experience. Seeking to effectively bridge the gap between Engineering and Business Teams, along with the capability of rendering excellent technical and communications skills. |
| [<img src="./img/bryant.jpg" width="1000" />](https://www.linkedin.com/in/bryantnovas/)                                                                                                                                                | A life-long learner with a passion for IT & Data. Team-focused, resourceful, and detail-oriented with a successful record of over 8 years of client-facing experience. Seeking to effectively bridge the gap between Engineering and Business Teams, along with the capability of rendering excellent technical and communications skills.  |
