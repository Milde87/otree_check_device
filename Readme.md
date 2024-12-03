# Device Detection Integration for oTree 5

This document provides instructions for integrating a device detection 
feature into an oTree app. 
This implementation detects whether participants are using a desktop or 
another device and redirects them to specific pages if they do not meet the device requirement.

## Installation
- Copy the provided ```check_device.js``` script into your _static folder.
- Create the required redirect templates:
    - ```_static/global/redirects/redirect_device.html```
    - ```_static/global/redirects/redirect_device2.html```



## Setup
### Define the Player Field
Add a ```device``` field in the ```Player``` class to store the detected device type:

```python
class Player(BasePlayer):
    device = models.StringField()
```    
    
### Add Pages
Define the pages and include logic for device-based redirection in the ```__init__.py```:

```python
class MyPage(Page):
    @staticmethod
    def live_method(player, data):
        if data['type'] == 'device':
            player.device = data['device']


class redirect_screenout(Page):
    template_name = '_static/global/redirects/redirect_device.html'

    @staticmethod
    def is_displayed(player: Player):
        return player.device != 'Desktop'


class redirect_screenout2(Page):
    template_name = '_static/global/redirects/redirect_device2.html'

    @staticmethod
    def is_displayed(player: Player):
        return player.device != 'Desktop'


class Results(Page):
    pass


page_sequence = [MyPage, redirect_screenout, redirect_screenout2, Results]
```

### Frontend Integration
In the template for MyPage, include the check_device.js script to detect the device type on the client side:

```html
{{ block scripts }}
    <script src="{% static 'check_device.js' %}"></script>
{{ endblock }}
```

## Usage
- Participants accessing the ````MyPage```` are automatically checked for their device type.
- Non-desktop users are redirected to the appropriate screenout pages (````redirect_screenout```` and ````redirect_screenout2````).
- Desktop users proceed to the ````Results```` page.


## Help
If you have any questions, please feel free to contact me via my [homepage](https://www.studies-services.de/en).
