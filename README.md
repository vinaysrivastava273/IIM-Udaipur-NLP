# IIM-Udaipur-NLP
This repository consists of my project on Natural Language Processing under Prof. Bhavya Singhvi, IIM Udaipur.

The project aimed at "Understanding Public Corporate Disclosures on Instagram" using Latent Dirichlet Allocation ( part of Natural Language Processing ).

Used Instagram Graph API ( it's free to use once you register as a Facebook developer on their website) with the following permissions.
![API Permissions](https://github.com/vinaysrivastava273/IIM-Udaipur-NLP/blob/9927e22b387131fba3c1e2114d135ec9b8305023/images/API%20Permissions.jpg)

Collected the following data from the home-page of NIFTY50 firms' Instagram page.
![Nifty50 main page data](https://github.com/vinaysrivastava273/IIM-Udaipur-NLP/blob/9927e22b387131fba3c1e2114d135ec9b8305023/images/Nifty50%20main%20page%20data.jpg)

Looks neat when viewed as JSON file.
![Asian Paints data](https://github.com/vinaysrivastava273/IIM-Udaipur-NLP/blob/9927e22b387131fba3c1e2114d135ec9b8305023/images/Asian%20Paints%20JSON%20data.jpg)

Upon applying LDA using NLTK and gensim in Python, optimal number of topics were utilized to generate sensible output.
Here is the output for Asian Paints:
![Output](https://github.com/vinaysrivastava273/IIM-Udaipur-NLP/blob/9927e22b387131fba3c1e2114d135ec9b8305023/images/Asian%20Paints%20Output.jpg)
