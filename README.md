
## Project Description

Rent A Cat has been implemented within the Information Systems Development course 2022/23 at University of Liechtenstein. It is meant to be a genuine idea that we turned into something real and thereby gained technical knowledge in both Python and Django.   
  
The goal of this online service is to provide a platform where animal shelters (or private persons) can post their cats and potential adopters can lend ("rent") them for a specific period of time. This facilitates close human-animal engagement and getting to know the cat better, which may result in further lendings or even an adoption. We believe that this concept has beneficial effects on the mental health of people (especially those who cannot permanently own a cat) while obviously also doing something good for the animals.  

![](https://wallpapercave.com/wp/wp3208773.jpg)

## Project Team

|Name|Email|   
|---|:---:|
|Linus Eisele|linus.eisele@uni.li| 
|Abena Nigg|abena.nigg@uni.li| 
|Marie Weinz|marie.weinz@uni.li| 
|Clara Ziche|clara.ziche@uni.li| 


## Motivation
The aim of the project is the practical application and consolidation of the learned methods and technologies from the modules Information Systems Development and Information System Modelling. It is meant to be a genuine idea that we turned into something real and thereby gained technical knowledge in both Python and Django. The goal of this online service is to provide a platform where animal shelters (or private persons) can post their cats and potential adopters can lend ("rent") them for a specific period of time. This facilitates close human-animal engagement and getting to know the cat better, which may result in further lendings or even an adoption. We believe that this concept has beneficial effects on the mental health of people (especially those who cannot permanently own a cat) while obviously also doing something good for the animals.

---

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
---

## Technical Environment

In order to realise our project, we used a simple e-commerce skeleton from [JustDjango](https://justdjango.com/?utm_source=github&utm_medium=logo) that uses (the free version of) a [Bootstrap Template](https://mdbootstrap.com/freebies/jquery/e-commerce/).  
The environment follows a Django-typical structure. The back-end classes `*.py` are located in `core/` where you will e.g. find the entities (`models.py`), the URL patterns (`urls.py`), as well as the views (`views.py`). The entities are stored as classes within a single file (as is typical within Django web development) and we also store our global constants and `Field.choices` in the same file (`models.py`).  
The URL patterns refer directly to the views (functions and classes defined in `views.py`) which can be seen as controllers  rather than just views, since they also contain logic in regard to the data that ought to be displayed in the view. The `context` stores the data that is available for each view and is pre-defined, but may be manipulated by the view classes. The front-end classes `*.html` are located in `templates/` where the UI is generated and filled with the data from the respective contexts.  
The overall software design pattern can therefore be seen as MVT (Model-View-Template). In terms of the more commonly known MVC-Pattern (Model-View-Controller), one could say that the Template in MVT corresponds to the View in MVC, and the View in MVT acts as the Controller in MVC. 

---

## Requirements Engineering
In this section we provide an overview of the functional and non-functional requirements from the relevant stakeholders. The needs of the various stakeholders have been taken into account and listed for the elaboration of the system. The requirements were then classified and organised. 

|Stakeholder|Description|   
|:---|:---|
|Cat enthusiasts |The cat lovers follow the invitation link of the homepage scroll through the page and book their favourite cat| 
|Pet shelter manager|The pet shelter employee follows the invitation link of the homepage and list a new cat, which can be rented| 
|Lecturer |The lecturer expects a software programme which corresponds to the description, and which covers material shown in class. The aim is to see that the students were able to use Python, Django, and Bootstrap. The goals are that students should get better insights into the project flow of software projects| 
|Developers |Get in touch with the programming language Python and the web development framework Django. To increase the programming skills for further challenges. The ideal outcome is that the web app works like the project groups expectations| 

Functional & Non-Functional Requirements
Below is a table with the requirements for the system. The needs of the various stakeholders have been taken into account and listed for the elaboration of the system. The requirements were then classified and organised. 


|Item|Requirement|Description|Type|  
|---|:---|:---|:---|
|1 |Create an account|Users shall be able to view, select, and rent cats|Functional| 
2|Log into an account|Users shall be able to create accounts and log in	Functional|
3|See availability of cats|The overview shall show pictures and the status of availability for each cat|Functional
4|See details of cats |The detail view shall show further details and characteristics about the cat|Functional
5|See overview of rented cats and due date |Users shall be able to see which cat they rented and when it is due to return|Functional
6|See possibility to extend rental date |Users shall be able to extend their rental period to a maximum of x days	|Functional
7|See overview of how cats |Managers should be able to add cats to be rented |Functional
8|Get notified approaching due dates |Email should be sent out to remind users of due dates etc |Functional
9|Get notified of missed deadline |Email notification of missed deadlines|Functional
10|Get notified of new listed cats|Email notification of new listed cats which can be rented |Functional
11|Process of renting|The operations renting a cat and logging into one's account should take no longer than 3 seconds for the application |Non-functional
12|User experience of homepage|All other operations like navigation on the website or selecting a cat should take no longer than 1 second	|Non-functional
13|See details of cats|The cat pictures should all be equally sized and have at least FHD resolution |Non-functional


## Documentation

In this section we provide a description of the most important models and views that we created or altered and give an insight into how they are composed technically as well as how they can be used.
  
### Item (Model)
We have added multiple fields and methods to this entity such as a boolean availability field, attributes of the cat (coat length, gender, size, energy), and pictures. The items have been obviously repurposed into cat entities, though the model has not been renamed since this would have caused additional effort throughout the entire code and database environment.   

### Order (Model)  
The Order model represents an order placed by a user. It has the following relevantfields:

user: a foreign key to the user who placed the order.
ref_code: a character field that represents a reference code for the order.
items: a many-to-many field to the OrderItem objects that are part of the order.
ordered_date: a date-time field that represents the date and time when the order was placed.
rental_duration: an integer field that represents the rental duration for the items in the order.
ordered: a boolean field that indicates whether the order has been placed.

It also has the following methods:

__str__: returns a string representation of the order, in the format self.user.username.
get_total: returns the total cost of the order, which is calculated by adding up the final price of all the OrderItem objects in the order. 
get_rental_duration: returns the rental duration for the items in the order.  

### OrderItem (Model)  
The OrderItem model represents a cat that is part of an order. It has the following relevant fields:

user: a foreign key to the user who added the cat to their order.
ordered: a boolean field that indicates whether the cat has been added to an order.
item: a foreign key to the cat being ordered.

It also has the following methods:

__str__: returns a string representation of the order item, in the format "{self.quantity} of {self.item.title}".
get_total_item_price: returns the hourly rental fee of the order item
get_duration: returns the rental duration of the order item. This is calculated as the rental duration of the associated Order object.
get_final_price: returns the final price of the order item, which is calculated as the product of the item's price and the rental duration. 

### HomeView (View)  
The home page acts as an overview of all cats and provides an interactive UI through various filters. It can be accessed by clicking the *Overview* Button in the top header, but it is also the default home page. Each of the cats can be clicked in order to be referred to a detail page with additional information (see **ItemDetailView**). There are (non-chainable) filtering possibilities for the attributes coat length, size, and energy. The other attributes (gender and availability) are also displayed for each cat and one could easily add filters for them. The filters have been implemented from scratch and pass their input to the view class using a GET request. The view then filters the items and refreshes them accordingly in the context. The filters are not chainable since in Django, an already filtered query cannot be further filtered (due to database performance reasons) and thus a more complicated solution would have had to be chosen for this. The template `home.html` is used in the front-end, where the content design is very scalable: The cats, their attributes, and the filters are all accessed dynamically using the given context.

### ItemDetailView (View) & Product Page (HTML)
The product page extends base.html and overrides the content block. It is used to display the details of our rental cats. The page displays the following information about the cats:

An image of the cat
The cats's name, category, size, label, and gender
The rental fee for the cat
A description of the cat
Any reviews of the cat
Two buttons: one to add the cat to the cart, and another to remove it from the cart
The page also displays additional images of the cat.

The page uses the following variables:

object: the cat being displayed
item: an object that represents an instance of the Item model, which has additional information about the cat (such as its size, label, and gender)

### CheckoutView (View)  
The checkout page is called by clicking the *PROCEED TO CHECKOUT* button from the order summary (*Cart*). It has been redesigned to provide an interface where the user can select a time period where they would like to request the cat(s). This has been implemented from scratch and no external libraries have been used (only for styling). This means we use the basic `datetime-local` HTML input and parse the format manually. The front-end uses the template `checkout.html`. Before entering anything, the *From:* and *To:* dates already initialise according to the soonest / latest possible booking. Users can select their preferred time and date in the calendar that appears when clicking the calendar icon. The input is submitted instantly upon selection in order for the calendar widget to immediately adapt the possible choices. This means that, after choosing a *From:* date, the eligible *To:* dates should already respond to the chosen date according to the shortest / longest lending duration. The duration is therefore calculated within the view and there are some checks in place in case the user circumvents the workflow design.  
>TODO the checkout page further contains... (order summary, pricing, address?)


---

## [Example Workflow](https://scribehow.com/page/Documentation__Rent_a_Cat__WkY23ShXQUylnEWIjB6kKw)

<!--
<iframe 
src="https://scribehow.com/embed/How_to_request_a_Booking__jenAy8kZTAa_eJQoD1-c-w" 
width="100%" 
height="640"
frameborder="0">
</iframe>
-->

---

## Database Management

The web-based administrator interface lies at `http://.../admin` where superusers can observe all current instances of entities, change them, or create new ones. If changes are made to the entity classes themselves (in `models.py`), [Django migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/) have to be run afterwards in order for the changes to reflect in the database.


