# Uchuu (Universe) database

```
> TCP Server		- (to listen the commands)
> SQLite database	- (to CRUD the data)

Request		>	+------------+
			| TCP Server |
			| +--------+ |
			| | SQLite | |
			| +--------+ |
Response	<	+------------+
```

#### Start

```bash
$ python3 run.py
$ nc localhost 8888

> Hello
```

#### TODO
- [ ] Database Access
	- [x] Server
	- [ ] I/O (CLI)
- [ ] Database Structure
	- [ ] Pages
	- [ ] Model Groups
	- [ ] Models
