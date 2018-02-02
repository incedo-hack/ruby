import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Router, ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-all-users',
  templateUrl: './all-users.component.html',
  styleUrls: ['./all-users.component.css']
})
export class AllUsersComponent implements OnInit {
users:any=["john","sam","aj"]

  constructor(private http:Http,private router:Router) { }

  ngOnInit() {
      this.getUsers();
  }
    getUsers():void{
        this.http.get("https://djvp2idgi0.execute-api.ap-south-1.amazonaws.com/dev/users")
        .subscribe(data=>{
            this.users=data.json();
            console.log(this.users);
        },err=>{
            console.log(err);
        })
    }
    
    goToUser(id):void{
        this.router.navigate(['profile',id]);
    }

}
