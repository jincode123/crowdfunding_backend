# Crowdfunding Back End
{{ your name here }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- Home Page
    - Featured fundraiser
- Search page
    - Search specific fundraiser
-Create New Fundraiser Page
    - Form with fundraiser details
    - Ability to submit
    - Nice error pages for validation

- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}
- Display Fundraiser
    - Shows all information about fundraiser

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL         | HTTP Method | Purpose                              | Request Body                  | Success Response Code | Authentication/Authorisation |
| ----------- | ----------- | ------------------------------------ | ----------------------------- | --------------------- | ---------------------------- |
| fundraisers | GET         | Fetch all the fundraisers            | N/A                           | 200                   | NONE                         |
| fundraisers | POST        | Create a new fundraiser              | JSON Payload                  | 201                   | Any logged in user           |
| pledges     | GET         | Fetch all the pledges                | N/A                           | 200                   | NONE                         |
| pledges     | POST        | Create a new pledge for a fundraiser | JSON Payload{"fundraiser_id"} | 201                   | Any logged in user           |


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )# crowdfunding_backend
![]( database.drawio.svg)
