
List all connections
```
airflow connections list
```

`sqlite_default` is the default sqlite connection. View the details
```
airflow connections get sqlite_default
## id | conn_id   | conn_type | descripti | host      | schema | login | password | port | is_encryp | is_extra_e | extra_dej | get_uri    
##    |           |           | on        |           |        |       |          |      | ted       | ncrypted   | son       |            
## ===+===========+===========+===========+===========+========+=======+==========+======+===========+============+===========+============
## 41 | sqlite_de | sqlite    | None      | /tmp/sqli | None   | None  | None     | None | False     | False      | {}        | sqlite://%2
##    | fault     |           |           | te_defaul |        |       |          |      |           |            |           | Ftmp%2Fsqli
##    |           |           |           | t.db      |        |       |          |      |           |            |           | te_default.
##    |           |           |           |           |        |       |          |      |           |            |           | db   
```

Create a new connection named `db_sqlite`
```
airflow connections add db_sqlite \
    --conn-type sqlite \
    --conn-host ~/airflow/airflow.db
```

The newly created connection can be seen in UI: `Admin > Connections` or run `airflow connections get db_sqlite`
```
id | conn_id   | conn_type | descripti | host      | schema | login | password | port | is_encryp | is_extra_e | extra_dej | get_uri    
   |           |           | on        |           |        |       |          |      | ted       | ncrypted   | son       |            
===+===========+===========+===========+===========+========+=======+==========+======+===========+============+===========+============
50 | db_sqlite | sqlite    | None      | /home/air | None   | None  | None     | None | False     | False      | {}        | sqlite://%2
   |           |           |           | flow/airf |        |       |          |      |           |            |           | Fhome%2Fair
   |           |           |           | low/airfl |        |       |          |      |           |            |           | flow%2Fairf
   |           |           |           | ow.db     |        |       |          |      |           |            |           | low%2Fairfl
   |           |           |           |           |        |       |          |      |           |            |           | ow.db
```