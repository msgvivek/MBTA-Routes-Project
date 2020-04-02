b={
  "data": [
    {
      "attributes": {
        "color": "003DA5",
        "description": "Rapid Transit",
        "direction_destinations": [
          "Bowdoin",
          "Wonderland"
        ],
        "direction_names": [
          "West",
          "East"
        ],
        "fare_class": "Rapid Transit",
        "long_name": "Blue Line",
        "short_name": "",
        "sort_order": 10040,
        "text_color": "FFFFFF",
        "type": 1
      },
      "id": "Blue",
      "links": {
        "self": "/routes/Blue"
      },
      "relationships": {
        "line": {
          "data": {
            "id": "line-Blue",
            "type": "line"
          }
        },
        "route_patterns": {},
        "stop": {
          "data": null
        }
      },
      "type": "route"
    }
  ],
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "first": "https://api-v3.mbta.com/routes?filter[type]=0%2C1&include=stop&page[limit]=1&page[offset]=0&sort=long_name",
    "last": "https://api-v3.mbta.com/routes?filter[type]=0%2C1&include=stop&page[limit]=1&page[offset]=7&sort=long_name",
    "next": "https://api-v3.mbta.com/routes?filter[type]=0%2C1&include=stop&page[limit]=1&page[offset]=1&sort=long_name"
  }
}
