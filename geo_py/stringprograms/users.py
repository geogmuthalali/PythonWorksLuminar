tweets="What a game,hats off boyh teams . well done @benstrokes38 @patcummins30 you have bought test cricket back to life. Love test cricket @TheBarmyArmy @CricketAus @ECB_cricket"
words=tweets.split(" ")
for w in words:
    if w.startswith('@'):
        print(w)