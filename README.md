# Charles Server

## Requirements

- Postgres
- Elasticsearch

## Variables

[Charles Elasticsearch Variables](https://github.com/sugarush/charles-elasticsearch#variables)

## Installation

- `git clone https://github.com/sugarush/charles-server.git`
- `cd charles-server`
- `pip3 install -r .requirements`
- `cp charles-server-dist.service /etc/systemd/system/charles-server.service`
- `vim /etc/systemd/system/charles-server.service`
- `systemctl start charles-server.service`
