# 0x02 - Bash Redirections
This repository contains the files of Linux Fundations, which focuses on the management of Shell on Linux
This folder is about:

* Commands like head, tail, find, wc, sort, uniq, grep, and tr
* Working with special characters
* Reversing strings
* Concatenating files

# Tasks
**0-hello_world**  
Write a script that prints “Hello, World”, followed by a new line to the standard output.

```
julien@ubuntu:/tmp/h$ ./0-hello_world 
Hello, World
julien@ubuntu:/tmp/h$ ./0-hello_world | cat -e
Hello, World$
julien@ubuntu:/tmp/h$ 
```
**1-confused_smiley**  
Write a script that displays a confused smiley "(Ôo)'.

```
julien@ubuntu:/tmp/h$ ./1-confused_smiley 
"(Ôo)'
julien@ubuntu:/tmp/h$ 
```

**2-hellofile**
Display the content of the /etc/passwd file.

Example:


```
$ ./2-hellofile
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
_lp:*:26:26:Printing Services:/var/spool/cups:/usr/bin/false
_postfix:*:27:27:Postfix Mail Server:/var/spool/postfix:/usr/bin/false
_scsd:*:31:31:Service Configuration Service:/var/empty:/usr/bin/false
_ces:*:32:32:Certificate Enrollment Service:/var/empty:/usr/bin/false
_mcxalr:*:54:54:MCX AppLaunch:/var/empty:/usr/bin/false
_krbfast:*:246:-2:Kerberos FAST Account:/var/empty:/usr/bin/false
$
```







## Getting Started
Each script execute it with the following syntax:

```
$ ./script_name
```

# Prerequisites
* Ubuntu 14.04 LTS - Operating system reqd.

## Author

* **Juan Felipe Bustamante** - *Initial work* - [Github](https://github.com/jfbm74)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* A whole staff of Holberton School, my mentors and peers.
