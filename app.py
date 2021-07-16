import streamlit as st
import matplotlib.pyplot as plt
import preprocessor
import helper
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    # fetch unique users
    user_list = df['users'].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt ", user_list)

    if st.sidebar.button("Show Analysis"):

        # stats Area ...................................................................................
        num_messages , words , num_media_msg , num_links = helper.fetch_stats(selected_user , df)

        st.title('Top Statistics')

        col1, col2, col3, col4 = st.beta_columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_msg)
        with col4:
            st.header("Link Shared")
            st.title(num_links)

        # timeline.........................................................................................
        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig = plt.figure(figsize=(6, 4))  # try different values
        ax = plt.axes()
        ax.plot(timeline['time'],timeline['messages'],color='green')
        plt.gcf().autofmt_xdate()
        st.pyplot(fig)

        # daily timeline
        st.title('Daily timeline')
        daily_timeline_df = helper.daily_timeline(selected_user,df)
        fig = plt.figure(figsize=(6, 5))  # try different values
        ax = plt.axes()
        ax.plot(daily_timeline_df['only_date'], daily_timeline_df['messages'], color='black')
        plt.gcf().autofmt_xdate()
        st.pyplot(fig)

        # activity map........................................................................................
        st.title('Activity Map')
        col1, col2 = st.beta_columns(2)
        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header("Most busy Month")
            busy_month = helper.month_activity_map(selected_user,df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # heatmap............................................................................................
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig ,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)







        # finding the busiest user in group (group level)  ....................................................
        if selected_user == "Overall":
            st.title("Most Busy Users")

            x , new_df = helper.fetch_most_busy_users(df)

            col1, col2 = st.beta_columns(2)

            with col1:
                fig ,ax = plt.subplots()
                ax.bar(x.index,x.values)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # word cloud .........................................................................................
        st.title("Word Cloud")
        df_wc = helper.create_word_cloud(selected_user,df)
        fig ,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words .................................................................................
        st.title("Most Common Words")
        most_common_df = helper.most_common_words(selected_user,df)
        col1, col2 = st.beta_columns(2)

        with col1:
            fig, ax = plt.subplots()
            ax.barh(most_common_df[0], most_common_df[1])
            st.pyplot(fig)
            plt.xticks(rotation='vertical')

        with col2:
            most_common_df = most_common_df.rename(columns={0:'message',1:"count"})
            st.dataframe(most_common_df)

        # emoji analysis........................................................................................
        st.title('Emoji Analysis')
        col1 ,col2 = st.beta_columns(2)

        with col1:
            emoji_df = helper.emoji_counter(selected_user, df)
            emoji_df = emoji_df.rename(columns={0: 'emoji', 1: "count"})
            st.dataframe(emoji_df)

        with col2:
            fig ,ax = plt.subplots()
            fig, ax = plt.subplots()
            ax.pie(emoji_df['count'].head(), labels=emoji_df['emoji'].head(), autopct="%0.2f")
            st.pyplot(fig)








