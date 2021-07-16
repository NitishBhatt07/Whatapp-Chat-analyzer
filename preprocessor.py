import re
import pandas as pd

def preprocess(data):
    pattern = '\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'messages_date': dates})

    # convert messages_date to date time type
    df['messages_date'] = pd.to_datetime(df['messages_date'], format='%d/%m/%y, %H:%M ')
    df.rename(columns={'messages_date': 'date'}, inplace=True)

    # extraction the am pm from user_message
    ampm = []
    msg = []
    for messasge in df.user_message:
        ampm.append(messasge.split("-")[0])
        msg.append(messasge.split("- ")[1])

    df['ampm'] = ampm
    df['user_message'] = msg

    # separate users and messages
    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['users'] = users
    df['messages'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # timeline
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date

    df['day_name'] = df['date'].dt.day_name()

    # for heatmap
    period = []
    for hour in df[['day_name','hour']]['hour']:
        if hour == 12:
            period.append(str(hour) + "-" + str('1'))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period'] = period
    df['period'] = df['period'] + df['ampm']

    return df



















