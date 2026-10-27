def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "Oliver",
    "Kivelä",
    job="Application Developer",
    city="Helsinki",
    favorite_language="Python"
)

print(user_profile)
