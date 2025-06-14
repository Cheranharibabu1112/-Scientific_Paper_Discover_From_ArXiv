import gradio as gr
import arxiv

def search_arxiv(q):
    """
    Searches arXiv for papers based on the user's input query.
    Returns up to 5 relevant papers, or a message if no results are found.
    """
    if not q or not q.strip(): # Check if the query is empty or just whitespace
        return "Please enter a research topic or keywords to search for."

    try:
        # Perform the search using the arxiv library
        # max_results: Limits the number of papers returned
        # sort_by: Sorts results by relevance to the query
        search = arxiv.Search(
            query=q,
            max_results=5, # You can adjust this number as needed
            sort_by=arxiv.SortCriterion.Relevance
        )

        results = []
        # Iterate through the search results and format each paper
        for result in search.results():
            paper = f"**{result.title}**\n\n{result.summary}\n\n🔗 {result.entry_id}"
            results.append(paper)

        if not results:
            return f"No papers found for '{q}'. Please try a different query or broader keywords."
        
        # Join all formatted paper strings with a clear separator
        return "\n\n---\n\n".join(results)

    except Exception as e:
        # Basic error handling for issues with the arXiv API or network
        print(f"An error occurred during the arXiv search: {e}")
        return "Sorry, an error occurred while searching arXiv. Please try again later."

# Create the Gradio interface
demo = gr.Interface(
    fn=search_arxiv, # The function to call when the user interacts
    inputs=gr.Textbox(label="Enter your research topic or keywords"), # Input field for the query
    outputs=gr.Markdown(label="Search Results"), # Output area, rendered as Markdown
    title="General arXiv Paper Search", # Title of the Gradio app
    description="Enter any research topic, keywords, or even a paper title to search arXiv. "
                "Get instant access to academic papers from various fields like physics, "
                "mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering and systems science, and economics."
)

# Launch the Gradio application
# This line is essential for the Gradio app to run and be accessible
demo.launch()
