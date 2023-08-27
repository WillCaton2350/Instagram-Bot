from main import webDriver

if __name__ == "__main__":
    func = webDriver()
    func.startDriver()
    func.getBrowser()
    func.login()
    counter = 5
    for i in range(counter):
        func.search()
        func.select()
    counter += 1
    func.closeDriver()