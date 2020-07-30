url = "https://www.google.com/search?sxsrf=ALeKk01iDEO6oatfM6nq86-lxM51-5tPtQ%3A1594204590653&ei=rqEFX9y5J-SBk74P68ul0A8&q=split%28%29%5B%5D+python&oq=split%28%29%5B%5D+python&gs_lcp=CgZwc3ktYWIQAzIHCAAQFBCHAjICCAAyAggAMgIIADIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBggAEBYQHjIGCAAQFhAeOgQIABBHOgYIABAHEB46CAgAEBYQChAeULkNWNBmYIJqaABwAXgAgAHsBIgBthWSAQsyLjMuMS4yLjAuMpgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjcyMzyur3qAhXkwMQBHetlCfoQ4dUDCAw&uact=5"




def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


print(domain_name(url))
