#### 실행
- elasticsearch의 bin folder 내에서
```sh
elasticsearch.bat
```
- 새로운 node 실행 (새 cmd 창에서)
```sh
.\elasticsearch.bat -E path.data=data2 -E path.logs=log2
```
```sh
.\elasticsearch.bat -E path.data=data3 -E path.logs=log3
```
- 클러스터 상태 확인
```sh
curl -X GET "localhost:9200/_cat/health?v&pretty"
```

### Indexing Documents
```sh
curl -X PUT "localhost:9200/customer/_doc/1" -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'
```
