# Metaheuristics - Procesamiento de resultados

Con este pequeño programa podemos procesar los resultados asociados a los experimentos realizados en el ámbito de la optimización utilizando metaheurísticas.

## Grupo de trabajo

José Lemus  jose.lemus.r@mail.pucv.cl
Diego Tapia root.chile@gmail.com - diego.tapia.r@mail.pucv.cl

## Publicaciones


## Uso

#### Build image

```
docker build --tag mh-results .
```


#### PostgresSQL Local

```
docker-compose -p "mh-results" -f db/docker-compose.yml up -d
```

#### Import SQL

```
docker cp db/backups/bd_exp.sql mh-results-db:/

psql -h localhost -U db_user -W -d db_name -f /bd_exp.sql
```