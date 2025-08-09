import { Component, ChangeDetectorRef } from '@angular/core';
import { ApiService } from '../../service/api-service';
import { CommonModule, UpperCasePipe } from '@angular/common';
import { ProfileReport } from '../../model/profileReport.interface';

@Component({
  selector: 'app-matcher',
  imports: [CommonModule,UpperCasePipe],
  templateUrl: './matcher.html',
  styleUrl: './matcher.css',
})
export class Matcher {
  selectedFile: File | undefined;
  isFileUploaded = false;
  jd: String = '';
  report: ProfileReport[]  = [];
  matchingReportsErr: any = 'ResumeErr';
  isMatchingTrigger = false;
  hasMatchingReport = false;
  buttonText = "Match & Score 🎉"
  dummyReport:ProfileReport | undefined

  constructor(private apiService: ApiService,private cdr: ChangeDetectorRef) {
    this.dummyReport = apiService.getDummyData()
  }

  onMatching() {
    if (true) {
      this.isMatchingTrigger = true;
      this.hasMatchingReport = false;
      this.apiService.getMatchingProfile().subscribe({
        next: (data) => {
          this.report = data
          console.log('Data received:', this.report);
        },
        error: (error) => {
          console.error('Error fetching data:', error);
        },
        complete: () => {
          console.log("Completed")
          this.isMatchingTrigger = false;
          this.hasMatchingReport = true;
          this.cdr.detectChanges();
        },
      });
    } else {
      console.log('Prerequisites are not provided!!');
    }
  }

  onJdChange(jd: String) {
    this.jd = jd;
    console.log('Selected JD : ' + this.jd);
    if (jd.length > 10) {
      this.apiService.uploadJD(this.jd).subscribe((res) => {
        alert(res.message);
      });
    } else {
      alert('No Proper JD is given');
    }
  }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
    console.log('Selected File : ' + this.selectedFile?.name);

    if (this.selectedFile) {
      this.isFileUploaded = false
      this.apiService.uploadResume(this.selectedFile).subscribe({
        next:(res) => {
        alert(res.message);
        this.isFileUploaded = true
        this.cdr.detectChanges();
        },
        error:(data)=>{
          console.log(data)
        },
        complete:()=>{
          
        }
        
      });
    } else {
      alert('No file selected.');
    }
  }
}
