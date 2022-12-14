from instapy import InstaPy
from instapy.util import smart_run

# Write your automation here
# Stuck? Look at the github page https://github.com/InstaPy/instapy-quickstart

insta_username = "french_anatra"
insta_password = "en mode bg 1998"

dont_like = ["food", "girl", "hot"]
ignore_words = ["pizza"]
friend_list = ["friend1", "friend2", "friend3"]

# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True, want_check_browser=False)
with smart_run(bot):
    bot.set_relationship_bounds(
        enabled=True,
        potency_ratio=-1.21,
        delimit_by_numbers=True,
        max_followers=4590,
        max_following=5555,
        min_followers=45,
        min_following=77,
    )
    bot.set_do_comment(True, percentage=10)
    bot.set_comments(["Cool!", "Awesome!", "Nice!"])
    bot.set_dont_include(friend_list)
    bot.set_dont_like(dont_like)
    bot.set_ignore_if_contains(ignore_words)
    bot.like_by_tags(["dog", "#cat"], amount=100)
    bot.end()
