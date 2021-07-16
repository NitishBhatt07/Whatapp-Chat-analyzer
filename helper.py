import pandas as pd
from wordcloud import WordCloud
import emoji
from urlextract import URLExtract
from collections import Counter

extract = URLExtract()


def fetch_stats(selected_user ,df):
    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['messages']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_msg = df[df['messages'] == '<Media omitted>\n'].shape[0]

    # fetch number of links
    links = []
    for msg in df['messages']:
        links.extend(extract.find_urls(msg))

    return num_messages,len(words),num_media_msg,len(links)


def fetch_most_busy_users(df):
    x = df['users'].value_counts().head()
    df = round((df['users'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'name','users':'percent'})
    return x , df


def create_word_cloud(selected_user,df):
    f = open("stop_hinglish.txt", 'r')
    stop_words = f.read()

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    temp = df[df['users'] != "group_notification"]
    temp = temp[temp['messages'] != "<Media omitted>\n"]

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    temp['messages'].apply(remove_stop_words)

    wc = WordCloud(width=500,height=500,min_font_size=10 ,background_color='white')
    df_wc = wc.generate(temp['messages'].str.cat(sep=" "))

    return df_wc


def most_common_words(selected_user,df):
    f = open("stop_hinglish.txt", 'r')
    stop_words = f.read()

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    temp = df[df['users'] != "group_notification"]
    temp = temp[temp['messages'] != "<Media omitted>\n"]

    words = []
    for messsge in temp['messages']:
        for word in messsge.lower().split():
            if word not in stop_words:
                words.append(word)

    return_df = pd.DataFrame(Counter(words).most_common(20))
    return return_df


def emoji_counter(selected_user,df):
    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    emojis = []
    for message in df['messages']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df


def monthly_timeline(selected_user,df):
    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['messages'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline


def daily_timeline(selected_user,df):
    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    daily_timeline_df = df.groupby(['only_date']).count()['messages'].reset_index()

    return daily_timeline_df


def week_activity_map(selected_user ,df):
    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user,df):
    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user,df):
    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name',columns="period",values='messages',aggfunc='count').fillna(0)

    return  user_heatmap














