import arxiv

def get_arxiv_results(query, max_results):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query, 
        max_results=max_results, 
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    results = client.results(search)
    return list(results)

def get_arxiv_message(result):
    summary = result.summary.replace('\n', ' ')
    authors = ', '.join([author.name for author in result.authors]) 
    message = (
        f"<b>Title:</b> {result.title}\n\n"
        f"<b>Authors:</b> {authors}\n\n"
        f"<b>Summary:</b> {summary}\n\n"
        f"<b>URL:</b> {result.entry_id}\n\n"
        f"<b>Pub Date:</b> {result.published.date()}"
    )
    return message

