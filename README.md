# xClean

xClean is a python script that cleans tweets via a list of id placed in a text file.

The script with the free version of X api (ex-twitter), cleaned up nearly 5,000 tweets in just a few days, free of charge.

## Installation

1. install tweepy via pip
```Shell
root@pocketvince:~/xclean# pip3 install tweepy
```
2. Download script xclean.py
3. Edit API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET 
4. Insert tweet id in a file named id.txt (one id per line)
5. Run the script

## Usage

```Shell
root@pocketvince:~/xclean# cat id.txt 
1837471053523603476
1837471079880597543
1837471105017106898
1837471130275258416
1837471154606412032
root@pocketvince:~/xclean# python3 xclean.py 
Tweet 1837471053523603476 successfully deleted.
Tweet 1837471079880597543 successfully deleted.
Tweet 1837471105017106898 successfully deleted.
Tweet 1837471130275258416 successfully deleted.
Tweet 1837471154606412032 successfully deleted.
```
## Contributing
https://www.makeareadme.com/

## Extra info
I wanted to use https://tweetdeleter.com/ & https://tweetdelete.net/ to clean multiple x-accounts.

The accounts were quite old and well overloaded, but the services were paid for, and doing it manually would have taken too much time.

By using the api & tweepy, the problem was quickly solved. 
