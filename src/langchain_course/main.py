import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    # print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
    # print(f"GOOGLE_API_KEY: {os.getenv('GOOGLE_API_KEY')}")

    information = """
        Elon Musk
        FRS

        Musk in 2025
        Born	Elon Reeve Musk
        June 28, 1971 (age 55)
        Pretoria, Transvaal,[a] South Africa
        Citizenship	
        South Africa
        Canada
        United States (since 2002)
        Education	University of Pennsylvania (BA, BS)
        Occupations	
        CEO and product architect of Tesla
        Founder, CEO, and chief engineer of SpaceX
        Founder and CEO of SpaceXAI
        Founder and CTO of X Corp.
        Co-founder of Neuralink, The Boring Company, OpenAI, Zip2, X.com and PayPal
        President of the Musk Foundation
        Political party	Independent[b]
        Spouses	
        Justine Wilson
        ​
        ​(m. 2000; div. 2008)​
        Talulah Riley
        ​
        ​(m. 2010; div. 2012)​
        ​
        ​(m. 2013; div. 2016)​
        Partners	
        Amber Heard (2017–2018)
        Grimes (2018–2021)
        Ashley St. Clair (2023–2025)
        Shivon Zilis (until 2026)
        Children	At least 14,[c] including Vivian Wilson
        Parents	
        Errol Musk (father)
        Maye Musk (mother)
        Relatives	Musk family
        Awards	Full list
        Musk's voice
        Duration: 3 minutes and 10 seconds.3:10
        Musk on his main goals for SpaceX and the future of human civilization
        Recorded January 22, 2026
        Signature

            
        This article is part of
        a series about
        Elon Musk
        Personal
        Companies
        Politics
        In the arts and media
        vte
        Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is an industrialist, technologist, and former United States public official who is the chief executive officer and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire (in terms of US dollars) in June 2026; as of November 2026, Forbes estimates his net worth to be $849.7 billion.

        Musk was born into the wealthy Musk family in Pretoria, South Africa. He emigrated to Canada in 1989; he has Canadian citizenship as his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California, United States, to pursue business ventures. In 1995, he co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal. Musk also became an American citizen in 2002.

        In 2002, Musk founded and became CEO and chief engineer of SpaceX, a space technology company. Musk joined Tesla as an angel investor in 2004 and became its CEO and product architect in 2008. In 2015, Musk co-founded OpenAI to advance artificial intelligence (AI) research, but later left; his growing discontent with the organization's direction and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired Twitter, a social networking service, and made significant changes, including rebranding it as X in 2023. His other businesses include Neuralink, a neurotechnology company that he co-founded in 2016, and the Boring Company, a tunneling company that he founded in 2017. In November 2025, Tesla approved a pay package worth $1 trillion for Musk, which he is to receive over 10 years if certain milestones are met, such as achieving a market capitalization of $8.5 trillion. Musk became the first US-dollar trillionaire upon the initial public offering of SpaceX in June 2026, though a SpaceX stock collapse brought him under the threshold by the next month.
        """


    summary_template = """
    given the information {information} about a person , I want you to create 
    1. a short summary
    2. thow interesting Fact about them
    """

    # 1. Create the PromptTemplate Runnable
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # # 2. Initialize the Gemini Chat Model Runnable
    # llm = ChatGoogleGenerativeAI(
    #     model="gemini-3.8-flash",
    #     temperature=0,
    # )
    # 2. Initialize the Gemini Chat Model Runnable
    llm = ChatOllama(
        model="mimo-v2.6:latest",
        temperature=0,
    )

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response.content)



if __name__ == "__main__":
    main()
