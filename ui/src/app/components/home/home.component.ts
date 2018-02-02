import { Component, OnInit } from '@angular/core';
import { NodeEvent, TreeModel, RenamableNode, Ng2TreeSettings } from 'ng2-tree';
import { Http } from '@angular/http';
import { Router } from '@angular/router';
declare const alertify:any;


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
userCount:number;
    accountCount:number;
    branchCount:number;
  constructor(private http:Http,
              private router:Router) {
  }
 
public settings: Ng2TreeSettings = {
    rootIsVisible: false,
  };
  
   pls: TreeModel;

  public ngOnInit(): void {
    this.getHierachy();
      this.getAccountsCount();
      this.getBranchCount();
      this.getUserCount();
  }
getHierachy(){
    this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/hierarchy/20").subscribe(data=>{
        this.pls=data.json();
        
    },err=>{
        console.log(err);
    })
}
    goToAllUsers(){
        this.router.navigate(['allUsers'])
    }
  public onNodeRemoved(e: NodeEvent): void {
    HomeComponent.logEvent(e, 'Removed');
  }

  public onNodeMoved(e: NodeEvent): void {
    HomeComponent.logEvent(e, 'Moved');
  }

  public onNodeRenamed(e: NodeEvent): void {
    HomeComponent.logEvent(e, 'Renamed');
  }

  public onNodeCreated(e: NodeEvent): void {
    HomeComponent.logEvent(e, 'Created');
  }

  public onNodeSelected(e: NodeEvent): void {
    HomeComponent.logEvent(e, 'Selected');
  }

  private static logEvent(e: NodeEvent, message: string): void {
    console.log(e);
    alertify.message(`${message}: ${e.node.value}`);
  }
    getUserCount(){
        this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/users")
        .subscribe(data=>{
            let response =data.json();
            this.userCount=response.length;
        },err=>{
            console.log(err)
        })
    }
    getAccountsCount(){
        this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/accounts")
        .subscribe(data=>{
            let response =data.json();
            this.accountCount=response.length;
        },err=>{
            console.log(err)
        })
    }
    getBranchCount(){
        this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/branches")
        .subscribe(data=>{
            let response =data.json();
            this.branchCount=response.length;
        },err=>{
            console.log(err)
        })
    }
}
