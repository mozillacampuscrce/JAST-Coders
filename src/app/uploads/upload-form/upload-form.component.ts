import { Component, OnInit } from '@angular/core';
import { UploadService } from '../shared/upload.service';
import { Upload } from '../shared/upload';
import * as _ from "lodash";
import {AuthService} from '../../services/auth.service';
@Component({
  selector: 'app-upload-form',
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.css']
})
export class UploadFormComponent {

  selectedFiles: FileList;
  currentUpload: Upload;
  user: firebase.User;
  userPresent: Boolean ;
  
  constructor(private upSvc: UploadService,private serv: AuthService) { }

  detectFiles(event) {
      this.selectedFiles = event.target.files;
  }

  uploadSingle() {
    let file = this.selectedFiles.item(0)
    this.currentUpload = new Upload(file);
    this.upSvc.uploadFile(this.currentUpload);
    console.log(this.user.email);
  }

  uploadMulti() {
    let files = this.selectedFiles
    let filesIndex = _.range(files.length)
    _.each(filesIndex, (idx) => {
      this.currentUpload = new Upload(files[idx]);
      this.upSvc.uploadFile(this.currentUpload)}
    )
  }
  ngOnInit(){
    this.serv.getLoggedInUser().subscribe(usr => {
      if (usr) {
   this.user = usr;
      }
      })
  }

}