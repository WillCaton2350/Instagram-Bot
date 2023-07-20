from Bot import instagramBot

if __name__ == "__main__":
    insta = instagramBot()
    insta.login()
    insta.popup()
    counter = 5
    for i in range(counter):
        insta.search()
        insta.select()
        insta.follow_Comment()
    counter += 1
    insta.closeDriver()


    
    