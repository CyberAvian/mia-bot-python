import requests


class Search():
    def get_result(self, query):
        result = requests.get("http://api.duckduckgo.com",
                        params = {
                            "q": query,
                            "format": "json",
                            "no-html": 1
                        })
        data = result.json()
        text = self.format_result(data)
        return text

    def format_result(self, search_result):
        abstract = search_result["Abstract"]
        related_topics = search_result["RelatedTopics"]

        if abstract != "":
            source = search_result["AbstractSource"]
            url = search_result["AbstractURL"]
            text = f"From: {source} at {url}\n{abstract}"
        elif len(related_topics) > 0:
            print(related_topics)
            abstract = related_topics[0]["Text"]
            url = related_topics[0]["FirstURL"]
            text = f"\tFrom: {url}\n\t{abstract}"
        else:
            text = ""
        return text


if __name__=='__main__':
    search = Search()
    result = search.get_result("What time is it?")
    print(result)
