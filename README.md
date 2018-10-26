# dotdotdown

`dotdotdown` - The Directory Traversal Downloader


## HOW TO INSTALL

```bash
$ pip install -r requirements.txt
```

OR

```
$ python setup.py install
```

## COMMAND LINE

```bash
$ python cli.py


    .___      __      .___      __      .___
  __| _/_____/  |_  __| _/_____/  |_  __| _/______  _  ______
 / __ |/  _ \   __\/ __ |/  _ \   __\/ __ |/  _ \ \/ \/ /    \\
/ /_/ (  <_> )  | / /_/ (  <_> )  | / /_/ (  <_> )     /   |  \\
\____ |\____/|__| \____ |\____/|__| \____ |\____/ \/\_/|___|  /
     \/                \/                \/                 \/

        Author: MyKings Version: 0.1.0/20181026

===========================================================================

usage: dotdotdown [-h] [-u URL] [-o OUTPUT_DIR] [--file-ext FILE_EXT]
                  [--dir-depth DIR_DEPTH] [-l {info,debug,warning,error}]
                  [--timeout TIMEOUT] [--max-try-count MAX_TRY_COUNT]
                  [--proxy-socks PROXY_SOCKS] [--enable-proxychains4]

optional arguments:
  -h, --help            show this help message and exit

Options Group:
  -u URL, --url URL     The url address to download.
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory.
  --file-ext FILE_EXT   Only allowed file extensions, default(*.*)
  --dir-depth DIR_DEPTH
                        The maximum depth of the directory, the default is 0
                        is not limited
  -l {info,debug,warning,error}, --log-level {info,debug,warning,error}
                        Set the log level, default:(info)
  --timeout TIMEOUT     HTTP request timeout, default:(5s)
  --max-try-count MAX_TRY_COUNT
                        Maximum number of attempts to connect after timeout,
                        default:(5)
  --proxy-socks PROXY_SOCKS
                        Set requests to use the socks proxy,
                        format:"socks5://127.0.0.1:1080"

```

## HOW TO USE

```bash
$ python cli.py -u http://99.248.235.4/Library/  --proxy-socks socks5://127.0.0.1:1080 --log-level debug


    .___      __      .___      __      .___
  __| _/_____/  |_  __| _/_____/  |_  __| _/______  _  ______
 / __ |/  _ \   __\/ __ |/  _ \   __\/ __ |/  _ \ \/ \/ /    \
/ /_/ (  <_> )  | / /_/ (  <_> )  | / /_/ (  <_> )     /   |  \
\____ |\____/|__| \____ |\____/|__| \____ |\____/ \/\_/|___|  /
     \/                \/                \/                 \/

        Author: MyKings Version: 0.1.0/20181026

===========================================================================

[2018-10-26 15:45:46] [INFO] Start analyzing http://99.248.235.4/Library/ ...
[2018-10-26 15:45:47] [DEBUG] Found 34 a tag links and started parsing links...
[2018-10-26 15:45:47] [DEBUG] Start testing "http://99.248.235.4/Library//**DO%20NOT%20RUN%20SAMPLES%20ON%20YOUR%20HOST%20COMPUTER!%20USE%20A%20VIRTUAL%20MACHINE**" url ...
```