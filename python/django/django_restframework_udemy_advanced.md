### Setup
#### Docker
- Docker is an open platform for developing, shipping, and running applications.
- Docker provides the ability to package and run an application in a loosely isolated environment called a container.
- Containers are lightweight because they don’t need the extra load of a hypervisor, but run directly within the host machine’s kernel.

#### Travis-CI
- CI: Continuous Integration is the practice of merging in small code changes frequently. The goal is to build healthier software by developing and testing in smaller increments.
- When you run a build, Travis CI clones your GitHub repository into a brand-new virtual environment, and carries out a series of tasks to build and test your code.
- Travis-CI will run our unit tests and linting Every time you push a change to GitHub.

#### Postgres
- docker-compse.yml 수정
- requirements.txt에 psycopg2 추가
- Dockerfile 수정
- $ docker-compose build
- app folder의 settings.py 내 DATABASES 설정 변경
- wait_for db command
