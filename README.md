# flask.net
# amirhosein heidari 

creating a flask app so .net can intract with it without user 
the data.json file contains radius of few circles like this

after calling the main function it will create a server that can be called with browser and has 3 functions

1-call the main window of server

2-use (/square/<int:num>) to calculate square of any given number

3-to call third function you can use (/circle)

    it will run jsond_.py file and calculate the area of given circles

    ---data.json before 
    {
    "circles": [
        { "radius": 5 },
        { "radius": 10 },
        { "radius": 3 },
        { "radius": 1 },
        { "radius": 90 },
        { "radius": 13 },
        { "radius": 563 }
    ]
    }

    ---data.json after
    {
        "circles": [
            {
                "radius": 5,
                "area": 78.53975,
                "circumference": 31.4159
            },
            {
                "radius": 10,
                "area": 314.159,
                "circumference": 62.8318
            },
            {
                "radius": 15,
                "area": 706.85775,
                "circumference": 94.2477
            }
        ]
    }