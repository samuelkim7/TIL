package com.sundogsoftware.sparkstreaming

import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.spark.streaming._
import org.apache.spark.streaming.twitter._
import org.apache.spark.streaming.StreamingContext._
import Utilities._
import java.util.concurrent._
import java.util.concurrent.atomic._
import scala.math.max

// 가장 긴 트윗의 길이를 구하는 프로그램 
object LongestTweet {
  
  def main(args: Array[String]) {

    setupTwitter()
    
    val ssc = new StreamingContext("local[*]", "AverageTweetLength", Seconds(1))
    
    setupLogging()

    val tweets = TwitterUtils.createStream(ssc, None)
    
    val statuses = tweets.map(status => status.getText())
    
    val lengths = statuses.map(status => status.length())
    
    // longestTweet 변수 선언
    var LongestTweet = new AtomicLong(0)
    
    // 각각의 tweet에 대해 길이가 긴 것을 longestTweet에 setting하고 최대값을 출력
    lengths.foreachRDD((rdd, time) => {
      
      LongestTweet.set(rdd.reduce((x,y) => max(x,y) ))
        
        println("LongestTweetLength: " + LongestTweet.get())
      })
    
    var LongestTweetText: String = ""
    var num = 0
    
    // 가장 긴 tweet의 내용 출력하기
    statuses.foreachRDD((rdd, time) => {
      
      LongestTweetText = rdd.reduce((x,y) => 
        if(x.length() >= y.length()) x
        else y
      )
      
      println("LongestTweetText: " + LongestTweetText)
    })
    
    ssc.checkpoint("C:/checkpoint/")
    ssc.start()
    ssc.awaitTermination()
  }  
}
