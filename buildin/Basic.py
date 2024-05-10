#from buildin.Chrome import ChromeList
ChromeList = {
  "Ctrl + n": ["open", "new", "window"],

  "Ctrl + Shift + n": ["Open", ["new", "window"], "incognito"],

  "Ctrl + t": ["open", "new", "tab"],

  "Ctrl + Shift + t": [
    ["Reopen", "open", "go to"],
    ["previously", "previous"],
    ["tab", "tabs"],
  ],

  "Ctrl + Tab": [["open", "jump", "go to"], "next", ["tab", "tabs"]],

  "Ctrl + Shift + Tab": [
    ["jump", "open"],
    ["previous", "last"],
    ["tab", "tabs"],
  ],

  "Alt + Home": [["open", "go to"], ["home"], ["tab"]],
  "Ctrl + w": ["close", ["current", ""], "tab"],
  "Ctrl + Shift + w": ["close", "current", "window"],
  "Alt + f4": [
    ["close", "exit", "leave"],
    ["chrome", "window"],
  ],

  "Alt + f": [["open", "show", "find", "where"], "chrome", "menu"],
  "Ctrl + Shift + b": [
    ["show", "hide", "open", "close"],
    ["bookmark"],
    ["tab", "window"],
  ],

  "Ctrl + Shift + o": [["open", "show"], ["bookmark"], "manager"],

  "Ctrl + h": [["show", "open"], ["history"], ["page", "tab"]],

  "Ctrl + j": [
    ["open", "show", "where"],
    ["download", "downloads"],
    ["page", "tab", ""],
  ],

  "Shift + Esc": [["open", "show"], ["chrome"], ["task", "manager"]],

  "Ctrl + Shift + j": [["show", "open"], "developer", "tools"],

  "Ctrl + Shift + Delete": [
    ["clear", "clean"],
    "browsing",
    ["history", "data"],
  ],

  "Ctrl + p": ["print", ["page", "pdf"], "current"],
}

class Trash_Parce:

    @staticmethod
    def check_if_any_in_str(lis: list, st: str):
#[1,2,3,4,5] #Q = "ARTTT" =>FALSE
#[1,2,3,4,5] #Q = "1hwiejh2eg" =>TRUE
        for i in lis:
            if i in st:
                return True
        return False

    @staticmethod
    def check_if_all_in_str(lis: list, st: str):
#["hii","my","name"] #Q hii my sajan==>FALSE
#["hii","my","name"] #Q hii my name is sajan==>True
        for i in lis:
            if type(i) is list:
                if not Trash_Parce.check_if_any_in_str(i, st):
                    return False
            else:
                if i not in st:
                    return False
        return True
#Q = open new tab
def ChromeCode(query):
    for _, lists in ChromeList.items():
        A = Trash_Parce.check_if_all_in_str(lists, query)
        if A:
            return _
    return False