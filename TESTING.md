# Testing 

Back to the [README.md](README.md)

## Testing Schedule

### Test Case 001 

### Python Validation - PEP8 

Python testing was done by using the [PEP8 Online](http://pep8online.com/). All python files were entered into this online checker and no errors were found in my custom code. However it did raise a few errors in my settings file but this is to do with django auth code and could not be updated. 

Results can be found here: 
* Wholebeans folder 
   * [asgi.py](docs/testing%20/PEP8-HS-asgi.png)
   * [settings.py](docs/testing%20/PEP8-HS-settings.png)
   * [urls.py](docs/testing%20/PEP8-HS-urls.png)
   * [views.py](docs/testing%20/PEP8-HS-views.png)
   * [wsgi.py](docs/testing%20/PEP8-HS-wsgi.png)
* Coffee folder 
   * [admin.py](docs/testing%20/PEP8-R-admin.png)
   * [apps.py](docs/testing%20/PEP8-R-apps.png)
   * [forms.py](docs/testing%20/PEP8-R-forms.png)
   * [models.py](docs/testing%20/PEP8-R-models.png)
   * [urls.py](docs/testing%20/PEP8-R-urls.png)
   * [views.py](docs/testing%20/PEP8-R-views.png)

### Test Case 002
![Test Case 002](docs/testing/css-validation.png)

### CSS Validation 

Custom CSS has been validated using [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/).
It passed. However some warnings were raised but these were to do with extensions and Google fonts. 

![CSS Validation Screenshot](docs/testing/css-validation-screenshot.png)

### Test Case 003 
![Test Case 002](docs/testing/html-testing-report.png)

On the website I made I used the dev tools to copy the rendered html code and pasted in into this validator. It returned no errors using the Nu HTML checker.  

### Test Case 004 

All JavaScript code was tested using the Beautify tool Javascript validator and returned no errors. 

### Test Case 005

### Manual testing 

All users can view the home page, view all coffee recipoes, search recipes, have the choice to sign up or login. All nav buttons were tested and work well. Once i checked it was working on a desktop, I did the same on my iphone and all nav functions also performed well. 

I also checked the registered user CRUD functionality, which allows users to add, edit or delete recipes. It also allows them to see all of the recipes they have created once they're logged in. 

I then made sure it looked well from a SuperUser perspective as they have access to more items. When logged in as a superuser, there will be an extra tab called 'Moderate Recipes', meaning the superuser can view a list of recipes that have been submitted for approval with the choice to edit them or delete. All functions performed well. 

### Wave Webaim Accessibility Report 

[Wave WebAim](https://wave.webaim.org/) was used to do an evaluation of the accessibility of the website. 

The full report can be found [here](https://wave.webaim.org/report#/https://wholebeans.herokuapp.com/)

### Lighthouse report 

Testing performed well on Lighthouse for desktop devices: 

![Lighthouse Screenshot for Desktop](docs/testing/lighthouse1.png)

It did not perform as well for mobile. However this is to do with django, bootstrap, cloudinary and font awesome., 

![Lighthouse Screenshot for Mobile](docs/testing/lighthouse2.png)


Back to the [README.md](README.md)





