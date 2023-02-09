<h1 align="center">elgit</h1>

<div align="center">The simplest tool for deferred commits</div><br/>

<p align="center">
    <img src="https://img.shields.io/badge/-zero--dependencies-blue">
    <img src="https://img.shields.io/badge/license-MIT-green">
</p>

## Download
```bash
git clone https://github.com/thenesterov/elgit.git
```
or
```bash
wget https://github.com/thenesterov/elgit/raw/master/elgit.py
```

Then make it executable:
```bash
chmod +x elgit.py
```

## How to use?
To print help, use the `-h` or `--help` flag:
```bash
./elgit.py -h
```

To commit right now:
```bash
git add .
./elgit.py -m "Commit message"
```

To commit later, you can use the following flags:
- `--minutes`
- `--absminutes`
- `--hours`
- `--abshours`
- `--days`
- `--absdays`
- `--months`
- `--absmonths`
- `--randtime`

## Examples
Commit in N (e.g. 3) minutes/hours/days/months:
```bash
./elgit.py -m "Elgit commit" --minutes 3
```
```bash
./elgit.py -m "Elgit commit" --hours 3
```
```bash
./elgit.py -m "Elgit commit" --days 3
```
```bash
./elgit.py -m "Elgit commit" --months 3
```

Commit to a specific (absolute) value of minutes/hours/days/months:
```bash
./elgit.py -m "Elgit commit" --absminutes 3
```
```bash
./elgit.py -m "Elgit commit" --abshours 3
```
```bash
./elgit.py -m "Elgit commit" --absdays 3
```
```bash
./elgit.py -m "Elgit commit" --absmonths 3
```

You can combine flags:
```bash
./elgit.py -m "Elgit commit" --hours 1 --absminutes 30
```

You can also specify a random time value:
```bash
./elgit.py -m "Elgit commit" --days 1 --randtime
```
