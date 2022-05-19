# SELEBOT 🤖🤖

SeleBot a simple bot 🤖

## Description

This a really simple bot that can automate some basic actions on a chrome broswer using Selenium. The idea was the have a simple bot that could be scheduled and do some basic things like click on button, insert text in field ... with the goal of creating a competitive way of getting your hand on a limited article or anything demanding certain action at a certain time.

This project is far from finish I have a lot of thing I would like to experiment.

## Getting Started
* This project run in a docker container that run Selenium so make sure to have [Docker](https://www.docker.com) install on your workspace.

* In ```/resources``` should be a file name ```instruction.txt```. This is your script that need to be executed by the bot to perform certain the actions in ```instruction.txt``` **(refer to ```/ressouces/instruction_demo.txt```)**.

### Commands
* **ip**   
  description : set the local ip address of the container  
  usage : ```ip <your ip adresse>```
* **clk**  
  description : Simulate a click on a html element  
  usage : ```clk <xPath of an html element>```
* **wrt**  
  description : Simulate input in html element that accept typing  
  usage : ```wrt <xPath of an html element>```
* **brw**  
  description : Go the page specify in the link   
  usage : ```brw <url>```
* **sw**  
  description : Swith the focus of the bot to another window (next windows by default)  
  usage : ```sw ```
* **gpt**  
  description : Return title of the last page browse in terminal  
  usage : ```gpt ```
* **gpc**  
  description : Return url of the last page browse in terminal  
  usage : ```gpc ```
* **w**  
  description : Timeout the bot for sec amount of time or until date is reach  
  usage : ```w <your ip adresse>```
* **iw**  
  description : Define the amount of time the bot have to wait after a element so it can load  
  usage : ```iw [-opt] <time>```  
  option :   
  -d : date (ex : 2022-01-06T13:39:00) 
  

### Dependencies

* requests 2.26.0
* selenium 4.1.0
* beautifulsoup4 4.10.0
* pandas 1.3.5


### Executing program

* Change the YOURIPADDRESSE in ```wait-for-grid.sh``` for your ip address
    ex: http://192.168.1.12:4444/status


* Run the docker containers using docker compose
    ```
    docker-compose up
    ```


## Help

Always add the your ip in the first line of the ```instruction.txt``` file  

```
ip 192.168.1.12
```

## Authors
[Roodney Aladin](https://www.linkedin.com/in/aladin-roodney) 

## Version History
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License.
## Acknowledgments

Inspiration, code snippets, etc.
* [README-Template.md](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
