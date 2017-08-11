# chatbotApp
Chatbot Demo App

ChatbotApp  captures key aspects of AI with features sure as:

I. Intelligent chatting
II. Image recognition(IMR) for upload document(for release in the beta version)

Note: Any changes to the code must be done in the virtualenv which include the installed libraries.

Set up:

1. Clone the repository
2. Run:  source chatterbotenv/bin/activate
3. This takes you into your chatterbotenv
4. cd into ChatbotApp folder
5. Run: Python manage.py runserver 0.0.0.0:8000
   Note: this can be changed via ALLOWED_HOSTS = ['*'] in the settings under uploads folder for the production environment
6. Open the bot in the browser via 0.0.0.0:8000
7. Once down, use 'deativate' command to exit the chatterbotenv



Contributions welcome. 
TODO: 

1. On the upload of documents:
   i.   Files can be in pdf format and needs to be converted to jpeg/jpg
   ii.  Tensorflow IMR using convoluted neural networks should be able to identity the validity of the verify the file uploaded and chat back on wether it the actual document or not.

2. Payment systems to be incorporated.

3. Login to capture email of the user

4. Mailgun to send back information to the user regarding the app and if payment is made, the completed transaction details.


UseCase:
a.) This app when completed can be used in advertisement.
b.) The part on chatbot(third on the alerts) can be modified to answer inquiries
c.) The upload can take in a file for advert and verified it. This is stored as part data in the media folder.




