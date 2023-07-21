from Bot import instaBot, autoGui

if __name__ == "__main__":
    GuiFunc = autoGui()
    func = instaBot()
    func.login()
    func.popup()
    func.createPost()
    func.cadMethod()
    func.textAreaField()
    GuiFunc.xClose()
    counter = 1
    for i in range(counter):
        func.search()
        func.select()
        func.savePost()
    counter +=1
    func.closeBrowser()
    