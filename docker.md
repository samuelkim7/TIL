### basic commands

- exit 상태인 모든 container 삭제
```
docker rm $(docker ps --filter 'status=exited' -a -q)
```
