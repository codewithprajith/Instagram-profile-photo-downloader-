import instaloader

app = instaloader.Instaloader()
user_name = input("User name:")
app.download_profile(user_name, profile_pic_only=True)