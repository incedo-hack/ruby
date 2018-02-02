import { Component, OnInit } from '@angular/core';
import { TreeviewItem, TreeviewConfig } from 'ngx-treeview';
import {
   ReactiveFormsModule,
   FormsModule,
   FormGroup,
   FormControl,
   Validators,
   FormBuilder,
   AbstractControl, 
   ValidatorFn,
} from '@angular/forms';
import { Http } from '@angular/http';
import { NodeEvent, TreeModel, RenamableNode, Ng2TreeSettings } from 'ng2-tree';
declare const alertify:any;


@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
    createUserForm:FormGroup;
    accounts:any;
    selectedBranchId:number;
    selectedPermissionId:any;
    public settings: Ng2TreeSettings = {
    rootIsVisible: false,
  };
  
   permissionsTree: TreeModel;
  constructor(private http:Http) { }

  ngOnInit() {
      this.selectedBranchId=null;
      this.createForm();
      this.getAccounts();
  }
    getAccounts():void{
        this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/accounts")
        .subscribe(data=>{
            this.accounts=data.json();
        },err=>{
            console.log(err);
        })
    }
    
   selectedBranch(id):void{
this.selectedBranchId=id;
       this.getHierachy();
   }
    createUser():void{
        const per=[this.selectedPermissionId];
        const body={
                "role": this.createUserForm.value.role,
                "user_name": this.createUserForm.value.userName,
                "first_name": this.createUserForm.value.firstName,
                "last_name": this.createUserForm.value.lastName,
                "phone_number": this.createUserForm.value.phone,
                "email_id": this.createUserForm.value.email,
                "account_id": this.selectedBranchId,
                "permissions": JSON.stringify(per)
        }
        console.log(body);
        this.http.post("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/users",body)
        .subscribe(data=>{
            console.log(data.json());
            window.alert("user created");
        },err=>{
            console.log(err);
            window.alert("user creation failed");
        });
    }
    getHierachy(){
    this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/hierarchy-by-account/" + this.selectedBranchId).subscribe(data=>{
        this.permissionsTree=data.json();
        
    },err=>{
        console.log(err);
    })
}
    public onNodeSelected(e: NodeEvent): void {
    UserProfileComponent.logEvent(e, 'Selected');
        this.selectedPermissionId=e.node.id;
  }

  private static logEvent(e: NodeEvent, message: string): void {
    console.log(e);
    alertify.message(`${message}: ${e.node.value}`);
  }
    private createForm(){
   this.createUserForm =new FormGroup({
   firstName:new FormControl(''),
   lastName:new FormControl(''),
       userName:new FormControl(''),
       email:new FormControl(''),
       phone:new FormControl(''),
   role:new FormControl(''),
       })
}
}
