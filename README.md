# Threat Score
This is going to be an automatic system, which will be personalized based on user.
it will assign threat score to people that come in contact with you and tell you
if they are any threat to you, higher score mean more threat they can be toward you.

# Person Threat Score Criteria

|Reason|Score|
|:----|:----:|
|Say negative stuff about you|1|
|Say negative stuff about thing you do|1|
|Say negative stuff about your religion|1|
|Say negative stuff about your race|1|
|Say negative stuff about your country|1|
|Say negative stuff about your gender|1|
|Jealous of you|0.5|
|want to get things you own|0.5|
|Blocked You|0.5|
|Don`t Reply Your message|0.5|
|Argue Against you|0.5|
|Can have things you own|0.2|

# Implementation
This project will collect data online and from surrounding using several sensors, 
including CCTV camera, your cell phone, conversation help near you, video capture,
or video seen online.

# Data Type
## Text
Text data will be collected online from social media accounts, which will be processed
to see if anything negative about yourself is found or not. More like sentiment analysis.

## Images/Video
Visual data will be collected from social media account/CCTV camera/Video on devices to look for sign of threat 
against yourself.

## Audio
Audio data will be collected from social media accounts/Videos/Audio on devices to look for sign of threat 
against you.

# Results
Final results will be stored in a database, result will show identity of a person, along with threat score and 
reason and timestamp.
Identity of a person can be name, picture, audio or social media account url.
