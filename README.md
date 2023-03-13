# README #

ScispaCy-NER is a Python package containing spaCy models for processing biomedical, scientific or clinical text. More information on this source can be found [here](https://allenai.github.io/scispacy/).

### How do I get set up? ###

A Dockerfile is provided to run in a docker container. 
Use the following scripts to build and run:

```
build.sh
run.sh
```

### Run ###

To test the try this: 

```
curl --location --request POST 'https://mediverse-api.medinet.net.au/NER/parse' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'apikey: 9snQx9kw0fiSZvsPdMVY7plqIllT5YZo' \
--data-raw '{"text":"The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient'\''s nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."}'
```

Expect this:

```
{
    "text": "The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.",
    "entries": [
        {
            "entity": "congestion",
            "start": 62,
            "end": 72,
            "label": "DISEASE"
        },
        {
            "entity": "perioral cyanosis",
            "start": 237,
            "end": 254,
            "label": "DISEASE"
        },
        {
            "entity": "Tylenol",
            "start": 345,
            "end": 352,
            "label": "CHEMICAL"
        },
        {
            "entity": "p.o",
            "start": 387,
            "end": 390,
            "label": "CHEMICAL"
        },
        {
            "entity": "respiratory congestion",
            "start": 492,
            "end": 514,
            "label": "DISEASE"
        },
        {
            "entity": "albuterol",
            "start": 637,
            "end": 646,
            "label": "CHEMICAL"
        },
        {
            "entity": "diarrhea",
            "start": 836,
            "end": 844,
            "label": "DISEASE"
        },
        {
            "entity": "His bowel movements",
            "start": 846,
            "end": 865,
            "label": "DISEASE"
        }
    ]
}
```