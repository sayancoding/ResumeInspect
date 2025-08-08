from pydantic import BaseModel
from typing import List

class ResumeInfo(BaseModel):
    name:str
    jobTitle:str
    yearsOfExperience:str
    primarySkill:List[str]
    secondarySkill:List[str]
    workingExperience:List[str]
    awardAndCertification:List[str]

class JobRequirementInfo(BaseModel):
    jobTitle:str
    jobFamily:str
    yearsOfExperience:str
    primarySkill:List[str]
    secondarySkill:List[str]
    location:List[str]
    othersInfo:List[str]

class ProfileMatchingReport(BaseModel):
    score:int
    matches:List[str]
    areaOfImprovement:List[str]
    applyRecommendation:str
    scoreBreakdown:List[str]


