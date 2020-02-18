# chrometabs
Write your favorite URLs in JSON format and open all of them Google Chrome with one command (For OSX only).

# Usage
Make sure you have Python 2.7 installed.

Run the tool by passing a JSON file with your URLs:

``` shell
python src/chrometabs.py tabs/demo.json
```

demo.json:
```
{
    "gmail" : "https://mail.google.com/mail/u/0/#inbox",
    "whatsapp": "https://web.whatsapp.com/",
    "8tracks" : "http://8tracks.com/",
    "netflix" : "http://www.netflix.com/"
}
```

You can also pass a folder, it will search for all JSON files recursively:

``` shell
python src/chrometabs.py tabs/
```

# Author
Jorge Victoria
