![Wholebeans](docs/images/banner.png)

<h1 align=center>Wholebeans!!</h1>

<h2 align=center>Introduction</h2>

<p align=center>Wholebeans is a website for coffee lovers dedicated to sharing, creating and interacting with coffee recipes and baristas from all around the world. Whether you are just getting into coffee or are a professional barista, wholebeans is the one stop place for all coffee related recipes. <br><br>
Browse through loads of different coffee recipes and even add your own! You can also comment and like other recipes to show your support. This website if perfect for anyone who is trying coffee from a new roaster or origin and is not sure how to diall it in for the perfect cup of coffee. Fear not, simply use the search bar to find a similar recipe for the coffee/wholebean you plan to use. <br><br> Users can now search through different recipes that have already been added to the site and registered users can create, update, edit and delete recipes from the website and via the admin panel. <br><br> Wholebeans has been buiot using the Django framework in python, HTML and CSS, and provides user authentication and full CRUD functionaility for recipes </p>

[Visit the live site on Heroku](https://wholebeans.herokuapp.com/)

![Multi Devive Website Mockup Generator Screenshot](docs/images/responsive-screenshot.png)


## UX - User Experience Design 

## The Strategy Plane
<hr>

### Concept 

This project has created as part of the [Code Institute's](https://codeinstitute.net/) Diplome in Full-Stack Software Development. The aim of this project is to create a full-stack that will show the skills I have gained in HTML, CSS and Javascript. 

The main purpose of this website is to provide a platform for like minded coffee connoisseurs who are looking for inspiration to brew the best coffee they can while being able to create and add their own recipes. A superuser will be able to approve, edit and delete user recipes in order to manage the content on the website. 

<h3>Site goals</h3>

* Create a platform that allows users to post their favourite coffee and share their thoughts as comments under posts. 
* The website is designed to be intuitive and easy to navigate. 
* The website was designed to be responsive and to meet all screen sizes. 
* The website should focus on the display of the posts/recipes and present in a convenient way. 
* The website should appeal to both at home coffee drinkers but also professional baristas acting as a a coffee community hub. 

### User Stories

<strong>As a normal site user:</strong>

* I can search the website to find different recipes using keywords. 
* I can see the view all page to see all recipes. 
* I can view the comments of the registered users. 
* I can select a coffee recipe if i wish to see more detail on it.

<strong>As registered user:</strong>

* I can register for a wholebeans account to allow me to access all of the functions throughout the website. 
* I can create and share my own coffee recipes to other users to see. 
* I can edit my recipes if i decide to change them. 
* I can delete my recipe if i dont like it anymore. 
* I can comment on other users recipes to give my thoughts. 
* I can like recipes to show my support for other users. 

<strong>As a SuperUser:</strong>

* I can create draft posts if i dont have time to finish the post. 
* I have the power to approve other users recipes before they are posted. 
* I can edit other users recipes. 
* I can delete other users recipes. 
* I have access to the backend django admin system. 

<strong>Agile Methodology</strong>

I managed this projects functions and development through GitHubs projects Kanban board: 

[Wholebeans Coffee Recipes - USER STORIES](https://github.com/users/AdamVictory/projects/1)

<h3>Scope</h3>

* The website should be functional, easy to naviagte and intuitive. 
* The frontend should present the content clearly. Visually appealing. 
* Users to manipluate their content (CRUD). 
* Allow logged in users to interact with other posts through comments. 
* Search - all users can use the search bar to quickly find recipes. 
* Comments and Likes - Users can comment and like other posts. 
* Users can sign in and sign out to view the website from differnet perspectives. Also can register for an account. 
* Custom 404 & 500 pages for good UI. 
* Use bootstrap to make the site responsive, and custom CSS and Java script. 
* Create a webpage application using the django framework. 


## The Structure Plane 
<hr>

<p>Wholebeans, will have four distint pages for first time users.</p>

  * Home page, Coffees, Register, Login, 

<p>Users without an account can navigate through these four pages and will be able to see the details of each coffee recipe. However they will not be able to add their own recipes or like/comment with other users until the have signed up. 

When the user creates an account and is logged in, the following pages will be displayed.</p>

* Home page, coffees, Logout and my recipes. 

<p>Logged in usera will be able to access all of the sites pages. They can access all the details of each recipe while being able to interact with them. 
They will also be able to access all of their recipes, to add new posts, edit old obnes or delete them.</p>


## The Structure Plane 
<hr>

## Functional Scope 

### Flowchart 

![Wholebeans Flowchar]()

## Database Schema 

I created two custom models for this website. This ERD was created using [DrawSQL](https://drawsql.app/home)

![Database Schema](docs/images/databaseschema.png)


## The Skeleton Plane

## Wireframes 

I created the wireframe using [Figma](https://www.figma.com/)

![PICTURE]()
![PICTURE]()

## The Surface Plane

## Design 

### Color Scheme 

![Color Scheme](docs/images/colour-scheme.png)

I kept the colour scheme simple for this project as i didnt want to distract the user too myuch and wanted the focus to be put on the recipe details. 

All colours were generated from using [imagecolorpicker.com](https://imagecolorpicker.com/en). 

### Typography 

Two fonts are used throughout this website. I got them from [Google Fonts](https://fonts.google.comn/). 
'x' was used for the website name and headings and 'x' was used for all other texts. They work well together and create positive contrast. 

![Font example](docs/images/fonts.png)

### Imagery 

I used [Unsplash](https://unsplash.com/) to source imagery for this project. The images are very high quality and give good inspiration for users on the purpose of this website. 

![Background Image](docs/images/background.jpg)

![Placeholder Image](docs/images/placeholder.jpg)

