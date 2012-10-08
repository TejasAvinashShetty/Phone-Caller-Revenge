#designed to win the battle

from twilio.rest import TwilioRestClient
import random
import time



account_sid = "ACc0e75e90f9f1440371f0bf2477518ec5"
auth_token = "692eab25fc25a93889c59d8a7c980bff"
phoneNumber = "+19027012138"
numAnnoying = 10
jillNumber = "+19022937775"
testNumber = "+19028802143"
annoyingRoot = "http://twimlets.com/message?Message%5B0%5D=https%3A%2F%2Fs3.amazonaws.com%2Fannoying%2Fmusic%2F"
jillInterval = 57600
def main():
    client = TwilioRestClient(account_sid, auth_token)
    jill = Caller(jillNumber,numAnnoying,jillInterval,annoyingRoot,client)
    #test = Caller("+19028802143",numAnnoying,180,annoyingRoot,client)

    while True:
       # test.execute(False)
        jill.execute(False)
        time.sleep(60)


class Caller:


    def __init__(self,number,numSong,interval,songRoot,client):
            self.client = client
            self.number = number
            self.numSong = numSong
            self.interval = interval
            self.songRoot = songRoot
            self.randInterval = random.randint(1,self.interval)+time.time()
    def execute (self,override):

        currTime = time.time();
        if (currTime<self.randInterval or override):
            songNumber =str( random.randint(1,self.numSong))
            call = self.client.calls.create(to=self.number,  # Any phone number
                                       from_=phoneNumber, # Must be a valid Twilio number
                               url= self.songRoot+songNumber+".mp3&" )
            print call.sid
            self.randInterval = random.randint(1,self.interval)+time.time()

if __name__ == "__main__":
        main()
