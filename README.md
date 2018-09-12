
Objectos-en-espanol Documentation

Overview
This application will take an uploaded image and translate the name of the object within the image into Spanish. The purpose of this application is to provide a user with a way to translate the name of an object into Spanish by using only an image. In order to confirm the project behaves as we expected, we will upload an image to our application, translate the name of the pictured object, and compare the outputs of the application with the expected result.

Constraints
We will create this application using the Google Cloud API, specifically the Google Translate API and Google Vision API
The language to be used in this project will be python.
There will be a development team of five members.
The application must run on Google Cloud.

Functional Specifications
The program shall be able to allow a user to upload an image of an object.
The program shall only accept image formats such as .jpg and .png.
The program shall be able to determine what object is displayed in the picture and store the data.
The program shall be able to translate the name of the object into spanish and display it to the user.

How to Use
Clone from git using the following command: 
git clone https://github.com/GrayTurtle/objectos-en-espanol.git

Go into the directory using the following command:
cd objectos-en-espanol

Upload image to the images folder

Install python dependencies requests, json, base64, and sys if they are not preinstalled using the following command:
pip install <dependency-name>
If the above does not work, use:
sudo pip install <dependency-name>

In the objectos-en-espanol folder, run the following command:
./objectos-en-espanol.py <image-name.extension>

View output in console


Use Cases/Basic Flow
A user uploads an image of an object by typing the image file on the command line. The program then identifies the object using the Google Vision API and stores the name of the object. The program then translates the name of the object into Spanish using the Google Translate API and displays it to the user on the command line.

User Stories
As a user, I can translate the name of an object by using a picture of the object allowing me to communicate across language barriers.
As a user, I can use the application to identify between two similar objects preventing confusion during translation.


Test Cases/Acceptance Tests
Test Case 1
Title: 
Image identification and translation
Description: 
A user should be able to successfully upload an image to Objectos en Espanol and receive a name of the object in the image in both English and Spanish.
Precondition: 
The user must have the Git repository objectos-en-espanol cloned to local device.
Assumption: 
A terminal or command prompt is being used. User has uploaded image into /objectos-en-espanol/images folder on local device. Image has one main focus item to be identified.
Test Steps:
Navigate to folder /objectos-en-espanol in terminal
Type the command ‘./objectos-en-espanol.py <image_name>’
Press Enter
Expected Result/Acceptance: 
The object name in both English and Spanish should show up in the terminal. This object should be present in the pre-uploaded image.
Test Case 2
Title: 
File not in directory
Description: 
A user should receive an error if the file called is not present in objectos-en-espanol/images.
Precondition: 
The user must have the Git repository gray-turtle/objectos-en-espanol cloned to local device.
Assumption: 
A terminal or command prompt is being used. File name being called does not exist in objectos-en-espanol/images.
Test Steps:
Navigate to folder /objectos-en-espanol in terminal
Type the command ‘./objectos-en-espanol <filename>’
Press enter
Expected Result/Acceptance: 
A user should receive a ‘No such file or directory’ error if the file is not located in objectos-en-espanol/images.
Test Case 3
Title: 
File is not an image
Description: 
A user should receive an error if the file called is not an image or supported image file.
Precondition: 
The user must have the Git repository gray-turtle/objectos-en-espanol cloned to local device.
Assumption: 
A terminal or command prompt is being used. File name being called is not an image or supported image file.
Test Steps:
Navigate to folder /objectos-en-espanol in terminal
Type the command ‘./objectos-en-espanol <filename>
Press Enter
Expected Result/Acceptance: 
A user should receive a “Error: Bad Image” error if the file is not an image or supported image file.
Test Case 4
Title: 
No filename provided
Description: 
User runs script without providing a filename
Precondition: 
The user must have the Git repository objectos-en-espanol cloned to local device.
Assumption: 
A terminal or command prompt is being used. 
Test Steps:
Navigate to folder /objectos-en-espanol in terminal
Type the command ‘./objectos-en-espanol.py’
Press Enter
Expected Result/Acceptance: 
The Python script returns an ‘IndexError: list index out of range’ error because the code asks for a second argument but it does not exist in the command.





