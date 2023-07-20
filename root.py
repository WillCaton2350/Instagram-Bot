from Bot import instagramBot

if __name__ == "__main__":
    insta = instagramBot()
    insta.login()
    counter = 5
    while counter > 0:
        for i in range(counter):
            insta.search()
            insta.select()
            insta.follow_Comment()
        counter +=1
        break
    insta.closeDriver()
    
    