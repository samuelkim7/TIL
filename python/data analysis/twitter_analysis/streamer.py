from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credentials
import json
import csv

# 주어진 키워드에 대한 실시간 트윗을 받아서 csv 파일로 저장
class Streamer(StreamListener):

    # 객체 생성시 authentication 처리
    def __init__(self):
        self.auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        self.auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    # twitter streaming API에 연결 및 filter 적용
    def stream_with_filter(self, list):
        stream = Stream(self.auth, self)
        stream.filter(track=list)

    # 전송받은 tweet의 내용을 출력하고 csv 파일에 저장
    # 기존 method overriding
    def on_data(self, data):
        try:
            data = json.loads(data)
            tweets = data['text'].encode(encoding='utf-8')
            print(tweets)
            with open("tweets.csv", 'w') as file:
                writer = csv.writer(file)
                writer.writerow(tweets)
            return True
        except BaseException as e:
            print("에러 발생: %s" % str(e))
        return True

    # overriding. 에러 발생시 호출됨
    def on_error(self, status):
        if status == 420:
            # rate limit 발생시 data 함수에 False를 반환
            return False
        print(status)

if __name__ == "__main__":

    list = ["donal trump", "joe biden"]
    streamer = Streamer()
    streamer.stream_with_filter(list)
