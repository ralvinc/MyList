# MyList

This is a simple website I made which allows users to keep track of their watch/readlist. 

## Features
CRUD operations: 
- Create new items on the list
  - Add a name, note, action (watch, read, or both), and completed status to each item
- Read items from the list 
- Update items from the list 
- Delete items from the list 

User authentication

![1](https://user-images.githubusercontent.com/126153932/236616999-558a604c-3d28-42d3-be96-d7424cd8439a.png)

![2](https://user-images.githubusercontent.com/126153932/236617002-db83edf5-22e7-402b-a7d6-6195291460ec.png)

![3](https://user-images.githubusercontent.com/126153932/236617007-eb9a4d80-1f7e-4adc-be39-db851beff486.png)


## Installation and Usage

To install this project, download or clone the repository to your local machine: 

    git clone https://github.com/ralvinc/mylist.git

Then, navigate to the project directory and install the dependencies:

    cd mylist
    pip install -r requirements.txt
    
Create a new database by running the following command: 

    python manage.py migrate
    
Create a superuser account by running the following command: 
  
    python manage.py createsuperuser

Start the server by running the following command: 

    python manage.py runserver

Navigate to **http://localhost:8000/** in your web browser to use the website

## Built with

HTML \
CSS \
Python (Django) \
SQLite (default Django database)

## Author
This project was created by **Ralvinc**.

## Acknowledgments
Nunito Sans font from **Google Fonts** \
**Font Awesome**
