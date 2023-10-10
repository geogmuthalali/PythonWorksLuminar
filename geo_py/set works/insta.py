all_users=["sachin","rahul","rohit","kohli","dravid","laxman","ganguly"]
sachin_followers=["rahul","ganguly","dravid"]
sachin_sugg=set(all_users).difference(set(sachin_followers))
sachin_sugg.remove("sachin")
print(sachin_sugg)