import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ProfileReport } from '../model/profileReport.interface';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private httpClient:HttpClient){}

  getWelcome():Observable<any>{
    let url = "http://localhost:8000/api/welcome"
    return this.httpClient.get(url);
  }

  uploadResume(file:File):Observable<any>{
    const url = "http://localhost:8000/api/uploadResume"
    const formData = new FormData()
    formData.append("file",file)

    return this.httpClient.post(url,formData);
  }

  uploadJD(jd:String):Observable<any>{
    const url = "http://localhost:8000/api/uploadJd"
    return this.httpClient.post(url,jd);
  }

  getMatchingProfile():Observable<any>{
    const url = "http://localhost:8000/api/matching"
    return this.httpClient.get(url)
  }

  getDummyData():ProfileReport{
    const report:ProfileReport = {
  "score": 66,
  "matches": [
    "Candidate's 3.5+ years of experience is close to the minimum 4 years required.",
    "Strong match in Core Java, Multithreading, JUnit, and Git.",
    "Candidate's experience with Spring Boot, Kafka, AWS, GCP, Docker, Microservices, and Event-Driven Architecture are significant assets, aligning with modern Java backend development.",
    "Candidate has experience with Angular (in self-projects), which partially matches the AngularJS requirement."
  ],
  "areaOfImprovement": [
    "Experience: Candidate needs about 6 months to 2.5 years more experience to fully meet the JD's range.",
    "UI Skills: Lack of explicit professional experience with AngularJS, HTML, CSS, and JSON as primary skills, and no mention of Espresso.",
    "Framework Specifics: Explicitly mentioning MVC architecture in their professional summary or project descriptions would strengthen the match.",
    "Agile/Scrum: Explicitly stating experience with Agile/Scrum methodologies in the professional summary or work experience.",
    "Location: The candidate's current location (West Bengal) does not match the job location (Bangalore), requiring relocation."
  ],
  "applyRecommendation": "moderate",
  "scoreBreakdown": [
    "Experience: 20/30 points (Candidate is just below the minimum requirement, high priority).",
    "Primary Skills: 31/40 points (Excellent match on core Java, multithreading, testing, and version control; gaps in specific UI technologies and explicit mention of MVC/Agile).",
    "Secondary Skills: 15/20 points (Strong set of modern backend technologies that are highly valuable for a Java developer role, even if not perfectly aligned with JD's 'nice to have').",
    "Location: 0/10 points (No match on location, very low priority)."
  ]
}
    return report;
  }
}
