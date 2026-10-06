# Docker Quick Reference

| Task | Command |
|---|---|
| List running containers | `docker ps` |
| List all containers | `docker ps -a` |
| List images | `docker image ls` |
| Inspect container | `docker inspect CONTAINER` |
| View recent logs | `docker logs --tail 100 CONTAINER` |
| Read-only process list | `docker top CONTAINER` |
| Build from current directory | `docker build -t local-example:dev .` |

Inspect image provenance and configuration; avoid privileged mode and unnecessary host mounts. `docker rm` and `docker system prune` change or delete resources—review targets first. See [Containers](../Containers/).
