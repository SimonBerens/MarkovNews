from web_scrape import Source

HEADLINE_SOURCES = {
    "nytimes_heading": Source("https://www.nytimes.com", "h2", "story-heading"),
    "wsj_heading": Source("https://www.wsj.com/", "a", "wsj-headline-link"),
    "npr_heading": Source("https://www.npr.org/sections/news/", "h2", "title")
}

SUMMARY_SOURCES = {
    "nytimes_summary": Source("https://www.nytimes.com", "p", "summary"),
    "wsj_summary": Source("https://www.wsj.com/", "p", "wsj-summary"),
    "npr_summary": Source("https://www.npr.org/sections/news/", "p", "teaser")
}

HEADLINE_JSON = "headline_matrix.json"

SUMMARY_JSON = "summary_matrix.json"
