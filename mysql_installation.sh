#!/bin/sh

# reading from user location of local package
echo Please input the location of mysql rpms
read location

## installing 
cd $location
yum localinstall mysql-commercial-client*.rpm mysql-commercial-common-*.rpm mysql-commercial-icu-data-files*.rpm  mysql-commercial-libs*.rpm mysql-commercial-server-*.rpm

## changing the open file limits
sed -i "s/LimitNOFILE.*/LimitNOFILE = 65535/" /usr/lib/systemd/system/mysqld.service
systemctl daemon-reload


## optimizing my.cnf
MEMORY=`free | grep Mem | awk '{print $2}'`
MEMORY=$((MEMORY*0.7))

## inquring server id for the server
echo Enter server id for the server
read SERVER_ID

cnf="
[client] 
socket=/data/mysql/mysql.sock 

[mysqld]
event_scheduler=OFF
sql_mode = STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
character_set_server=latin1
collation_server=latin1_swedish_ci
default_authentication_plugin=mysql_native_password
datadir=/data/mysql
socket=/data/mysql/mysql.sock
default_storage_engine=innodb


open_files_limit=65535

innodb_buffer_pool_size=$MEMORY
innodb_buffer_pool_instances=24
innodb_log_buffer_size=1G
key_buffer_size=64M
innodb_change_buffer_max_size=30
#innodb_log_file_size=512M
innodb_flush_log_at_trx_commit = 2
innodb_redo_log_capacity = 1073741824


max_connections=2000
transaction-isolation = READ-COMMITTED
skip-name-resolve
max_allowed_packet = 256M
tmp_table_size = 512M
max_heap_table_size = 512M
#long_query_time = 120
#slow_query_log = 1
#slow_query_log_file = /data/mysql/database-slow.log

innodb_flush_method=O_DIRECT

# tablespace--
innodb-file-per-table



# Replication Configuration
disable-log-bin
server-id = $SERVER_ID
#binlog-format = mixed
#max_binlog_size = 512M
#expire_logs_days = 7
#log_bin = /data/binlog/mysql-bin
relay-log = mysql-relay-bin
#log-slave-updates = 1
#slave-skip-errors=1062
read-only = 1
#skip_slave_start

# AuditLogConfiguration
#server_audit_logging = ON
#server_audit_file_path = /data/AuditLog/audit.log
#server_audit_file_rotate_size = 536870912
#server_audit_file_rotations = 10
#server_audit_output_type = 'FILE'

slave_load_tmpdir=/data/tmp
tmpdir=/data/tmp

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

"

echo "$cnf" > /etc/my.cnf


