
from gpt_researcher import GPTResearcher
import asyncio
from openai import OpenAI
from tavily import TavilyClient
from dotenv import load_dotenv
import os


load_dotenv()

# Initialize clients with API keys
# client = OpenAI(api_key=os.getenv("GROQ_API_KEY"))

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY"),
# )

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

async def get_report(query: str, report_type: str) -> str:
    # import pdb; pdb.set_trace()
    researcher = GPTResearcher(query, report_type, source_urls=['https://www.fool.com/investing/2025/01/20/nvidia-stock-investors-great-news-from-wall-street/'], complement_source_urls=True)
                            #    document_urls=['https://s201.q4cdn.com/141608511/files/doc_financials/2024/q4/1cbe8fe7-e08a-46e3-8dcc-b429fc06c1a4.pdf'])
    research_result = await researcher.conduct_research()
    # print("done research/n")
    # print("research result", research_result)
    report = await researcher.write_report()
    # report1 = await researcher.write_report_conclusion(report)
    return report
    # return "Done"

if __name__ == "__main__":
    
    com = 'Nvidia'
    competitors = ['nvidia', 'Intel']
    # The company with ticker symbol {com} has two key competitors: {competitors[0]} and {competitors[1]}.
    # query = f'''
    #     Collect comprehensive information on at least 15 {com} product/service launches in 2024 from {com}.
    #     Ensure the data includes exactly 15 or more products/services. For each product, provide the following details:
    #     - Launch Date
    #     - Product/Service Features and Specifications
    #     - Target Market and Demographics
    #     - Initial Market Reception (100 words)
    #     - Market Share and Capture in Relevant Segment (100 words)
    #     - Competitive Positioning Against Similar Products (100 words)
    #     - Post-Launch Updates and Developments
    #     Ensure that the data is up-to-date and presented clearly for accurate financial analysis.
    #     '''
    query = f'''
    Give detailed financial report of the company {com}.
    '''
    report_type = "research_report"
    
    report = asyncio.run(get_report(query, report_type))
    print(report)
    f = open('NVIDIA_report.md','w')
    f.write(report)
    print(len(report.split(' ')))
 