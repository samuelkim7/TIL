*elasticsearch 공식 reference*에서 정리함 ([링크](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html))

### 실행
- elasticsearch의 bin folder 내에서
```sh
elasticsearch.bat
```
- 새로운 node 실행 (각각 새 cmd 창에서)
```sh
.\elasticsearch.bat -E path.data=data2 -E path.logs=log2
.\elasticsearch.bat -E path.data=data3 -E path.logs=log3
```
- 클러스터 상태 확인
```sh
curl -X GET "localhost:9200/_cat/health?v&pretty"
```

### Indexing Documents
1) document 생성 (Kibana console)
```sh
PUT customer/_doc/1"
{
  "name": "John Doe"
}
```
2) 대량의 document를 한번에 indexing (cmd에서 .json file의 위치로 이동 후)
```sh
curl -H "Content-Type: application/json" -XPOST "localhost:9200/bank/_bulk?pretty&refresh" --data-binary "@accounts.json"
```
- 현재 저장된 indices 확인
```sh
curl "localhost:9200/_cat/indices?v"
```

### Searching
1) sorting한 후 모든 결과 출력
```sh
GET /bank/_search
{
  "query": { "match_all": {} },
  "sort": [
    { "account_number": "asc" }
  ]
}
```
2) field 내에 특정 term이 있는 document 검색
```sh
GET /bank/_search
{
  "query": { "match": { "address": "mill lane" } }
}
```
