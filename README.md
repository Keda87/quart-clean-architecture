# Quart Clean Architecture
Todo API implemented on [Quart](https://pgjones.gitlab.io/quart/) using clean architecture.

##### Prerequisite.
- Python 3.7
- PostgreSQL
- Docker

##### Run the project.
Ensure postgresql is started and create the database.
```bash
$ mv .env.example .env       # Then update the content with your own.
$ docker-compose up --build  # Open in port 5000.
$ docker-compose run api alembic upgrade head  # Run db migration.
```


#### TODO:

- [x] Web API.
- [ ] Validate and sanitize request payload.
- [ ] API Documentation.
- [ ] Unit/Integration test.
