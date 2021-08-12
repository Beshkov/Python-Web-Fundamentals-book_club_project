# Python-Web-Fundamentals_final_project


### Initial commit:
* added models;
* added html
* added css
* added aadmin models


### Secondary commit: 09.08.2021 / 16:26
* added two models to Like and Dislike connecting them to the BookEvent Model via ForeighKey. (proably I will have to refactor it down the line)


### commit at 11.08.2021 at this commit :

* Book Changes
* (1) added views on the book app = view book , remove book, add book, edit book;
* (2) changed the Likes to Marks in Book Model;
* (3) added book forms AddBook, EditBook that inherit from the BookForms and added DeleteBooks that inherit and extend the BookForms form;

*  User Profile Changes: 
* (1) EditProfile form that inherit and extend the  main UserProfileForm  - > added functionaliuty remove images from the os. 
* (2) changed the ImageFrield, upload_to from '/media/' to '/user_profile_pictures/'
* (3) changes in views.py : view_profile, edit_profile added  < TODO Need to implement delete and refactor edit profile views.>

* Settings Changes:
* (1) added MEDIA_ROOT

Notes: I need to refactor the user profile and make it authenticate. 

### Changes with the commit at 12.08.2021

#### I had to back up the project and upload reupload the project. Still learing git I guess. /that is kind of irrelevant for the project/

* Changes to user_profiles:
* (1) deleted the old profiles and created  new updated user profiles.
* (2) user profile now is registered by email and password and is extended by profile_image / TODO: implement user profile / 
* (3) implemented new forms, models, urls, signals, auth views, 

* Changes to books and book events 