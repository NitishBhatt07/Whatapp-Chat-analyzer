
# Whatsapp Chat Analyzer

This is project to analyze the whatsapp chat of two individual persons or for whole group.

## Requirements
- Python3 / Anaconda3
- machine learning libraries installed


## How to Use:

- You need to export any whatsapp chat text file and upload it on this web app.
- You need to select the day time formate of you chat file.
- Then you can visualize the whole chat or any individual person chat.


## Features:
- We can see the most busy user , most used words and other stuffs.
- The one another important feature is we can save all the un saved mobile numbers from the chat list to a excel file and also can download it.


  
## Deployment Demo
- The web app deployed using streamlit on heroku.
- http://whatsapp-chat-analyzer-beta.herokuapp.com/

  
## Screenshots
### Top Statistics
- Show total Message count ,words, media shared,links shared and a timely graph.
![](images/top_stats.png)

### Most busy day and Months
- Show most busy day and month using bar plot.
![](images/activity_map(busy_user_month).png)

### Weekly Activity Map
- Show most busy week days with hours and display it using heatmap.
![](images/weekly_activity.png)

### Most busy Users
- Show most busy users using bar plot and also the message percentage count.
![](images/most_busy_users.png)

### World Cloud
- Show most used words in a world cloud.
![](images/word_cloud.png)

### Most Common words
- Show mostly used words in hbar plot and also the count of word used in chat.
![](images/most_common_words.png)

### Emoji Analysis and Number Extractor
- Show commonly used emoji and their count using the pi-chart
- And also show the number not saved in chat and we can download those numbers in excel file.
![](images/emoji_no_extractor.png)
  
## Referance Taken From
- Mainly this project made by Nitish on youtube channel 
  CampusX and i do some changes on it.
- [Youtube Video Link](https://www.youtube.com/watch?v=Q0QwvZKG_6Q&t=754s)
- [His Github Repo](https://github.com/campusx-official/whatsapp-chat-analysis)
- [His Deployment Demo](https://wca-campusx.herokuapp.com/)
