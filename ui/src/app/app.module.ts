import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { TreeModule } from 'ng2-tree';
import { RouterModule,Routes} from '@angular/router';
import { TreeviewModule } from 'ngx-treeview';
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



import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { ProfileComponent } from './components/profile/profile.component';
import { AllUsersComponent } from './components/all-users/all-users.component';
const routes:Routes=[{path:'',component:HomeComponent},
              {path:'home',component:HomeComponent},
              {path:'user',component:UserProfileComponent},
              {path:'profile/:id',component:ProfileComponent},
              {path:'allUsers',component:AllUsersComponent}]

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    UserProfileComponent,
    ProfileComponent,
    AllUsersComponent
  ],
  imports: [
    ReactiveFormsModule,
   FormsModule,
    TreeModule,
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(
      routes,
     {useHash:true} 
    ),
      TreeviewModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
