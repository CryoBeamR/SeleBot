from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import os
import time

def import_instructions(filename = "resources/instructions.txt"):
    with open(filename) as file:
        instructions = dict()
        actions = []
        params = []
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        config =  lines[0].split()
        for line in lines[1:]:
            line_arg = line.split()
            actions.append(line_arg[0])
            params.append(line_arg[1:])
        instructions["ip"] = config[1:]
        instructions["actions"] = actions
        instructions["params"] = params
    return instructions
            
class SeleBot:
    def __init__(self, instructions, ip):
        self.instructions = instructions
        self.HOSTADDRESS = ip
        print(f'SeLeBot starting ... ')
        options = wd.ChromeOptions()
        ext_path =  os.path.abspath("resources/Phantom.crx")
        print(ext_path)
        options.add_extension(ext_path)
        self.wd = wd.Remote(f"http://{self.HOSTADDRESS}:4444", options=options)
        print(f'Startup completed.')

    def init(self):
        self.cmd_dict = {
            "clk" : self.click,
            "wrt" : self.write,
            "brw" : self.browse,
            "sw" : self.switch_window,
            "gpt" : self.get_page_title,
            "gpc" : self.get_current_page_url,
            "w" : self.wait,
            "iw" : self.imp_wait
        }
    def execute_instructions(self):
        """
        Execute all instructions receive written by the user
        """
        self.init()
        print(f"Executing {len(self.instructions['actions'])} instruction{'s.' if len(self.instructions) > 1 else '.'}")
        actions = self.instructions['actions']
        params = self.instructions['params']
        for (cmd, arg) in zip(actions, params):
            self.cmd_dict[cmd](arg=arg)
        self.wd.quit()
        print("All instructions executed succesfully" if len(self.instructions['actions']) > 1 else "Instruction executed succesfully ")

    def click(self, elem_link="", arg=[]):
        """
        Simulate a click on a html element
        
        - elem_link: need to be a XPath to a element
        """
        x_path = elem_link
        if len(arg) > 0 :
            x_path = arg[0]
        try:
            element = self.wd.find_element(By.XPATH, x_path )
            self.wd.execute_script("arguments[0].click();", element)
        except Exception as e:
            self.wd.quit()
            raise e


    def write(self, elem_link="", text="", arg=[]):
        """
        Simlate key stroke in html element that accept typing
        
        - elem_link: need to be a XPath to a element
        - text: text that will be type in the element 
        """

        x_path = elem_link
        text_content = text
        if len(arg) > 0 :
            x_path = arg[0]
            # add "" verification !
            text_content = " ".join(arg[1:])[1:-1]
        try:
            passwd_confimation_input = self.wd.find_element(By.XPATH,x_path)
            passwd_confimation_input.send_keys(text_content)
        except Exception as e:
            self.wd.quit()
            raise e

    def browse(self, link="", arg=[]):
        """
        Browse the page specify in the link 

        -link: url of the page  
        """
        url = link
        if len(arg) > 0 :
            url = arg[0]
        try:
            self.wd.get(url)
        except Exception as e:
            self.wd.quit()
            raise e

    def switch_window(self, position=-1, arg=[]):
        """
        Swith the focus of the bot to another window

        - position: the position of the window/tab
        use negative nuumber to count backward and positive for forward 
        """
        index = position
        if len(arg) > 0 :
            index = int(arg[0])
        try:
            self.wd.switch_to.window(self.wd.window_handles[index])
        except Exception as e:
            self.wd.quit()
            raise e
            
    def get_page_title(self, printIsOn=False, arg=[]):
        """
        Return title of the last page browse
        
        - printIsON: need to set to True to print title in terminal
        """
        if len(arg) > 0 :
            printIsOn = arg[0] == 'True'
        if printIsOn:
            print(self.wd.title)
        try:
            title = self.wd.title
        except Exception as e:
            self.wd.quit()
            raise e
        return title

    def get_current_page_url(self, printIsOn=False, arg=[]):
        """
        Return url of the last page browse
        
        - printIsON: need to set to True to print url in terminal
        """
        if len(arg) > 0 :
            printIsOn = arg[0]
        if printIsOn:
            print(self.wd.current_url)
        try:
            current_url = self.wd.current_url
        except Exception as e:
            self.wd.quit()
            raise e
        return current_url
        
    
    def wait(self, sec=0, date=datetime.now(), arg=[]):
        """
        Stop the bot for sec amount of time or until date is reach.
        if params sec and date are given sec is prioritize
        
        - sec: amount of sec that the bot wait
        - date: the date the bot is going to wait until
        """
        diff_date :timedelta =   date - datetime.now()
        laps_time = sec if sec > 0 else diff_date.total_seconds()
        if len(arg) > 0 :
            if arg[0] == "-d":
                diff_date :timedelta =  datetime.fromisoformat(arg[1]) - datetime.now()
                print(datetime.fromisoformat(arg[1]))
                print(datetime.now())
                print(f"diff : {diff_date} sec")
                laps_time = laps_time if laps_time > 0 else (diff_date.total_seconds()-1)
            else:
                laps_time = float(arg[0])
        print(f"Execution pause at {datetime.now().strftime('%H:%M:%S')}")
        try:
            time.sleep(laps_time)
        except Exception as e:
            self.wd.quit()
            raise e
        print(f"Execution continu at {datetime.now().strftime('%H:%M:%S')}")
    
    def imp_wait(self,sec=0, arg=[]):
        """
        Define the amount of time the bot have to wait after 
        a element to load
        """
        laps_time = sec
        if len(arg) > 0 :
            laps_time = float(arg[0])
        try:
            self.wd.implicitly_wait(laps_time)
        except Exception as e:
            self.wd.quit()
            raise e    
        

instructions = import_instructions()
ip = instructions["ip"][0]
bot = SeleBot(instructions,ip)
bot.execute_instructions()
