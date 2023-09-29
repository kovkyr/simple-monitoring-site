# simple-monitoring-site

Monitor your devices by icmp echo (ping) grouped by squads.

### Installation

* Update Django secret key, database password, superadmin password and time zone in `.env` file:
```
SECRET_KEY=secret_key
DB_PASSWORD=123456
SUPERUSER_PASSWORD=admin
TIME_ZONE=Asia/Yekaterinburg
```

* Create and run app:
```
make docker-create
```

* Restart app:
```
make docker-restart
```

* Get help:
```
make help
```

Go to http://localhost:3000/admin and create your squads with devices

Go to http://localhost:3000/ to view devices ordered by squads

Go to http://localhost:3000/table to view devices in table format

### Review

- Add devices grouped by squads:

  <img src=".readme/1.gif" width="544" height="306">

- Set priority to change squads order in views:

  <img src=".readme/2.gif" width="544" height="306">

- Switch between card and table views:

  <img src=".readme/3.gif" width="544" height="306">

- View detail information about device:

  <img src=".readme/4.gif" width="544" height="306">

- Fill detail information about devices:

  <img src=".readme/5.gif" width="544" height="306">

