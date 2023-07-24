from Bot import instagramBot

if __name__ == "__main__":
    insta = instagramBot()
    insta.login()
    insta.popup()
    counter = 5
    for i in range(counter):
        insta.viewStory()
    counter += 1
    insta.closeBrowser()