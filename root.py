from Brute.Bot import WebDriver

if __name__ == "__main__":
    num_iterations = 5
    counter = 0

    func = WebDriver()
    func.startDriver()

    while counter < num_iterations:
        func.startDriver()
        func.openBrowser()
        func.login()
        counter += 1