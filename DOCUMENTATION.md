# Documentation

## Base URL
Base URL is your localhost


## Overall description
This WEB app is just for fun. We have 2 sections described below:

### Developer career
First section is about Developer career path. From start here is Junior Developer and his available skill set. We are going to observe his promotion by getting new technical skills. He will be promoted to Middle, Senior and Team Lead, once new skills getting achieved. Below parameters to be used for promotion:

```
- Junior level: < 5 skills
- Middle level: => 5 AND < 10 skills
- Senior level: => 10 AND < 15 skills
- Team Lead: => 15 skills
```

### Company growth
Second section is about Company growth. From start here is Startup project with a small team. We are going to observe company growth by increasing team size. We will upgrade our Startup to Small business, Big company, Enterprise and Corporation. Below parameters to be used for upgrade:

```
- Startup: < 2 team members
- Small business: => 2 AND < 4 team members
- Big company: => 4 AND < 7 team members
- Enterprise: => 7 AND < 10 team members
- Corporation: => 10 team members
```


## UI endpoint 
Endpoint to be used to see user interface: 

### UI for Developer career

```
"/dev_ui"
```

### UI for Company growth

```
"/team_ui"
```

## Skills endpoint

### Endpoint to be used for GET, PATCH, DELETE requests: 
```
"/skills/<int:skill_id>"
```
PATH parameter `<skill_id>` to be used to fetch, update or delete skills by its ID. 
#### Usage sample:
* In case if you want to fetch or delete skill by ID, then you will need to use the following endpoint: 
```
/skills/1
```
* In case if you want to update skill then, along with ID you will also need to send JSON body like in below sample:
    * In case if you want to update both values use below body. It will update both values by ID
    ```
    {
        "name": "Django",
        "level": "Beginner"
    }
    ```
    * In case if you want to update only one value use below body. It will update only specified value by ID
    ```
    {
        "name": "Django"
    }
    ```

### Endpoint to be used for GET, POST requests: 
```
"/skills"
```
#### Usage sample:
* In case if you want to fetch or create skills you will need to use the following endpoint: 
```
/skills
```
* In case if you want to create new skill use below body. It will create new skill including skill name and the level with an incrementing ID
```
{
    "name": "Django",
    "level": "Beginner"
}
```

## Teams endpoint

### Endpoint to be used for GET, PATCH, DELETE requests: 
```
"/teams/<int:team_id>"
```
PATH parameter `<team_id>` to be used to fetch, update or delete teams by its ID. 
#### Usage sample:
* In case if you want to fetch or delete team by ID, then you will need to use the following endpoint: 
```
/teams/1
```
* In case if you want to update team then, along with ID you will also need to send JSON body like in below sample:
    * In case if you want to update both values use below body. It will update both values by ID
    ```
    {
        "role": "BA",
        "count": 1
    }
    ```
    * In case if you want to update only one value use below body. It will update only specified value by ID
    ```
    {
        "role": "BA"
    }
    ```

### Endpoint to be used for GET, POST requests: 
```
"/teams"
```
#### Usage sample:
* In case if you want to fetch or create teams you will need to use the following endpoint: 
```
/teams
```
* In case if you want to create new team use below body. It will create new team including team role and count of employees with an incrementing ID
```
{
    "role": "BA",
    "count": 1
}
``` 