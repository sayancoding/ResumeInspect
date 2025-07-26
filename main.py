import asyncio

from utils.VectorStore import VectorStore




async def main():

    jd = """
Requirements
Proficiency in Java and its frameworks such as Spring, Hibernate, and JUnit
Strong understanding of RESTful APIs, data modeling concepts, and integration patterns
Knowledge of database systems including SQL, and scripting capabilities with Python and Bash
Background in data ingestion, transformation, ETL/ELT pipelines, and workflows
Experience with Git or other version control systems in Agile development environments
Skills in problem-solving, troubleshooting, and analytical reasoning
Familiarity with AWS services such as EC2, S3, and Lambda

Nice to have
Understanding of big data technologies like Apache Kafka and Apache Spark
Knowledge of containerization tools such as Docker and Kubernetes
Awareness of data governance, security, and quality standards
Familiarity with Snowflake data warehousing and query optimization techniques
Showcase of certifications in service-based frameworks like AWS or Java
"""

    """JD & Resume embedding and storing at vector DB (FAISS)"""
    vs = VectorStore()
    await vs.store_Jd_as_Vector(jd)
    # await vs.store_resume_as_Vector('./data/resume.pdf')

    from crews.JdExtractCrew import JdExtractCrew
    from crews.ResumeExtractCrew import ResumeExtractCrew 
    from crews.MatcherCrew import MatcherCrew

    """Parse / Extract info from Resume"""
    resume_response = ResumeExtractCrew().crew.kickoff()
    print(resume_response)

    """Parse / Extract info from JD"""
    jd_response = JdExtractCrew().crew.kickoff()
    print(jd_response) 
    
    """Matching both JD and resume and analyzing"""
    match_response = MatcherCrew().crew.kickoff(inputs={'resume_output': str(resume_response.raw), 
                                                 'jd_output': str(jd_response.raw) })
    print(match_response) 

if __name__ == "__main__":
    asyncio.run(main())



