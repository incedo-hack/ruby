import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { Http } from '@angular/http';
import { NodeEvent, TreeModel, RenamableNode, Ng2TreeSettings } from 'ng2-tree';



@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
    /*clicked:boolean=false;
user={name:"John",country:"Uk","state":"Manchester"}*/
    navigatedUserId:number;
    userInfo:any;
    userPermissions:any;
    userPermissionsTree:any;
    userPermissionsTreeArr:any=[];
    title:string;
    hasPermissions:boolean=false;
    public settings: Ng2TreeSettings = {
    rootIsVisible: false,
  };
       pls: TreeModel;

  constructor(private route:ActivatedRoute,private router:Router,private http:Http) { }

  ngOnInit() {
      this.route.params.subscribe(params=>{
this.navigatedUserId = params["id"];
          console.log(this.navigatedUserId);
      });
      this.getUserProfile();
  }
    getUserProfile():void{
        this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/users/" + this.navigatedUserId)
        .subscribe(data=>{
            this.userInfo=data.json();
            if(this.userInfo["permissions"]){
                this.userPermissions = JSON.parse(this.userInfo["permissions"]);
                for(var i=0;i<this.userPermissions.length;i++){
                    this.getUserPermissions(this.userPermissions[i]);
                }
            }
        },err=>{
            console.log(err);
        })
    }
     getUserPermissions(id):void{
         this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/hierarchy/" + id)
         .subscribe(data=>{
             this.pls=data.json();
             this.hasPermissions=true;
             this.userPermissionsTreeArr.push(this.pls);
             console.log(this.userPermissionsTreeArr);
             const arrayToObject = (array) =>
               array.reduce((obj, item) => {
                 obj = item
                 return obj
               }, {});
             this.userPermissionsTree=arrayToObject(this.userPermissionsTreeArr);
             console.log(this.userPermissionsTree);
             this.title=this.userPermissionsTree.value;
         },err=>{
             console.log("err",err);
             this.hasPermissions=false;
         })
     }
 /*editProfile():void{
    this.clicked = !this.clicked;
    console.log(this.clicked);
}
    cancel():void{
        this.clicked=!this.clicked;
    }
    updateProfile(){
        
    }*/
}
