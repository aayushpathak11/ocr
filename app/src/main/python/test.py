import yake
def extract(text):
    kw_extractor = yake.KeywordExtractor(top=6)
    keywords = kw_extractor.extract_keywords(text)
    t=""
    for i in keywords:
        t=t+"/"+i[0]
    return t