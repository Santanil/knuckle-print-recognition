import re

# this file is use to parse config files for environment related things
class ParseConfig:
    def __init__(self):
        # configuration file for settings
        # other setup variables will be added later
        self.lines =""
        self.configs = {}
        with open("setup.config",'r') as setupfile:
            self.lines = setupfile.readlines()

        for line in self.lines:
            line = line.strip()
            if self.IsNameValuePair(line):
                key,value = self.GetNameValuePair(line.strip())
                self.configs[key] = value

    def IsNameValuePair(self,line):
        return re.match(r'(.*)\s*=\s*(.*)',line)

    def GetNameValuePair(self,line):
        param, value = re.compile(r'\s*=\s*').split(line,2)
        var_name = param.strip()
        value = value.strip()
        return var_name,value
