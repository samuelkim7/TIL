// 스파크의 덧셈 연산
val df = spark.range(500).toDF("number") //0~499까지의 값이 할당된 500 row의 df 생성
df.select(df.col("number")+10).take(10)  //각 로우에 10을 더함

// scala에서 스파크 데이터 타입 사용
import org.apache.spark.sql.types._

val b = ByteType

// DataFrame 생성
val df = spark.read.format("json")
  .load("c:/SparkDG/data/flight-data/json/2015-summary.json")

//스키마 출력
df.printSchema

//column 생성: col 함수 사용
import org.apache.spark.sql.functions.{col, column, expr}
col("someColumnName")
expr("someColumnName2")  // expr 함수에 인수로 컬럼 표현식을 넣으면 col 함수와 동일하게 사용 가능

//row 생성 및 데이터 접근. row 생성시 df와 같은 순서로 값을 명시해야 함
import org.apache.spark.sql.Row
val myRow = Row("Hello", null, 1, false)

myRow.getString(0)
myRow.getInt(2)
