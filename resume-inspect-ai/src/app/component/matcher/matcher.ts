import { Component, ChangeDetectorRef } from '@angular/core';
import { ApiService } from '../../service/api-service';
import { CommonModule } from '@angular/common';
import { ProfileReport } from '../../model/profileReport.interface';

@Component({
  selector: 'app-matcher',
  imports: [CommonModule],
  templateUrl: './matcher.html',
  styleUrl: './matcher.css',
})
export class Matcher {
  selectedFile: File | undefined;
  jd: String = '';
  report: ProfileReport[]  = [];
  matchingReportsErr: any = 'ResumeErr';
  isMatchingTrigger = false;
  hasMatchingReport = false;

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
      this.apiService.uploadResume(this.selectedFile).subscribe((res) => {
        alert(res.message);
      });
    } else {
      alert('No file selected.');
    }
  }
}
